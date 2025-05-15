print("")
ensemble_input = input("Enter ensemble name: ")
print("")
from urllib.request import install_opener
import pandas as pd
import openpyxl
#import numpy as np

ensemble = pd.read_excel('/Users/anabelle/Documents/GitHub/ImmersiveModelLakeMead/HydrologyScenarios.xlsx' , sheet_name = ensemble_input) # Reads from specified ensemble.
# Display data
#print(ensemble)

# Three Consecutive Minimum Hydrologic Flows
for y in ensemble.columns[1:]: # Iterates through each Trace

    TraceY = ensemble[y] # Simplify to call Trace1 easier.
    minList = [] # Creates a list to store and work with minimum consecutive sums of Trace1.

    for x in range(0,len(TraceY)-2): # For loop to iterate each value in Trace1
        result = TraceY[x] + TraceY[x+1] + TraceY[x+2] # Sums three consecutive values for each value.
        minList.append(result) # Adds the summation to minList
        #print(result) # Shows the result of the summations.
    print(y)
    minimumSum = min(minList) # Finds the minimum summation.

    print('Minimum Summation Value of Trace:', round(minimumSum,1))

    minPosition = minList.index(minimumSum) # Finds the position of the minimum summation.
    print('Position of Minimum Value of Trace:',minPosition + 1)

    print('Three consecutive minimums of Trace:',round(TraceY[minPosition],1), round(TraceY[minPosition+1],1), round(TraceY[minPosition+2],1),'\n')
    #(above) Finds and prints the three consecutive minimum values based on the minimum summation.

# Creating initial conditions as placeholders
overall_min = float('inf')
overall_trace = ""
overall_index = -1
overall_values = ()

for y in ensemble.columns[1:]: # Iterates through traces
    TraceY = ensemble[y]
    minList = []
    for x in range(0, len(TraceY) - 2): # Iterates through each row
        result = TraceY[x] + TraceY[x + 1] + TraceY[x + 2] # Calculates minimum sum
        minList.append(result)
    minimumSum = min(minList)
    if minimumSum < overall_min: # If it is minimum, values are stored
        overall_min = minimumSum
        overall_trace = y
        overall_index = minList.index(minimumSum)
        overall_values = (TraceY[overall_index], TraceY[overall_index + 1], TraceY[overall_index + 2]) # Stores the values in order.

print("====== OVERALL MINIMUM ACROSS ENSEMBLE ======")
print("Trace with Overall Minimum:", overall_trace)
print("Row:", overall_index + 1)
print("Three Consecutive Minimum Values:",round(overall_values[0], 1), round(overall_values[1], 1), round(overall_values[2], 1))


