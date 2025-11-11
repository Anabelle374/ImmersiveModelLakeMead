import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locates code and input
code_file = Path(__file__)
input_file = code_file.parent / 'LowStorageBlogGraph.xlsx'

# Reads the input and forces values into numeric
ensemble = pd.read_excel(input_file)
ensemble = ensemble.apply(pd.to_numeric, errors='coerce')

# Defines each session to three rows
session_data = 3
length = len(ensemble)

# Builds arrays storages in sessions
all_years = []
for first in range(0, length, session_data):
    sessions = ensemble.iloc[first:first + session_data, 3:6]   # Extracts year columns
    years = np.array(sessions[:1])   # Locates year storage data in sessions
    all_years.append(years)
all_years = np.array(all_years)

# Builds arrays for protection storage
all_protect_storage = []
for first in range(0, length, session_data):
    sessions = ensemble.iloc[first:first + session_data, 2]   # Selects protected elevation column
    protect_storage = np.array(sessions[:1])   # Selects protected storage row
    all_protect_storage.append(protect_storage)
all_protect_storage = np.array(all_protect_storage)


# Calculates the dimensionless variable (storage/protected storage)
dimensionless = []
for first in range(0, len(ensemble), session_data):
    storage_vals = ensemble.iloc[first, 3:6].astype(float).values   # Selects storages for corresponding session
    protect_val_raw = ensemble.iloc[first, 2]   # Selects corresponding protected storage

    try:
        protect_val = float(protect_val_raw)   # Tries to convert protected storage to a float
    except Exception:   # If non-numeric, converts to NaN
        protect_val = np.nan

    if np.isnan(protect_val) or protect_val == 0:   # Checks if protected storage doesn't exist or is zero
        sp = np.array([np.nan, np.nan, np.nan])
    else:
        sp = np.round(storage_vals / protect_val, 1)   # If protected storage exists calculates dimensionless

    ensemble.iloc[first + 1, 3:6] = sp   # Writes calculated dimensionless into same columns second row
    dimensionless.append(sp)

# Builds array for dimensionless
dimensionless = np.array(dimensionless)
print("Dimensionless results (Storage/Protect):")
print(dimensionless)


dim = np.array(dimensionless)   # Copied dimensionless array
aps = np.array(all_protect_storage)   # Copied protected storage array

if dim.ndim == 3 and dim.shape[1] == 1:   # Checks shape of array to be 3D
    dim = dim[:, 0, :]   # Changes into a 2D array

if aps.ndim == 2 and aps.shape[1] == 1:   # Checks if 2D array
    elevs = aps[:, 0]   # Changes into 1D array

protected_rows = np.array([3, 6, 9, 12, 15, 18, 21])   # 0-based indices for Excel cells C4, C7, C10, C13, C16, C19, C22
protected_elevs = np.array([0, 0, 0, 0, 0, 0, 0])
for row in protected_rows:
    elev = ensemble.iloc[row, 2]   # Column C is index 2
    np.append(protected_elevs, elev)

data = []   # Data groups for box plots
labels = []   # Stores x axis labels
for e, sp_row in zip(protected_elevs, dim):   # Corresponds x value to box plot
    sp_clean = [float(v) for v in np.ravel(sp_row) if not np.isnan(v)]   # Removes NaNs
    if len(sp_clean) == 0:   # If no values
        data.append([np.nan])   # Place holder NaN
    else:
        data.append(sp_clean)   # Adds new 'cleaned' list to box plot


    if not np.isnan(e):   # If x value is valid
        labels.append(str(int(e)) if e == int(e) else str(e))   # Formats as integer if whole number, if not keeps as a string
    else:
        labels.append("NaN")   # NaN will be used as a label for missing x values

# Creating box plot figure
fig, ax = plt.subplots(figsize=(12, 6))
ax.boxplot(data, labels=labels, patch_artist=True, showmeans=True)
ax.set_xlabel('Protected Elevation (per session)')
ax.set_ylabel('Storage / Protected Storage')
ax.grid(axis='y', linestyle='--', alpha=0.4)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('BlogPostGraphTry.png')
plt.show()
