import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locates code and input
code_file = Path(__file__)
input_file = code_file.parent / 'LowStorageBlogGraph.xlsx'

# Reads the input and forces values into numeric
ensemble = pd.read_excel(input_file)
ensemble.iloc[:, 3:6] = ensemble.iloc[:, 3:6].apply(pd.to_numeric, errors="coerce")

# Defines each session to three rows
session_data = 3
length = len(ensemble)

# Builds arrays storages in sessions
all_years = []
all_elevs = []
protect_storages = []
protect_elevs = []

for first in range(0, length, session_data):
    sessions = ensemble.iloc[first:first + session_data, 3:6]   # Extracts year columns

    years = sessions.iloc[0].values  # Locates year storage data in sessions
    all_years.append(years)

    elevs = sessions.iloc[2].values  # Locates year storage data in sessions
    all_elevs.append(elevs)

    protect_s = ensemble.iloc[first:first + session_data, 2]   # Extracts protect column
    storage = protect_s.iloc[0]
    protect_storages.append(storage)

    protect_e = ensemble.iloc[first:first + session_data, 2]   # Extracts protect column
    elevation = protect_e.iloc[2]
    protect_elevs.append(elevation)


all_years = np.array(all_years)
aug_twenty_storage = all_years[0]
aug_twenty_protect_s = protect_storages[0]
aug_twenty_elevation = all_elevs[0]
aug_twenty_protect_e = protect_elevs[0]
year_header = np.array(list(ensemble.columns)[3:6])

print(year_header)
print(aug_twenty_storage)
print(aug_twenty_protect_s)
print(aug_twenty_protect_e)
print(aug_twenty_elevation)

aug_twenty_protect_s_series = np.repeat(aug_twenty_protect_s, len(year_header))

# y-axis (storage)
fig, ax1 = plt.subplots()
ax1.plot(year_header, aug_twenty_storage, marker='o', markersize=8, linewidth=3, label='Storage', color='tab:blue')
ax1.plot(year_header, aug_twenty_protect_s_series, marker='d', markersize=8,color='red', linewidth=3, label='Protection Limit')
ax1.set_ylim(bottom=0)
ax1.set_ylabel('Storage', fontweight='bold', fontsize=12)
ax1.tick_params(axis='y', labelsize=11)
ax1.tick_params(axis='x', labelsize=11)

for label in ax1.get_xticklabels() + ax1.get_yticklabels():
    label.set_fontweight('bold')

ax1.grid(linewidth=1)
ax1.set_xlabel(None, fontweight='bold', fontsize=12)

# Secondary y-axis (elevation)
ax2 = ax1.twinx()

# Match the y limits and ticks to the left axis
ax2.set_ylim(ax1.get_ylim())
ax2.set_yticks(ax1.get_yticks())

order = np.argsort(aug_twenty_storage)
S_sorted = aug_twenty_storage[order]
E_sorted = aug_twenty_elevation[order]

# Interpolate elevation labels from the Excel pairs
elev_labels = np.interp(ax1.get_yticks(), S_sorted, E_sorted)

# Apply labels
ax2.set_yticklabels([f"{e:.1f}" for e in elev_labels], fontweight='bold')
ax2.set_ylabel('Elevation (ft)', fontweight='bold', fontsize=12)
ax2.tick_params(axis='y', labelsize=11)

# Set labels and formatting
ax2.set_yticklabels([f"{e:.1f}" for e in elev_labels], fontweight='bold')
ax2.set_ylabel('Elevation (ft)', fontweight='bold', fontsize=12)
ax2.tick_params(axis='y', labelsize=11)

# Legend and title
ax1.legend(loc='best', fontsize=11, frameon=True)
plt.savefig('TimeSeries.png')
plt.show()

# Creating box plot figure
# plt.plot(year_header, aug_twenty_storage, marker='o', label='Storage')
# plt.plot(year_header, aug_twenty_protect_s_series, color='red', label='Protection Limit')
# plt.ylim(bottom=0)
# plt.grid()
# plt.ylabel('Storage')
# plt.legend()