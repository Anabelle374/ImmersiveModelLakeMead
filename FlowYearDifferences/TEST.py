
# Interpreters
import pandas as pd
import openpyxl
from openpyxl.worksheet.table import Table, TableStyleInfo
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import os

# Input
code_file = Path(__file__).parent # Locates code
MinimumHydrologyScenarios = code_file.parent # Locates parent folder
input_file = MinimumHydrologyScenarios / 'HydrologyScenarios.xlsx' # Shows where the input is relative to where the code is

# Output
output_file = "BuildingTableNotEmpty.xlsx" # Names output a unique name
output_path = code_file / 'Results' / output_file   # Shows where the output is relative to where the code is

sheet_names = pd.ExcelFile(input_file).sheet_names  # Variable for ease of access to all the sheets in HydrologyScenarios.xlsx


# Specifies which sheets not to read.
excluded_sheets = ["ReadMe", "AvailableHydrologyScenarios", "ScenarioListForAnalysis", "AvailableMetrics", "MetricsForAnalysis", "Heatmap", "Hist"]

columns_series = []


for ensemble_input in sheet_names:
    if ensemble_input in excluded_sheets: # Skips over sheets listed in excluded_sheets
        continue

    # Reads and converts values in ensembles to numeric values
    ensemble = pd.read_excel(input_file, sheet_name=ensemble_input, header=0)  # Ensure first row is header
    data_cols = ensemble.columns[1:]

    if len(data_cols) > 0:
        ensemble.loc[:, data_cols] = ensemble.loc[:, data_cols].apply(pd.to_numeric, errors='coerce')

    if 'ISM' in ensemble_input:  # Selects ensembles with 'ISM' in the title
        trace = data_cols[0]
        vals = ensemble[trace].reset_index(drop=True)
        extra = vals.iloc[[0]].reset_index(drop=True)
        vals = pd.concat([vals, extra]).reset_index(drop=True)

        col_name = f"{ensemble_input}::{trace}"  # keeps sheet + trace so column names are unique
        columns_series.append((col_name, vals))

    else:
        # non-ISM: include all data columns
        for trace in data_cols:
            vals = ensemble[trace].reset_index(drop=True)
            col_name = f"{ensemble_input}::{trace}"
            columns_series.append((col_name, vals))

if columns_series:
    df_wide = pd.concat([s.rename(c) for c, s in columns_series], axis=1)
else:
    df_wide = pd.DataFrame()

# difference logic
difference_df = df_wide.diff().round(3)

# Narrow Flow
narrow_flow = (df_wide.reset_index().melt(id_vars=['index'], var_name='Ensemble::Trace', value_name='Flow'))
narrow_flow.round(3)
# Narrow Difference
narrow_diff = (difference_df.reset_index().melt(id_vars=['index'], var_name='Ensemble::Trace', value_name='Difference'))

# Merge
narrow_df = narrow_flow.merge(narrow_diff, on=['index', 'Ensemble::Trace'])

narrow_df.replace('', pd.NA, inplace=True)
narrow_df = narrow_df.dropna(subset=['Flow', 'Difference'], how='all').reset_index(drop=True)


# Rename index to Year
narrow_df.rename(columns={'index': 'Year'}, inplace=True)

# Split Ensemble & Trace (do this only once)
narrow_df[['Ensemble', 'Trace']] = narrow_df['Ensemble::Trace'].str.split("::", expand=True)

# Reorder columns
narrow_df = narrow_df[['Ensemble', 'Trace', 'Year', 'Flow', 'Difference']]


# Save to Excel with table formatting
csv_path = output_path.with_suffix('.csv')
narrow_df.to_csv(csv_path, index=False)

print(f"\nResults saved to:\n{csv_path}")

