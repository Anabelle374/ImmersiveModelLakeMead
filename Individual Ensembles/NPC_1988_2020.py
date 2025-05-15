print("")
print('Ensemble: NPC_1988_2020\n')
from urllib.request import install_opener
import pandas as pd
import openpyxl
#import numpy as np

ensemble = pd.read_excel('/Users/anabelle/Documents/HydrologicScenarios/HydrologyScenarios.xlsx' , sheet_name = 'NPC_1988_2020') # For Mac
#ensemble = pd.read_excel('C:/Users/A02369941/Downloads/HydrologyScenarios.xlsx', sheet_name = 'NPC_1988_2020') # For HP
# Display data
#print(ensemble)

# Three Consecutive Minimum Hydrologic Flows
for y in ensemble.columns[1:]: # Iterates through each Trace

    TraceY = ensemble[y] # Simplify to call Trace1 easier.
    minList = [] # Creates a list to store and work with minimum consecutive sums of Trace1

    for x in range(0,len(TraceY)-2): # For loop to iterate each value in Trace1
        result = TraceY[x] + TraceY[x+1] + TraceY[x+2] # Sums three consecutive values for each value.
        minList.append(result) # Adds the summation to minList
        #print(result) # Shows the result of the summations.
    print(y)
    minimumSum = min(minList) # Finds the minimum summation.
    print('Minimum Summation Value of Trace:', minimumSum)

    minPosition = minList.index(minimumSum) # Finds the position of the minimum summation.
    print('Position of Minimum Value of Trace:',minPosition + 1)

    print('Three consecutive minimums of Trace:',TraceY[minPosition], TraceY[minPosition+1], TraceY[minPosition+2],'\n')
    #(above) Finds and prints the three consecutive minimum values based on the minimum summation.