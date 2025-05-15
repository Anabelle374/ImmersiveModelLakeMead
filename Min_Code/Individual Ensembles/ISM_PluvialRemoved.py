print('Ensemble: ISM_PluvialRemoved')
from urllib.request import install_opener
import pandas as pd
import openpyxl
#import numpy as np

#print(openpyxl.__version__)

# Read Excel file sheet: ISM_PluvialRemoved
ensemble = pd.read_excel('/Users/anabelle/Documents/HydrologicScenarios/HydrologyScenarios.xlsx' , sheet_name = 'ISM_PluvialRemoved') # For Mac
#ensemble = pd.read_excel('C:/Users/A02369941/Downloads/HydrologyScenarios.xlsx', sheet_name = 'ISM_PluvialRemoved') # For HP
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