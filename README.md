# ImmersiveModelLakeMead
This code identifies three, four, and five lowest consecutive annual scenarios of natural inflow to Lake Powell. The code also identifies when the rolling sum of ten consecutive values sums to less than 75 million acre-feet (maf). These values are pulled out from the traces and ensembles in the HydrologyScenarios.xlsx file (Salehabadi, 2023). The results of this code are used to create scenarios of extreme low inflow to Lake Mead.
## Description of Contents
The HydrologyScenarios.xlsx is the input for all three codes. A furthur description can be found below in the Input section. The folder "ThreeMinimumHydrologyScenarios" contains the code used to find the the three most minimum consecutive values in each ensemble in the input. The results of this code can be found in the same folder. Two near identical folders, "FourMinimumHydrologyScenarios" and "FiveMinimumHydrologyScenarios" include similar contents. "FourMinimumHydrologyScenarios" contains code and results for four most minimum consecutive values in each ensemble and "FiveMinimumHydrologyScenarios" contains code and results for five most minimum cosecutive values in each ensemble. The folder "10YearsCompactNotMet" contains code used to find ten cosecutive values that sums to less than 75 maf. 
## Input
This excel workbook, created by Homa Salehabadi using different hydrologic scenarios, shows inflow values to Lee's Ferry for differing hydrologic scenarios. Values from these ensembles and traces were used as input to the ImmersiveModelLakeMead code.
## Software Needed
The software applications needed to reproduce these results are Microsoft Excel, and PyCharm.
## Output
Four different excel workbooks were written with the results from three slightly different python code. The output shows three, four, or five overall consecutive minimum values from each ensemble from the input. The fourth output shows all instances (no more than one per trace) ten consecutive values that sums to less than 75 maf. These results are written from the Python code into Excel workbooks.
## Reproducibility
To reproduce the results for MinimumThreeHydrologyScenariosCode, follow the directions below.
1. Install Microsoft Excel and Pycharm.
2. Download HydrologicScenarios.xlsx
3. Open MinimumThreeHydrologyScenariosCode with Pycharm.
4. Select a Python interpreter.
5. Open settings in Pycharm.
   a. Select "Project:MinimumThreeHydrologyScenariosCode", "Python Interpreter", then "+".
   b. In the search bar, type, "pandas". Select "pandas" then "Install Package".
   c. Repeat step 5b. with "openpyxl" instead of "pandas".
6. Change the value for "excel_path" to the path were HydrologyScenarios.xlsx is stored. Ensure all back slashes are changed to forward slashes and that 'C:' is deleted.
7. Change the value for "output_path" to desired path to an excel book. Ensure all back slashes are changed to forward slashes and that 'C:' is deleted.
8. Click the play arrow to run the code.
9. The results will be stored in a created excel file in the output path specified above.
10. To reproduce results for MinimumFourHydrologyScenariosCode and MinimumFiveHydrologyScenariosCode, follow steps follow steps 1-9, but use the desired code in place of MinimumThreeHydrologyScenariosCode.
## Contact Information
### Authors
#### Anabelle Myers. Email: A02369941@aggies.usu.edu.
#### David E. Rosenberg. Email: david.rosenberg@usu.edu
