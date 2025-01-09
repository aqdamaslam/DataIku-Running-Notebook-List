# DataIku-Running-Notebook-List
How to list all Dataiku notebook which is running but not modified or edited in last 7 days in Dataiku 

## Steps Explained:
###### 1- Get DSS Client: Connect to the Dataiku DSS instance using the API.
###### 2- List Running Notebooks: Retrieve all running Jupyter notebooks for the specified project.
###### 3- Check Modification Date: Compare the last modification date with the current date minus 7 days.
###### 4- Filter Notebooks: Only include notebooks that are running and haven't been modified in the last 7 days.
###### 5- Make sure to replace "your_project_key" with the actual project key in your Dataiku instance.

## Pre-requisites:
Dataiku DSS must have API access enabled.
You need appropriate permissions to access the project and notebooks in Dataiku.
