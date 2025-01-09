# DataIku-Running-Notebook-List
## How to list all Dataiku notebook which is running but not modified or edited in last 7 days in Dataiku 

#### To list all notebooks that are running and have not been modified or edited in the last 7 days in Dataiku, you can follow these steps using the Dataiku API and some Python code.

#### Access Dataiku API: You can use the Dataiku DSS Python API to interact with the Dataiku instance and retrieve information about Jupyter notebooks.

#### Python Code: Use the code below to get the list of running notebooks and check their last modification date.

## Steps Explained:
#### 1- Get DSS Client: Connect to the Dataiku DSS instance using the API.
#### 2- List Running Notebooks: Retrieve all running Jupyter notebooks for the specified project.
#### 3- Check Modification Date: Compare the last modification date with the current date minus 7 days.
#### 4- Filter Notebooks: Only include notebooks that are running and haven't been modified in the last 7 days.
#### 5- Make sure to replace "your_project_key" with the actual project key in your Dataiku instance.

## Pre-requisites:
Dataiku DSS must have API access enabled.
You need appropriate permissions to access the project and notebooks in Dataiku.

### Automating the process of listing Jupyter notebooks in Dataiku that are running but haven't been modified in the last 7 days provides several benefits:

#### 1. Time Savings
###### -- Manual Work Reduction: It eliminates the need to manually check each notebook's status and modification date, saving significant time, especially in large projects with many notebooks.

#### 2. Resource Optimization
###### -- Efficient Resource Use: Identifying and stopping idle notebooks prevents unnecessary resource consumption, ensuring that system resources (CPU, memory) are used efficiently.
###### -- Cost Reduction: By optimizing resource usage, you can potentially reduce costs, especially in cloud environments where resources are billed based on usage.

#### 3. Improved System Performance
###### -- Performance Boost: Stopping unused running notebooks can free up system resources, enhancing the performance of the Dataiku instance for other active tasks.

#### 4. Enhanced Project Management
###### -- Automated Monitoring: Regularly running this script can help maintain a clean and organized environment by keeping track of unused resources.
###### -- Compliance and Governance: Ensures adherence to organizational policies regarding resource usage and project maintenance.

#### 5. Reduced Error Potential

###### -- Consistent Results: Automation reduces the likelihood of human error in tracking notebook statuses, leading to more reliable outcomes.

#### -- 6. Customization and Scalability
###### -- Adaptability: The script can be customized to include additional criteria or to handle other tasks related to notebook management.
###### -- Scalable Solution: The script can easily scale with the number of projects and notebooks, making it suitable for large environments.

#### 7. Proactive Maintenance
###### -- Preventive Action: It allows teams to proactively manage running notebooks, reducing the risk of overloading the system or facing unexpected resource shortages.
###### -- Implementing such a script is an excellent way to enhance operational efficiency and maintain a robust data science environment.
