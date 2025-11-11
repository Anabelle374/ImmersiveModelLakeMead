# ImmersiveModelSessionData

This code iterates through an excel sheet of compacted data from multiple different immersive model for Lake Mead sessions and creates graphs that show the differences and successess of each session.

## Description of Contents
1. **LowStorageBlogGraph.xlsx** - Excel sheet that is the input for both python scripts. It contains condensed data from immersive model for Lake Mead sessions.
1. **SessionDotPlot.py** - This python script reads through the input and produces a dot plot representation of Lake Mead Storage to protection Ratio vs Chosen Protection Elevation.
1. **SessionDotPlot.png** - This graph shows when collaborators in sessions succeeded and did not succeed in stabilizing Lake Mead's storage and elevation.
2. **TimeSeries.py** - This python script reads through the input and produces a line graph.
1. **TimeSeries.png** - This line graph shows a time series of one immersive model session of Storage and elevation vs years.

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



