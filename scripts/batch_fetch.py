import requests
import json
from config import projectsConfig
import datetime

def fetchAllProjects(config):
    # Fetches from the supplied url using a specified token.
    url = config['domain'] + config['auth']
    zohoResponse = requests.get(url, params=config['params']).json()
    return zohoResponse

def parseAllProjects(rawProjects):
    # Takes in a dict of "rawProjects" from Zoho Projects, returns a list of parsed projects 
    allParsedProjects = []
    for aProject in rawProjects:
        currentProject = (singleProjectBuilder(aProject))
        allParsedProjects.append(currentProject)
    return allParsedProjects
    
def singleProjectBuilder(rawProject):
    # Takes a single "rawProject" Zoho Project JSON object, returns a parsed object, "parsedProject"
    projProgress = progresCalc(rawProject["task_count"]["open"], rawProject["task_count"]["closed"])
    parsedProject = {
            "name": rawProject["name"],  
            "projectId": rawProject["id"],
            "owner": rawProject["owner_name"],
            "startDate": rawProject["start_date"],
            "custom": customIsolateSingle(rawProject["custom_fields"]),
            "tasks_open": rawProject["task_count"]["open"],
            "tasks_closed": rawProject["task_count"]["closed"],
            "status": rawProject["status"],
            "progress" : str(projProgress),
            "progress_val" : projProgress
    }
    # customFieldParser(parsedProject["custom"])
    # return arrayProjectBuilder(parsedProject)

    return parsedProject

def arrayProjectBuilder(projy):
    arraydProj = [None, projy["name"], projy["owner"], projy["startDate"], projy["custom"]["Expected go-live date"], None, projy["progress"], None]
    return arraydProj


# def customFieldParser(projectsDict):
#     customFieldDict = {}
#     for projdict in projectsDict:
#         customFieldDict[projdict["name"]] = customFieldIsolate(projdict["custom"])
    
#     writeProjectToJson(customFieldDict, "custom_export.json")
    
# def customFieldIsolate(custom):
#     retproj = {}
#     for thing in custom:
#         for key, value in thing.items():
#             dummy = {key: value}
#             retproj[key] = value

#     return retproj

def customIsolateSingle(customObj):
    returnCustom = {}
    for dicty in customObj:
        for key, value in dicty.items():
            returnCustom[key] = value

    return returnCustom

def progresCalc(open, closed):
    if closed == 0:
        return 0
    else:
        total = open + closed
        return round(closed/total*100)

# def durationCalc(start, goLiveDate):
    
def writeProjectToJson(jsonObj, dest):
    # Accepts a JSON object, and dumps it into a specified destination file.
    print("Writing to ", dest)
    with open(dest, "w") as outfile:
        json.dump(jsonObj, outfile)

zohoDump = fetchAllProjects(projectsConfig)
isolatedProjects = zohoDump["projects"]
print("Parsing:", len(isolatedProjects), "projects")
parsedProjects = parseAllProjects(isolatedProjects)
writeDict = {
    time = datetime.datetime.now()
    projects = parsedProjects
}

def projList(projects):
    returnList= []
    for projj in parsedProjects:
        returnList.append([None, projj["name"], projj["owner"], projj["startDate"], None, projj["progress"], None])
    return returnList

# writeProjectToJson(projList(parsedProjects), "../chart/list.json")

writeProjectToJson(parsedProjects, "../chart/output.json")

# customFieldParser(parsedProjects)
