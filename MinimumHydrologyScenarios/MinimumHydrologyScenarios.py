# MinimumHydrologyScenariosCode.py
#
#################

# Purpose
# This code iterates through all ensembles and traces in HydrologyScenarios.xlsx
#   by Homa Salehabadi (2023). During the iterations, the code finds the most minimum
#   consecutive years. The user chooses the window.

# Please report bugs/feedback to: Anabelle Myers A02369941@aggies.usu.edu


# Anabelle G. Myers
# August 6, 2025

# Utah State University
#A02369941@aggies.usu.edu
####################

# Interpreters
import pandas as pd
import openpyxl
from openpyxl.worksheet.table import Table, TableStyleInfo

year = int(input("Enter the number of consecutive years over which to calculate the minimum of each ensemble: "))

# Input
excel_path = 'ImmersiveModelLakeMead/HydrologyScenarios.xlsx'  # Path to HydrologyScenarios.xlsx
sheet_names = pd.ExcelFile(excel_path).sheet_names  # Variable for ease of access to all the sheets in HydrologyScenarios.xlsx.

# Specifies which sheets not to read.
excluded_sheets = ["ReadMe", "AvailableHydrologyScenarios", "ScenarioListForAnalysis", "AvailableMetrics", "MetricsForAnalysis", "Heatmap", "Hist"]

# Empty list to collect the overall minimum of each ensemble calculated from the for loops.
all_results = []

count_ensembles = 0
all_traces = []
total_traces = 0

# Assigns ensemble_input to each sheet individually for each time the code is looped
for ensemble_input in sheet_names:  # Iterates through ensembles
    if ensemble_input in excluded_sheets:  # Skips over sheets listed in excluded_sheets
        continue

    # Reads and converts values in ensembles to numeric values
    ensemble = pd.read_excel(excel_path, sheet_name=ensemble_input)  # Reads and skips ensemble if in excluded list
    ensemble = ensemble.apply(pd.to_numeric, errors='coerce')  # Converts to a DataFrame

    # Initialize variables to find and store minimum years
    overall_min = float('inf')
    overall_trace = None
    overall_pos = None

    count_traces = 0

    # Searches for the overall minimum sum of consecutive years
    for trace in ensemble.columns[1:]:  # Iterates through each trace in the ensemble
        series = ensemble[trace]  # Isolates one column to be iterated through
        rollingSum = series.rolling(window=year).sum()  # Calculates sum of a rolling window
        valid = rollingSum.dropna()  # Drops NaN values to calculate only full windows

        if valid.empty:
            continue

        end_idx = int(valid.idxmin())  # Finds position of minimum rolling window
        minimum = valid.min()  # Finds the years of the rolling sum
        start_idx = end_idx - (year - 1)  # Finds the position of the start of the window

        # Stores the most minimum sum information until an even smaller sum occurs
        if minimum < overall_min:
            overall_min = minimum
            overall_trace = trace
            overall_start = start_idx

        count_traces += 1

    all_traces.append(count_traces)
    total_traces += count_traces
    count_ensembles += 1

    if overall_trace is not None:
        window = ensemble[overall_trace].iloc[overall_start : overall_start + year].reset_index(drop=True)  # Extracts years from the rolling sum window
        average = round(overall_min / year, 1)

        # Stores results into variables
        result = {
            'Ensemble': ensemble_input,
            'Trace': overall_trace,
            'Start Row': overall_start + 1,
            'Average': average
        }

        for i in range(len(window)):  # Assigns results to correct title to store into Excel columns
            result[f'Year{i + 1}'] = round(window.iloc[i], 1)

        all_results.append(result)  # Adds results to the list of all results


# Convert to DataFrame
df = pd.DataFrame(all_results)

# Write results to a single-sheet Excel file with a table
output_path = '/Users/anabelle/Documents/GitHub/ImmersiveModelLakeMead/MinimumHydrologyScenarios/MinimumHydrologyResults.xlsx'
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Ensemble Minimums', index=False)
    workbook = writer.book
    worksheet = writer.sheets['Ensemble Minimums']

    end_col = chr(65 + len(df.columns) - 1)
    end_row = len(df) + 1
    table_range = f"A1:{end_col}{end_row}"

    table = Table(displayName="MinPerEnsemble", ref=table_range)
    style = TableStyleInfo(name="TableStyleMedium9", showRowStripes=True)
    table.tableStyleInfo = style
    worksheet.add_table(table)

# Displays path to output
print(f"\nResults saved to:\n{output_path}")

print("\nThe code iterated through", count_ensembles, "ensembles and", sum(all_traces), "traces.")
