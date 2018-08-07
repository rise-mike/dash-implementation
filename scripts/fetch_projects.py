import requests
import json
from config import projectsConfig

# FUNCTION DEFINITIONS
def fetchAllProjects(config):
    # Fetches from the supplied url using a specified token.
    url = config['domain'] + config['auth']
    zohoResponse = requests.get(url, params=config['params']).json()
    return zohoResponse

def writeProjectToJson(jsonObj, dest):
    # Accepts a JSON object, and dumps it into a specified destination file.
    print("Writing to ", dest)
    with open(dest, "w") as outfile:
        json.dump(jsonObj, outfile)

def parseAllProjects(rawProjects):
    # Takes in a dict of "rawProjects" from Zoho Projects, returns a list of parsed projects 
    allParsedProjects = []
    for aProject in rawProjects:
        currentProject = (singleProjectBuilder(aProject))
        allParsedProjects.append(currentProject)
    return allParsedProjects
    
def customIsolateSingle(customObj):
    # Takes an object of custom fields from Zoho, and flattens them
    returnCustom = {}
    for dicty in customObj:
        for key, value in dicty.items():
            returnCustom[key] = value

    return returnCustom

def progresCalc(open, closed):
    # Takes a number of open and closed tasks/milestones, and returns an int representing percentage of completion.
    if closed == 0:
        return 0
    else:
        total = open + closed
        return round(closed/total*100)

def singleProjectBuilder(rawProject):
    # Takes a single "rawProject" Zoho Project JSON object, returns a parsed object, "parsedProject". This project dict is used in all other scripts.
    projProgress = progresCalc(rawProject["milestone_count"]["open"], rawProject["milestone_count"]["closed"])
    parsedProject = {
            "name": rawProject["name"],  
            "projectId": rawProject["id"],
            "owner": rawProject["owner_name"],
            "startDate": rawProject["start_date"],
            "custom": customIsolateSingle(rawProject["custom_fields"]),
            "tasks_open": rawProject["milestone_count"]["open"],
            "tasks_closed": rawProject["milestone_count"]["closed"],
            "status": rawProject["status"],
            "progress" : str(projProgress),
            "progress_val" : projProgress
    }
    return parsedProject

# FUNCTION CALLS
# Fetch from API
zohoDump = fetchAllProjects(projectsConfig)

# Isolate and parse projects
isolatedProjects = zohoDump["projects"]
parsedProjects = parseAllProjects(isolatedProjects)

# Writes the raw and parsed output to json files in the 'data' folder
writeProjectToJson(isolatedProjects, "../data/rawprojects.json")
writeProjectToJson(parsedProjects, "../data/projects.json")