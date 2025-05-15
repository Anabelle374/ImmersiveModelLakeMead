print('Ensemble: ISM_StressTest')
from urllib.request import install_opener
import pandas as pd
import openpyxl
#import numpy as np

#print(openpyxl.__version__)

# Read Excel file sheet: ISM_StressTest
ensemble = pd.read_excel('/Users/anabelle/Documents/HydrologicScenarios/HydrologyScenarios.xlsx' , sheet_name = 'ISM_StressTest') # For Mac
#ensemble = pd.read_excel('C:/Users/A02369941/Downloads/HydrologyScenarios.xlsx', sheet_name = 'ISM_StressTest') # For HP
# Display data
#print(ensemble)

# Three Consecutive Minimum Hydrologic Flows
Trace1 = ensemble['Trace1'] # Simplify to call Trace1 easier.

minList = [] # Creates a list to store and work with minimum consecutive sums of Trace1

for x in range(0,len(Trace1)-2): # For loop to iterate each value in Trace1
    result = Trace1[x] + Trace1[x+1] + Trace1[x+2] # Sums three consecutive values for each value.
    minList.append(result) # Adds the summation to minList
    #print(result) # Shows the result of the summations.

minimumSum = min(minList) # Finds the minimum summation.
print('Minimum Summation Value:', minimumSum)

minPosition = minList.index(minimumSum) # Finds the position of the minimum summation.
print('Position of Minimum Value:',minPosition + 1)

print('Three consecutive minimums:',Trace1[minPosition], Trace1[minPosition+1], Trace1[minPosition+2])
# (above) Finds and prints the three consecutive minimum values based on the minimum summation.


# Minimum flow per Trace
#min_flow_rates = ensemble['Trace1'].min()
###print("Minimum Flow Rates per Trace",'\n', min_flow_rates)

# Three smallest values:
#three_min = ensemble['Trace1'].nsmallest(3)
###print("Three Most Minimum Flow Rates per Trace:","\n", three_min)

# Average flow per Trace
#avg_flow_rates = ensemble['Trace1'].mean()
#Display average flow per Trace
###print("Average Flow Rates per Trace",'\n', avg_flow_rates)








