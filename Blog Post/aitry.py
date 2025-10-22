import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ------------------------------------------------------------
# Load data
# ------------------------------------------------------------
code_file = Path(__file__)
input_file = code_file.parent / 'LowStorageBlogGraph.xlsx'

# Reads the input and forces values into numeric
ensemble = pd.read_excel(input_file)
ensemble.iloc[:, 3:6] = ensemble.iloc[:, 3:6].apply(pd.to_numeric, errors="coerce")

# ------------------------------------------------------------
# Parse the session data
# ------------------------------------------------------------
session_data = 3
length = len(ensemble)

all_years = []
all_elevs = []
protect_storages = []
protect_elevs = []

for first in range(0, length, session_data):
    sessions = ensemble.iloc[first:first + session_data, 3:6]
    years = sessions.iloc[0].values                    # storage row
    elevs = sessions.iloc[2].values                    # elevation row
    all_years.append(years)
    all_elevs.append(elevs)

    protect_s = ensemble.iloc[first:first + session_data, 2]
    storage = protect_s.iloc[0]
    elevation = protect_s.iloc[2]
    protect_storages.append(storage)
    protect_elevs.append(elevation)

# ------------------------------------------------------------
# Select session (example: May 22nd)
# ------------------------------------------------------------
all_years = np.array(all_years)
aug_twenty_storage = all_years[0]
aug_twenty_protect_s = protect_storages[0]
aug_twenty_elevation = all_elevs[0]
aug_twenty_protect_e = protect_elevs[0]
year_header = np.array(list(ensemble.columns)[3:6])

print("Years:", year_header)
print("Storage:", aug_twenty_storage)
print("Protect storage:", aug_twenty_protect_s)
print("Protect elevation:", aug_twenty_protect_e)
print("Elevation:", aug_twenty_elevation)

# ------------------------------------------------------------
# Plot - Storage
# ------------------------------------------------------------
aug_twenty_protect_s_series = np.repeat(aug_twenty_protect_s, len(year_header))

fig, ax1 = plt.subplots()
ax1.plot(year_header, aug_twenty_storage, marker='o', markersize=8, linewidth=3,
         label='Storage', color='tab:blue')
ax1.plot(year_header, aug_twenty_protect_s_series, marker='d', markersize=8,
         color='red', linewidth=3, label='Protection Limit')

ax1.set_ylim(bottom=0)
ax1.set_ylabel('Storage', fontweight='bold', fontsize=12)
ax1.tick_params(axis='y', labelsize=11)
ax1.tick_params(axis='x', labelsize=11)
for label in ax1.get_xticklabels() + ax1.get_yticklabels():
    label.set_fontweight('bold')
ax1.grid(linewidth=1)
ax1.set_xlabel(None, fontweight='bold', fontsize=12)

# ------------------------------------------------------------
# Plot - Elevation (Right axis)
# ------------------------------------------------------------
ax2 = ax1.twinx()

# Match y limits and ticks
ax2.set_ylim(ax1.get_ylim())
ax2.set_yticks(ax1.get_yticks())

# Build linear mapping with anchor points
# 0 storage -> 0 elevation
# protection storage -> 1000 ft
# storage values from Excel -> their elevation
S_anchor = np.array([0.0, aug_twenty_protect_s, *aug_twenty_storage], dtype=float)
E_anchor = np.array([0.0, 1000.0, *aug_twenty_elevation], dtype=float)

order = np.argsort(S_anchor)
S_sorted = S_anchor[order]
E_sorted = E_anchor[order]

# Interpolate labels
elev_labels = np.interp(ax1.get_yticks(), S_sorted, E_sorted)

ax2.set_yticklabels([f"{e:.1f}" for e in elev_labels], fontweight='bold')
ax2.set_ylabel('Elevation (ft)', fontweight='bold', fontsize=12)
ax2.tick_params(axis='y', labelsize=11)

# ------------------------------------------------------------
# Legend and export
# ------------------------------------------------------------
ax1.legend(loc='best', fontsize=11, frameon=True)
plt.savefig('TimeSeries.png')
plt.show()
