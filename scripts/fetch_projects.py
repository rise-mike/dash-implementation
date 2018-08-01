import requests
import json
from config import projectsConfig

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
    
def singleProjectBuilder(rawProject):
    # Takes a single "rawProject" Zoho Project JSON object, returns a parsed object, "parsedProject"
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

def arrayProjectBuilder(projy):
    arraydProj = [None, projy["name"], projy["owner"], projy["startDate"], projy["custom"]["Expected go-live date"], None, projy["progress"], None]
    return arraydProj

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

zohoDump = fetchAllProjects(projectsConfig)

isolatedProjects = zohoDump["projects"]
parsedProjects = parseAllProjects(isolatedProjects)

writeProjectToJson(isolatedProjects, "../data/rawprojects.json")
writeProjectToJson(parsedProjects, "../data/projects.json")

def main():
    pass

if __name__ == "__main__":
    main()