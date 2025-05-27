# ImmersiveModelLakeMead
This code identifies three and five lowest consecutive values within each trace and ensemble from HydrologyScenarios (Salehabadi, 2023). The results of this code was used to create scenarios of extreme low inflow to Lake Mead.
## Input
This excel workbook, created by Homa Salehabadi using different hydrologic scenarios, shows inflow values to Lee's Ferry for differing hydrologic scenarios. Values from these ensembles and traces were used as input to the ImmersiveModelLakeMead code.
## Output
Two different excel workbooks were written with the results from two slightly different python code. The output shows three or five overall consecutive minimum values from each ensemble from the input.
## Code
The ImmersiveModelLakeMead code is run in this order:
First, this code takes the specified input stated above and reads the input. Then sheets that do not contain hydrologic scenarios are specified to exclude. Next, an empty list stores the overall minimum of each ensemble of the upcoming loop. A for loop assigns an ensemble sheet to use for each loop. The ensemble is met with a condition to ensure the ensemble is not listed as an excluded ensemble. Next, the ensemble is converted to numeric values. Initial variables are created, so values found can be stored in these variables. Then, each value in each trace in the ensemble is iterated through to find the three or five most minimum consecutive values. The minimum sum is found, then the overall minimum sum of the traces in the ensemble is found and stored. Each value in the list and the start position is found. The values are then stored in varibales. The results are then exported and written into excel in a table.
