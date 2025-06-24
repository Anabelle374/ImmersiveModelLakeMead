# MinimumThreeHydrologyScenariosCode.py
#
#################

# Please report bugs/feedback to: Anabelle Myers A02369941@aggies.usu.edu

# Updated May 21, 2025 to iterate through all ensembles.

# Anabelle G. Myers
# June 24, 2025

# Utah State University
#A02369941@aggies.usu.edu
####################

# Interpreters
import pandas as pd
import openpyxl
from openpyxl.worksheet.table import Table, TableStyleInfo

# Input
excel_path = '/Users/anabelle/Documents/GitHub/ImmersiveModelLakeMead/HydrologyScenarios.xlsx' # Path to HydrologyScenarios.xlsx
sheet_names = pd.ExcelFile(excel_path).sheet_names # Variable for ease of access to all the sheets in HydrologyScenarios.xlsx.

# Specifies which sheets not to read.
excluded_sheets = ["ReadMe", "AvailableHydrologyScenarios", "ScenarioListForAnalysis", "AvailableMetrics", "MetricsForAnalysis", "HeatMap", "Hist"]

# Empty list to collect the overall minimum of each ensemble calculated from the for loops.
all_results = []

# Assigns ensemble_input to each sheet individually for each time the code is looped
for ensemble_input in sheet_names:
    if ensemble_input in excluded_sheets: # Skips over sheets listed in excluded_sheets
        continue

    # Reads and converts values in ensembles to numeric values
    ensemble = pd.read_excel(excel_path, sheet_name=ensemble_input)
    ensemble = ensemble.apply(pd.to_numeric, errors='coerce')

    # Initialize variables to find and store minimum values
    overall_min = float('inf')
    overall_trace = ""
    overall_pos = -1
    first = second = third = None

    # Searches for the overall minimum sum of three consecutive values
    for y in ensemble.columns[1:]: # Iterates through each trace in the ensemble
        TraceY = ensemble[y]
        minList = [] # Empty list to store values calculated in the for loop below.

        for x in range(0, len(TraceY) - 2): # Iterates through each row in a trace stopping 2 rows from the bottom
            result = TraceY[x] + TraceY[x + 1] + TraceY[x + 2]
            minList.append((result, x)) # Stores the sum of every three rows.

        trace_min_sum, trace_min_pos = min(minList, key=lambda t: t[0]) # Finds a grouping of three that has the smallest sum and unpacks the group.

        # Finds the overall minimum of the ensemble and position of it
        if trace_min_sum < overall_min:
            overall_min = trace_min_sum
            overall_trace = y
            overall_pos = trace_min_pos
            first = TraceY[trace_min_pos]
            second = TraceY[trace_min_pos + 1]
            third = TraceY[trace_min_pos + 2]

    # Stores values into variables and rounds values
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

    # Define Excel table boundaries
    end_col = chr(65 + len(df.columns) - 1)
    end_row = len(df) + 1
    table_range = f"A1:{end_col}{end_row}"

    #Stylizes variables
    table = Table(displayName="MinPerEnsemble", ref=table_range)
    style = TableStyleInfo(name="TableStyleMedium9", showRowStripes=True)
    table.tableStyleInfo = style
    worksheet.add_table(table)

# Displays path to output
print(f"\n Results saved to:\n{output_path}")
