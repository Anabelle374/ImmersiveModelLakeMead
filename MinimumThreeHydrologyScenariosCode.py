import pandas as pd
import openpyxl
from openpyxl.worksheet.table import Table, TableStyleInfo

# Input
excel_path = '/Users/anabelle/Documents/GitHub/ImmersiveModelLakeMead/HydrologyScenarios.xlsx'
sheet_names = pd.ExcelFile(excel_path).sheet_names

# Sheets for code to skip reading
excluded_sheets = [
    "ReadMe", "AvailableHydrologyScenarios", "ScenarioListForAnalysis",
    "AvailableMetrics", "MetricsForAnalysis", "HeatMap", "Hist"
]

# Empty list to collect the overall minimum of each ensemble
all_results = []

# Assigns ensemble_input to each sheet individually for each time the code is looped
for ensemble_input in sheet_names:
    if ensemble_input in excluded_sheets: # Skips sheets listed in excluded_sheets
        continue

    # Reads and converts values in ensembles to numeric values
    ensemble = pd.read_excel(excel_path, sheet_name=ensemble_input)
    ensemble = ensemble.apply(pd.to_numeric, errors='coerce')

    # Initialize variables to find and store minimum values
    overall_min = float('inf')
    overall_trace = ""
    overall_pos = -1
    first = second = third = None

    # Search for the overall minimum sum of three consecutive values
    for y in ensemble.columns[1:]: # Iterates through each trace
        TraceY = ensemble[y]
        minList = [] # Empty list to store values

        for x in range(0, len(TraceY) - 2): # Iterates through each trace stopping 2 rows from the bottom
            result = TraceY[x] + TraceY[x + 1] + TraceY[x + 2]
            minList.append((result, x)) # Stores the sum and position

        trace_min_sum, trace_min_pos = min(minList, key=lambda t: t[0]) # Finds minimum sum, not minimum position

        if trace_min_sum < overall_min: # Finds the overall minimum of the ensemble and position of it
            overall_min = trace_min_sum
            overall_trace = y
            overall_pos = trace_min_pos
            first = TraceY[trace_min_pos]
            second = TraceY[trace_min_pos + 1]
            third = TraceY[trace_min_pos + 2]

    # Adds values into variables
    if overall_trace:
        average = round((first + second + third) / 3, 1)
        all_results.append({
            'Ensemble': ensemble_input,
            'Trace': overall_trace,
            'Start Row': overall_pos + 1,
            'First': round(first, 1),
            'Second': round(second, 1),
            'Third': round(third, 1),
            'Average': average
        })

# Convert to DataFrame
df = pd.DataFrame(all_results)

# Write results to a single-sheet Excel file with a table
output_path = '/Users/anabelle/Documents/GitHub/ImmersiveModelLakeMead/MinimumThreeHydrologyResults.xlsx'
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Ensemble Minimums', index=False)
    workbook = writer.book
    worksheet = writer.sheets['Ensemble Minimums']

    # Define Excel table
    end_col = chr(65 + len(df.columns) - 1)
    end_row = len(df) + 1
    table_range = f"A1:{end_col}{end_row}"

    table = Table(displayName="MinPerEnsemble", ref=table_range)
    style = TableStyleInfo(name="TableStyleMedium9", showRowStripes=True)
    table.tableStyleInfo = style
    worksheet.add_table(table)

print(f"\n Results saved to:\n{output_path}")
