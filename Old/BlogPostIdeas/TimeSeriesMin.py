import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locates code and input
code_file = Path(__file__)
input_file = code_file.parent / 'LowStorageBlogGraph.xlsx'

# Reads the input and forces values into numeric
ensemble = pd.read_excel(input_file)
ensemble.iloc[:, 3:7] = ensemble.iloc[:, 3:7].apply(pd.to_numeric, errors="coerce")

# Defines each session to three rows
session_data = 3
length = len(ensemble)

# Builds arrays storages in sessions
all_years = []
all_elevs = []
protect_storages = []
protect_elevs = []

for first in range(0, length, session_data):
    sessions = ensemble.iloc[first:first + session_data, 3:7]  # Extracts year columns
    years = sessions.iloc[0].values  # Locates year storage data in sessions
    all_years.append(years)

    elevs = sessions.iloc[2].values  # Locates year storage data in sessions
    all_elevs.append(elevs)

    protect_s = ensemble.iloc[first:first + session_data, 2]  # Extracts protect column
    storage = protect_s.iloc[0]
    protect_storages.append(storage)

    protect_e = ensemble.iloc[first:first + session_data, 2]  # Extracts protect column
    elevation = protect_e.iloc[2]
    protect_elevs.append(elevation)

all_years = np.array(all_years)

aug_eighteen_storage = all_years[2]
aug_eighteen_protect_s = protect_storages[2]
aug_eighteen_elevation = all_elevs[2]
aug_eighteen_protect_e = protect_elevs[2]

year_header = np.array(list(ensemble.columns)[3:7])

print(year_header)
print(aug_eighteen_storage)
print(aug_eighteen_protect_s)
print(aug_eighteen_protect_e)
print(aug_eighteen_elevation)

aug_eighteen_protect_s_series = np.repeat(aug_eighteen_protect_s, len(year_header))



fig, ax1 = plt.subplots()
ax1.plot(year_header, aug_eighteen_storage, marker='o', markersize=8, linewidth=3,
         label='Storage', color='tab:blue')
ax1.plot(year_header, aug_eighteen_protect_s_series, marker='d', markersize=8,
         color='red', linewidth=3, label='Protection Limit')


storage_ticks = [0.0, aug_eighteen_protect_s, aug_eighteen_storage.max()]


ax1.set_ylim(0, aug_eighteen_storage.max() * 1.05)

ax1.set_yticks(storage_ticks)


ax1.set_ylabel('Storage (million acre-feet)', fontweight='bold', fontsize=20)
ax1.tick_params(axis='y', labelsize=17)
ax1.tick_params(axis='x', labelsize=17)
for label in ax1.get_xticklabels() + ax1.get_yticklabels():
    label.set_fontweight('bold')
ax1.grid(linewidth=1)
ax1.set_xlabel(None, fontweight='bold', fontsize=20)



all_S_data = np.concatenate(all_years)
all_E_data = np.concatenate(all_elevs)

S_anchor_base = np.concatenate([protect_storages, all_S_data]).astype(float)
E_anchor_base = np.concatenate([protect_elevs, all_E_data]).astype(float)

S_anchor = np.append(S_anchor_base, 0.0)
E_anchor = np.append(E_anchor_base, 0.0)

valid_indices = ~np.isnan(S_anchor) & ~np.isnan(E_anchor)
S_anchor = S_anchor[valid_indices]
E_anchor = E_anchor[valid_indices]

order = np.argsort(S_anchor)
S_sorted = S_anchor[order]
E_sorted = E_anchor[order]



ax2 = ax1.twinx()


ax2.set_ylim(ax1.get_ylim())


ax2.set_yticks(storage_ticks)

elev_labels = np.interp(storage_ticks, S_sorted, E_sorted)


ax2.set_yticklabels([f"{e:.1f}" for e in elev_labels], fontweight='bold')
ax2.set_ylabel('Elevation (feet)', fontweight='bold', fontsize=20)
ax2.tick_params(axis='y', labelsize=17)

ax1.legend(loc='best', fontsize=17, frameon=True)

plt.savefig('TimeSeriesMin.png')
plt.show()
