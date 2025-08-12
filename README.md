# ImmersiveModelLakeMead
The purpose of this python code is to find the lowest flow rate sum of consecutive years using data from the Excel workbook 'HydrologyScenarios' (Salehabadi, 2023). The results of this code are used to create scenarios of extreme low inflow to Lake Mead.
## Description of Contents
### Input (HydrologyScenarios.xlsx)
The Excel workbook 'HydrologyScenarios' (Salehabadi, 2023) shows inflow values to Lee's Ferry for differing hydrologic scenarios. Values from these ensembles and traces were used as input to the MinimumHydrologyScenarios.py code.
### Code (MinimumHydrologyScenarios / MinimumHydrologyScenarios.py
First the code takes user input to define the number of consecutive years to use for calculations. Then the window and flow rates of the minimum consecutive years are found for every trace in every ensemble. The ensembles with 'ISM' in the title only iterates through one trace. This trace is duplicated and vertically stacked then the minimum consecutive years window sum is calculated. The ensemble title, trace title, starting position, and average for the windows are stored and outputted to Excel. In-depth descriptions can be found in the comments in the script.
Notes: Only one trace in the 'ISM' ensembles are calculated because the 'ISM' traces have the same data in the same order, but offset by one cell. Doing this rids the results of redundant data. 
### Output (MinimumHydrologyScenarios / Results/ 'X'yearsMinimumHydrologyResults.xlsx)
The results for the minimum consecutive years are stored in Excel files in the 'Results' folder located in the 'MinimumHydrologyScenarios' folder. 'X' represents the number of consecutive years the user chooses. The results only are overwritten when the user chooses the same number.
### Old
The HydrologyScenarios.xlsx is the input for all three codes. A furthur description can be found below in the Input section. The folder "ThreeMinimumHydrologyScenarios" contains the code used to find the the three most minimum consecutive values in each ensemble in the input. The results of this code can be found in the same folder. Two near identical folders, "FourMinimumHydrologyScenarios" and "FiveMinimumHydrologyScenarios" include similar contents. "FourMinimumHydrologyScenarios" contains code and results for four most minimum consecutive values in each ensemble and "FiveMinimumHydrologyScenarios" contains code and results for five most minimum cosecutive values in each ensemble. The folder "10YearsCompactNotMet" contains code used to find ten cosecutive values that sums to less than 75 maf. 
## Software Needed
The software applications needed to reproduce these results are Microsoft Excel, and PyCharm.
## Reproducibility
To reproduce the results for MinimumHydrologyScenarios.py, follow the directions below.
1. Install Microsoft Excel.
   a. Search 'https://excel.cloud.microsoft/' in a search engine.
   b. Sign in or create an account.
   c. If Excel is not purchased, follow Microsofts provided instructions to purchase Excel.
   d. Open Excel and sign in.
2. Install Python.
   a. Search 'https://www.python.org/' in a search engine.
   b. Scroll down to the 'Download' section and click the latest Python version.
   c. Scroll down to the 'Files' section.
   d. Read the 'Description' column in the table, choose the best description for the device in use, then follow the row to the left to the 'Version' column and click on the installer option.
   e. Go to the device's downloads and find the installer chosen in step 2d.
   f. Click on the installer and follow the directions.
3. Install Pycharm
   a. Search 'https://www.jetbrains.com/pycharm/' in a search engine.
   b. Select 'Download'.
   c. Ensure the .dmg is correct for the device in use, then select 'Download'.
   d. Go to the device's downloads and find the installer chosen in step 3c.
   e. Select the installer and follow the directions.
4. Download this repository.
   a. Scroll to the top of this page and select 'Code'.
   b. Select 'Download ZIP'.
   c. Go to the device's downloads and select 'ImmersiveModelLakeMead-main'. This will unzip the file.
5. Open the Python script.
   a. In the 'ImmersiveModelLakeMead-main' file, select the folder 'MinimumHydrologyScenarios'.
   b. Open 'MinimumHydrologyScenarios.py' with Pycharm.
   c. Follow the directions.
   d. Select 'MinimumHydrologyScenarios.py'.
6. Select a Python interpreter.
7. Open settings in Pycharm.
   a. Select 'Project:MinimumHydrologyScenarios', 'Python Interpreter', then "+".
   b. In the search bar, type, 'pandas'. Select 'pandas' then 'Install Package'.
   c. Repeat step 5b. with 'openpyxl' instead of 'pandas'.
8. Click the green play arrow at the top of the page.
9. Follow the directions at the bottom of the page.
10. The results will be stored in a created excel file in the 'Results' folder in the 'MinimumHydrologySenarios' folder.
## Contact Information
### Authors
#### Anabelle Myers. Email: A02369941@aggies.usu.edu.
#### David E. Rosenberg. Email: david.rosenberg@usu.edu
