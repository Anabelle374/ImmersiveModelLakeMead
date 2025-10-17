import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locates code and input
code_file = Path(__file__)
input_file = code_file.parent / 'LowStorageBlogGraph.xlsx'

# Reads the input and forces values into numeric
ensemble = pd.read_excel(input_file)
ensemble.iloc[:, 3:6] = ensemble.iloc[:, 3:6].apply(pd.to_numeric,
                                                    errors="coerce")  # Selects data and converts to numeric

# Defines each session to three rows
session_data = 3
first_data_row = ensemble.iloc[:, 3].first_valid_index()
df = ensemble.iloc[first_data_row:].copy().reset_index(drop=True)
length = len(df)

# Build arrays: storages by session, elevations, protect values, session names
all_years = []  # storage values (Year1, Year2, Year3) for each session
all_elevs = []  # elevation display rows (the Year columns for elevation row)
protect_storages = []  # "Set to Protect" storage (column C in your layout)
protect_elevs = []  # "Set to Protect" elevation (also from column C, elevation row)
session_names = []
all_storage_protect = []  # List to hold the Storage/Protect year-end values

for first in range(0, length, session_data):
    sessions = df.iloc[first:first + session_data, 3:6]  # Extracts year columns for the 3 rows in the session

    # The first row of sessions is Storage (Year1..Year3)
    years = sessions.iloc[0].values
    all_years.append(years)

    # Get the second row (Storage/Protect) year-end values
    storage_protect_vals = sessions.iloc[1].values
    all_storage_protect.append(storage_protect_vals)

    # The third row of sessions is the Elevation (Year1..Year3)
    elevs = sessions.iloc[2].values
    all_elevs.append(elevs)

    # "Set to Protect" is in column index 2 relative to the original ensemble (column C)
    protect_col = df.iloc[first:first + session_data, 2]
    # Set-to-protect storage value is the first row in the group (Storage cell in your sheet)
    protect_storage = protect_col.iloc[0]
    protect_storages.append(protect_storage)

    # Set-to-protect elevation is the third row in the group (Elevation cell in your sheet)
    protect_elevation = protect_col.iloc[2]
    protect_elevs.append(protect_elevation)

    session_name = df.iloc[first, 0]
    session_names.append(session_name)

# Convert lists to numpy arrays for easier math
all_storages = np.array(all_years)  # shape: (n_sessions, 3)
all_elevs = np.array(all_elevs)
protect_storages = np.array(protect_storages, dtype=float)
protect_elevs = np.array(protect_elevs, dtype=float)
all_storage_protect = np.array(all_storage_protect)

# Compute dimensionless ratios: storage / protect_storage (per session)
dimensionless_list = []
for idx, ps in enumerate(protect_storages):
    # Avoid division by zero (coerce to nan if zero)
    if ps == 0 or np.isnan(ps):
        dimensionless = np.full(all_storages[idx].shape, np.nan)
    else:
        dimensionless = all_storages[idx] / ps
    dimensionless = np.round(dimensionless, 1)
    dimensionless_list.append(dimensionless)
dimensionless_list = np.array(dimensionless_list)  # shape: (n_sessions, 3)

# Prepare plotting
plt.figure(figsize=(12, 7))
ax = plt.gca()

all_x = []
all_y = []

# Flatten the data for plotting (3 points per session, x is the session's protect elevation)
for i in range(len(protect_elevs)):
    x_values = [protect_elevs[i]] * 3  # same elevation for the 3 storage values
    y_values = dimensionless_list[i].tolist()  # 3 storage ratios

    all_x.extend(x_values)
    all_y.extend(y_values)

# Determine color for each point (red if < 1.0 else blue)
point_colors = ['red' if (y < 1.0) else 'blue' for y in all_y]

# Scatter the points
plt.scatter(all_x, all_y, color=point_colors, s=100, alpha=0.9)

# --- horizontal red line at y = 1.0 ---
plt.axhline(1.0, color='red', linewidth=2.0, linestyle='-')

# Axis labels and style
plt.xlabel('Protection Elevation\n(Protect Storage: Set to Protect)', fontsize=12, fontweight='bold')
plt.ylabel('Storage / Protect Storage', fontsize=12, fontweight='bold')

# --- NEW: Code to build correct labels for grouped ticks ---

# Create a dataframe to hold all data, making it easy to group
plot_data = pd.DataFrame({
    'session': session_names,
    'elevation': protect_elevs,
    'storages': all_storages.tolist(),
    'sp_values': all_storage_protect.tolist()
})

# Get unique elevations *in sorted order*
unique_elevs = np.sort(np.unique(plot_data['elevation'].dropna()))

xtick_labels = []
for elev in unique_elevs:
    # Get all sessions for this elevation
    sessions_at_elev = plot_data[plot_data['elevation'] == elev]

    # Format elevation
    if np.isfinite(elev) and abs(elev - round(elev)) < 1e-6:
        elev_str = f"{int(round(elev))}"
    else:
        elev_str = f"{elev:.1f}"

    # Build multi-line label for ALL sessions at this elevation
    sp_labels = []
    for idx, row in sessions_at_elev.iterrows():
        # Get the 3 'Storage/Protect' values
        stor_vals = row['sp_values']
        stor_formatted = ", ".join([f"{s:.1f}" if not np.isnan(s) else "NaN" for s in stor_vals])
        # Add session name for clarity (optional, but good)
        sp_labels.append(f"{row['session']}: ({stor_formatted})")

    # Join all groups with a newline
    all_sp_labels = "\n".join(sp_labels)

    # Final label is Elevation on line 1, and all session data below
    label = f"{elev_str}\n{all_sp_labels}"
    xtick_labels.append(label)

# Apply ticks and labels
ax.set_xticks(unique_elevs)
ax.set_xticklabels(xtick_labels, fontsize=9, fontweight='bold')  # Reduced font size

# --- End of new tick code ---

# Bold y ticks
for label in ax.get_yticklabels():
    label.set_fontweight('bold')

# Grid and y-limits
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(bottom=0)

# Optional: improve layout so multi-line xticks are not clipped
plt.tight_layout()

# Save and show
plt.savefig("SessionDotPlotFinal_CorrectLabels.png", dpi=200)
plt.show()