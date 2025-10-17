#########
# This file shows a plot of a storage ratio (Lake Mead storage / Protection Elevation) for each protection elevation in recent Lake Mead Immersive model sessions.
# 
# We save the figure to a png picture file.

# This script reads in compiled results from the LowStorageBlogGraph.xlsx file
#
# Anabelle Myers
# October 17, 2025
# A02369941@aggies.usu.edu
###########################



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locates code and input
code_file = Path(__file__)

#This file is organized as columns of [Session][Variable][Protection Elevation][Year 1][Year 2][Year 3]
input_file = code_file.parent / 'LowStorageBlogGraph.xlsx'

# Reads the input and forces values into numeric
ensemble = pd.read_excel(input_file)
ensemble.iloc[:, 3:6] = ensemble.iloc[:, 3:6].apply(pd.to_numeric, errors="coerce")   # Selects data and converts to numeric

# Defines each session to three rows
session_data = 3
first_data_row = ensemble.iloc[:, 3].first_valid_index()
df = ensemble.iloc[first_data_row:].copy().reset_index(drop=True)
length = len(df)


all_years = []
all_elevs = []
protect_storages = []
protect_elevs = []
session_names = []

for first in range(0, length, session_data):
    sessions = df.iloc[first:first + session_data, 3:6]

    years = sessions.iloc[0].values
    all_years.append(years)

    elevs = sessions.iloc[2].values
    all_elevs.append(elevs)

    protect_col = df.iloc[first:first + session_data, 2]
    protect_storage = protect_col.iloc[0]
    protect_storages.append(protect_storage)

    protect_elevation = protect_col.iloc[2]
    protect_elevs.append(protect_elevation)

    session_name = df.iloc[first, 0]
    session_names.append(session_name)

all_storages = np.array(all_years)
all_elevs = np.array(all_elevs)
protect_storages = np.array(protect_storages, dtype=float)
protect_elevs = np.array(protect_elevs, dtype=float)

dimensionless_list = []
for idx, ps in enumerate(protect_storages):
    if ps == 0 or np.isnan(ps):
        dimensionless = np.full(all_storages[idx].shape, np.nan)
    else:
        dimensionless = all_storages[idx] / ps
    dimensionless = np.round(dimensionless, 1)
    dimensionless_list.append(dimensionless)
dimensionless_list = np.array(dimensionless_list)

#
plt.figure(figsize=(12, 7))
ax = plt.gca()

all_x = []
all_y = []

for i in range(len(protect_elevs)):
    x_values = [protect_elevs[i]] * 3
    y_values = dimensionless_list[i].tolist()
    all_x.extend(x_values)
    all_y.extend(y_values)

point_colors = ['red' if (y < 1.0) else 'blue' for y in all_y]

plt.scatter(all_x, all_y, color=point_colors, s=100, alpha=0.9)

plt.axhline(1.0, color='red', linewidth=2.0, linestyle='-')

plt.xlabel('Protection Elevation\n(Protect Storage: Set to Protect)', fontsize=12, fontweight='bold')
plt.ylabel('Storage / Protect Storage', fontsize=12, fontweight='bold')


unique_elevs = protect_elevs.tolist()
xtick_labels = []
for i, elev in enumerate(unique_elevs):
    if np.isfinite(elev) and abs(elev - round(elev)) < 1e-6:
        elev_str = f"{int(round(elev))}"
    else:
        elev_str = f"{elev:.1f}"

    stor_vals = all_storages[i] if i < len(all_storages) else [np.nan, np.nan, np.nan]
    stor_formatted = ", ".join([f"{s:.1f}" if not np.isnan(s) else "NaN" for s in stor_vals])

    label = f"{elev_str}\n{stor_formatted}"
    xtick_labels.append(label)

ax.set_xticks(unique_elevs)
ax.set_xticklabels(xtick_labels, fontsize=10, fontweight='bold')

for label in ax.get_yticklabels():
    label.set_fontweight('bold')

ax.grid(True, linestyle='--', alpha=0.6)
ax.set_ylim(bottom=0)


plt.tight_layout()

plt.savefig("SessionDotPlotFinal.png", dpi=200)
plt.show()
