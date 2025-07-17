# MinimumFiveHydrologyScenariosCode.py
#
#################

# Purpose
# This code iterates through all ensembles and traces in HydrologyScenarios.xlsx
#   by Homa Salehabadi (2023). During the iterations, the code finds the most minimum
#   five consecutive values of each ensemble.

# Please report bugs/feedback to: Anabelle Myers A02369941@aggies.usu.edu

# Updated May 21, 2025 to iterate through all ensembles.

# Anabelle G. Myers
# June 24, 2025

# Utah State University
#A02369941@aggies.usu.edu
####################

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

    # Iterates through each trace and stores found values
    for y in ensemble.columns[1:]: # Iterates through each trace
        TraceY = ensemble[y] # Creates a variable to call traces easier
        failList = [] # Empty list to store values

        for x in range(0, len(TraceY) - 9): # Iterates through each trace stopping 9 rows from the bottom
            result = (TraceY[x] + TraceY[x + 1] + TraceY[x + 2] + TraceY[x + 3] + TraceY[x + 4]
                + TraceY[x + 5] + TraceY[x + 6] + TraceY[x + 7] + TraceY[x + 8] + TraceY[x + 9])
            failList.append((result, x)) # Stores the sum and position

        trace_ten_sum, trace_fail_pos = min(failList, key=lambda t: t[0]) # Finds minimum sum, not minimum position

        if trace_ten_sum < 75: # Finds the overall minimum of the ensemble and position of it
            first = TraceY[trace_fail_pos]
            second = TraceY[trace_fail_pos + 1]
            third = TraceY[trace_fail_pos + 2]
            fourth = TraceY[trace_fail_pos + 3]
            fifth = TraceY[trace_fail_pos + 4]
            sixth = TraceY[trace_fail_pos + 5]
            seventh = TraceY[trace_fail_pos + 6]
            eighth = TraceY[trace_fail_pos + 7]
            ninth = TraceY[trace_fail_pos + 8]
            tenth = TraceY[trace_fail_pos + 9]
    # Adds values into variables
            sumTen = round((first + second + third + fourth + fifth + sixth + seventh + eighth + ninth + tenth), 1)
            all_results.append({
                'Ensemble': ensemble_input,
                'Trace': y,
                'Start Row': trace_fail_pos + 1,
                'First': round(first, 1),
                'Second': round(second, 1),
                'Third': round(third, 1),
                'Fourth': round(fourth, 1),
                'Fifth': round(fifth, 1),
                'Sixth': round(sixth, 1),
                'Seventh': round(seventh, 1),
                'Eighth': round(eighth, 1),
                'Ninth': round(ninth, 1),
                'Tenth': round(tenth, 1),
                'Sum': sumTen
            })

# Convert to DataFrame
df = pd.DataFrame(all_results)

# Write results to a single-sheet Excel file with a table
output_path = '/Users/anabelle/Documents/GitHub/ImmersiveModelLakeMead/10YearsCompactNotMet/10YearsCompactNotMetResults.xlsx'
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Ensemble Fails', index=False)
    workbook = writer.book
    worksheet = writer.sheets['Ensemble Fails']

    # Define Excel table
    end_col = chr(65 + len(df.columns) - 1)
    end_row = len(df) + 1
    table_range = f"A1:{end_col}{end_row}"

    table = Table(displayName="EnsembleFails", ref=table_range)
    style = TableStyleInfo(name="TableStyleMedium9", showRowStripes=True)
    table.tableStyleInfo = style
    worksheet.add_table(table)

print(f"\n Results saved to:\n{output_path}")
