import dataiku
from datetime import datetime, timedelta

# Get the DSS client
client = dataiku.api_client()

# Define the project
project_key = "your_project_key"
project = client.get_project(project_key)

# Get all running notebooks
running_notebooks = project.list_jupyter_notebooks()

# Define the time limit (7 days ago)
time_limit = datetime.now() - timedelta(days=7)

# List all notebooks not modified in the last 7 days
notebooks_not_modified = []
for notebook in running_notebooks:
    last_modified = datetime.fromisoformat(notebook['lastModified'])
    
    if last_modified < time_limit and notebook['state'] == 'RUNNING':
        notebooks_not_modified.append(notebook)

# Print the notebooks
for nb in notebooks_not_modified:
    print(f"Notebook {nb['name']} is running and was last modified on {nb['lastModified']}")
