
# Interpreters
import pandas as pd
import openpyxl
from openpyxl.worksheet.table import Table, TableStyleInfo
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import os
import matplotlib.pyplot as plt
import numpy as np

# Input
code_file = Path(__file__).parent # Locates code
FlowYearDifferences = code_file.parent # Locates parent folder
input_file = FlowYearDifferences / 'HydrologyScenarios.xlsx' # Shows where the input is relative to where the code is

# Output
output_file = "NarrowTableDifferences.xlsx" # Names output
output_path = code_file / 'Results' / output_file   # Shows where the output is relative to where the code is

sheet_names = pd.ExcelFile(input_file).sheet_names  # Variable for ease of access to all the sheets in HydrologyScenarios.xlsx


# Specifies which sheets not to read.
excluded_sheets = ["ReadMe", "AvailableHydrologyScenarios", "ScenarioListForAnalysis", "AvailableMetrics", "MetricsForAnalysis", "Heatmap", "Hist"]

columns_series = [] # Empty list to store columns to create wide table


for ensemble_input in sheet_names:
    if ensemble_input in excluded_sheets: # Skips over sheets listed in excluded_sheets
        continue

    # Reads and converts values in ensembles to numeric values
    ensemble = pd.read_excel(input_file, sheet_name=ensemble_input, header=0)  # Ensure first row is used as column names
    data_cols = ensemble.columns[1:] # Ignores first column

    if len(data_cols) > 0: # Converts all data_cols to numeric
        ensemble.loc[:, data_cols] = ensemble.loc[:, data_cols].apply(pd.to_numeric, errors='coerce')

    if 'ISM' in ensemble_input:  # Selects ensembles with 'ISM' in the title
        trace = data_cols[0] # Selects only the first column
        vals = ensemble[trace].reset_index(drop=True) # Removes row numbers to rid index errors
        extra = vals.iloc[[0]].reset_index(drop=True) # Selects first value in the column
        vals = pd.concat([vals, extra]).reset_index(drop=True) # Adds the first value onto the end of the column

        col_name = f"{ensemble_input}::{trace}"  # Creates a new column name to avoid repeats and pandas creating a new name
        columns_series.append((col_name, vals)) # Adds the column name and the data to the list

    else:
        # All other traces
        for trace in data_cols:
            vals = ensemble[trace].reset_index(drop=True) # Removes row numbers to rid index errors
            col_name = f"{ensemble_input}::{trace}" # Creates a new column name to avoid repeats and pandas creating a new name
            columns_series.append((col_name, vals)) # Adds the column name and the data to the list

if columns_series: # Adds all of the columns from the list to the wide data set side by side and assigns series name as column name
    df_wide = pd.concat([s.rename(c) for c, s in columns_series], axis=1)

# Computes year to year differences and rounds to three decimal points
# Negative value is a DECREASE in flow from year i to i+1, positive is an INCREASE in flow from year i to i+1.
difference_df = df_wide.diff().round(3)

# Narrow Flow
    # Converts row numbers (years) into a column as well as a column for the traces. The values go into the flow column
narrow_flow = (df_wide.reset_index().melt(id_vars=['index'], var_name='Ensemble::Trace', value_name='Flow'))
narrow_flow.round(3) # Rounds the values above

# Narrow Difference
    # Converts differences to a column
narrow_diff = (difference_df.reset_index().melt(id_vars=['index'], var_name='Ensemble::Trace', value_name='Difference'))

# Merge
    # Adds flow column and difference column into the same dataframe
narrow_df = narrow_flow.merge(narrow_diff, on=['index', 'Ensemble::Trace'])

# Drops rows where there is no data for the flow and difference (Scalable)
narrow_df = narrow_df.dropna(subset=['Flow', 'Difference'], how='all').reset_index(drop=True)


# Rename index to Year
narrow_df.rename(columns={'index': 'Year'}, inplace=True)

# Splits the 'Ensemble::Trace' identifier used for the wide table and creates different column for them
narrow_df[['Ensemble', 'Trace']] = narrow_df['Ensemble::Trace'].str.split("::", expand=True)

# Reorders columns
narrow_df = narrow_df[['Ensemble', 'Trace', 'Year', 'Flow', 'Difference']]


# Converts Excel to csv
csv_path = output_path.with_suffix('.csv')
narrow_csv = narrow_df.to_csv(csv_path, index=False)


# ## Histogram ##
# hist_df = pd.read_csv(csv_path) # Reads input
#
# diffs = narrow_df['Difference'].dropna() # Calls difference column and drops empty values
#
# rounded = diffs.round(0).astype(int) # Rounds differences to nearest whole value and converts to integers
#
# negatives = rounded[rounded < 0] # Calls only negative integers
#
# counts = negatives.value_counts().sort_index() # Counts negative integer occurrences and sorts them
# x_range = list(range(-20, 0)) # Creates range
# counts = counts.reindex(x_range, fill_value=0)
# histogram_df = counts.reset_index() # Creates counted index
# histogram_df.columns = ['Difference', 'Occurrence'] # Calls histogram data
#
# hist_csv_path = output_path.parent / 'Hist_Differences.csv' # Saves histogram path
# histogram_df.to_csv(hist_csv_path, index=False) #
#
# # Creates new figure that is the histogram
# plt.figure(figsize=(10, 6))
# plt.bar(histogram_df['Difference'], histogram_df['Occurrence'])
# plt.xlabel('Year to Year Change in Flow (million acre-feet per year')
# plt.ylabel('Occurrence')
# plt.title('Flow Year Differences')
# plt.xticks(x_range)  # still show -20..-1 ticks (optional)
# plt.subplots_adjust(left=0.06, right=0.98, top=0.93, bottom=0.12)
# plt.grid(axis='y', linestyle='--', alpha=0.3)
# plt.tight_layout()
#
# # Saves histogram as a png
# hist_png_path = output_path.parent / 'FlowYearDifferences_hist.png'
# plt.savefig(hist_png_path, dpi=300)
#
# # Shows histogram
# plt.show()


# # POSITIVE HISTOGRAM
# ## Histogram ##
hist_df = pd.read_csv(csv_path) # Reads input
#
# diffs = narrow_df['Difference'].dropna() # Calls difference column and drops empty values
#
# rounded = diffs.round(0).astype(int) # Rounds differences to nearest whole value and converts to integers
#
#  # Calls only positive integers
#
# counts = rounded.value_counts().sort_index() # Counts negative integer occurrences and sorts them
# x_range = list(range(-20, 20)) # Creates range
# counts = counts.reindex(x_range, fill_value=0)
# histogram_df = counts.reset_index() # Creates counted index
# histogram_df.columns = ['Difference', 'Occurrence'] # Calls histogram data
#
# hist_csv_path = output_path.parent / 'Hist_Differences.csv' # Saves histogram path
# histogram_df.to_csv(hist_csv_path, index=False) #
#
# # Creates new figure that is the histogram
# plt.figure(figsize=(10, 6))
# plt.bar(histogram_df['Difference'], histogram_df['Occurrence'])
# plt.xlabel('Year to Year Change in Flow (million acre-feet per year)')
# plt.ylabel('Occurrence')
# plt.title('Flow Year Differences')
# plt.xticks(x_range)
# plt.subplots_adjust(left=0.06, right=0.98, top=0.93, bottom=0.12)
# plt.grid(axis='y', linestyle='--', alpha=0.3)
# plt.tight_layout()
#
# # Saves histogram as a png
# hist_png_path_positive = output_path.parent / 'POSTIVEFlowYearDifferences_hist.png'
# plt.savefig(hist_png_path_positive, dpi=300)
#
# # Shows histogram
# plt.show()


# Create the histogram
# 12 bins
# Plot from 0 to -12. X-axis labels as positive 0, 1, 2, 3 ... 12


plt.hist(data, bins=20)  # Using 20 bins
# Add labels and a title
plt.xlabel("Annual decrease in flow (million acre-feet per year)")
plt.ylabel("Percent")
#plt.title("Histogram of Sample Data")


#print(f"Histogram image saved to: {hist_png_path}")

print(f"\nResults saved to:\n{csv_path}")

