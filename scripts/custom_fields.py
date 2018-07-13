from config import projectsConfig
from fetch_projects import fetchAllProjects
from fetch_projects import writeProjectToJson
import json

data = fetchAllProjects(projectsConfig)
print(data)
