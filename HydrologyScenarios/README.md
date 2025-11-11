# Supporting Extreme Low Reservoir Inflows for Immersive Model for Lake Mead

This code identifies periods of three-, four-, and 10-year extreme low natural flow at Lee Ferry. 
The code also identifies when the rolling sum of ten consecutive values sums to less than 75 million acre-feet (maf).
These values are pulled out from the traces and ensembles in the HydrologyScenarios.xlsx file (Salehabadi, 2024). There are 22 ensembles and 1750 traces in this data set.
The results of this code are used to create scenarios of extreme low inflow to Lake Mead used for Immersive Modeling.

## Description of Contents
1. **HydrologyScenarios.xlsx** is the input for all three codes. This workbook comes from Salehabadi et al, 2024). A furthur description can be found below in the Input section.
1. **MinimumHydrologyScenarios** - Folder  contains the Python code (MinimumHydrologyScenarios.py) used to find 3-, 4-, and 10-year minimum flows.
1. **Old** - Folder with older versions of Python code.
1. **MinimumHydrologyScenarios/Results** - Subfolder that contains results in Excel files, e.g., **3yearsMinimumHydrologyResults.xlsx**.

### Code (MinimumHydrologyScenarios / MinimumHydrologyScenarios.py)
First the code takes user input to define the number of consecutive years to use for calculations. Then the window and flow rates of the minimum consecutive years are found for every trace in every ensemble. The ensembles with 'ISM' in the title only iterates through one trace. This trace is duplicated and vertically stacked then the minimum consecutive years window sum is calculated. The ensemble title, trace title, starting position, and average for the windows are stored and outputted to Excel. In-depth descriptions can be found in the comments in the script.
Notes: Only one trace in the 'ISM' ensembles are calculated because the 'ISM' traces have the same data in the same order, but offset by one cell. Doing this rids the results of redundant data. 

### Output (MinimumHydrologyScenarios / Results / 'X'yearsMinimumHydrologyResults.xlsx)
The results for the minimum consecutive years are stored in Excel files in the 'Results' folder located in the 'MinimumHydrologyScenarios' folder. 'X' represents the number of consecutive years the user chooses. The results only are overwritten when the user chooses the same number.

## Directions to Reproduce Results
### Software Needed
The software applications needed to reproduce these results are Microsoft Excel, and PyCharm.
### Reproducibility
To reproduce the results for MinimumHydrologyScenarios.py, follow the directions below.
1. Install Microsoft Excel.
- Search 'https://excel.cloud.microsoft/' in a search engine.
- Sign in or create an account.
- If Excel is not purchased, follow Microsofts provided instructions to purchase Excel.
- Open Excel and sign in.
2. Install Python.
- Search 'https://www.python.org/' in a search engine.
- Scroll down to the 'Download' section and click the latest Python version.
- Scroll down to the 'Files' section.
- Read the 'Description' column in the table, choose the best description for the device in use, then follow the row to the left to the 'Version' column and click on the installer option.
- Go to the device's downloads and find the installer chosen in step 2d.
- Click on the installer and follow the directions.
3. Install Pycharm
- Search 'https://www.jetbrains.com/pycharm/' in a search engine.
- Select 'Download'.
- Ensure the .dmg is correct for the device in use, then select 'Download'.
- Go to the device's downloads and find the installer chosen in step 3c.
- Select the installer and follow the directions.
4. Download this repository.
- Scroll to the top of this page and select 'Code'.
- Select 'Download ZIP'.
- Go to the device's downloads and select 'ImmersiveModelLakeMead-main'. This will unzip the file.
5. Open the Python script.
- In the 'ImmersiveModelLakeMead-main' file, select the folder 'MinimumHydrologyScenarios'.
- Open 'MinimumHydrologyScenarios.py' with Pycharm.
- Follow the directions.
- Select 'MinimumHydrologyScenarios.py'.
6. Select a Python interpreter.
7. Open settings in Pycharm.
- Select 'Project:MinimumHydrologyScenarios', 'Python Interpreter', then "+".
- In the search bar, type, 'pandas'. Select 'pandas' then 'Install Package'.
- Repeat step 5b. with 'openpyxl' instead of 'pandas'.
8. Click the green play arrow at the top of the page.
9. Follow the directions at the bottom of the page.
10. The results will be stored in a created excel file in the 'Results' folder in the 'MinimumHydrologySenarios' folder.


