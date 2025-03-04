import pandas as pd
# Add Comment
# David added comment
# Read Excel file sheet: ISM_StressTest
stress_test = pd.read_excel('C:/Users/A02369941/Downloads/HydrologyScenarios.xlsx', sheet_name = 'ISM_StressTest')
# Display data
#print(stress_test)

# Minimum flow per Trace
min_flow_rates = stress_test['Trace1'].min()
print("Minimum Flow Rates per Trace",'\n', min_flow_rates)

# Three smallest values:
three_min = stress_test['Trace1'].nsmallest(3)
print("Three Most Minimum Flow Rates per Trace:","\n", three_min)

# Average flow per Trace
avg_flow_rates = stress_test['Trace1'].mean()
#Display average flow per Trace
print("Average Flow Rates per Trace",'\n', avg_flow_rates)




