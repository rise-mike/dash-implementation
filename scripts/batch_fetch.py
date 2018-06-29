import requests
import json

config = {
    "domain": "https://projectsapi.zoho.com/restapi/portal/risepeople/projects/",
    "auth": "hahahahahaha",
    "params": "test"
}

def fetchAllProjects(config):
    # Fetches from the supplied url using a specified token.
    url = config['domain'] + config['auth']
    return requests.get(url).json()
    # writeJson(requests.get(url).json(), "test_dump.json")

def writeProjectToJson(jsonObj, dest):
    # Accepts a JSON object, and dumps it into a specified destination file.
    with open(dest, "w") as outfile:
        json.dump(jsonObj, outfile)

def parseAllProjects(rawProjects):
    # Takes in a dict of "rawProjects" from Zoho Projects, returns a dict of parsed projects 
    allParsedProjects = {}
    for aProject in rawProjects:
      currentProjectName = (aProject["name"])
      allParsedProjects[currentProjectName] : singleProjectBuilder(aProject)
    #   print(singleProjectBuilder(aProject))
    print(allParsedProjects)
    return allParsedProjects
    

def singleProjectBuilder(rawProject):
    # Takes a single "rawProject" Zoho Project JSON object, returns a parsed object, "parsedProject"
    parsedProject = {
        rawProject["name"] : {
            "projId": rawProject["id"],
            "owner": rawProject["owner_name"],
            "startDate": rawProject["start_date"],
            # "goLive": rawProject["custom_fields"][5]["Expected go-live date"],
            "tasks": {
                "open": rawProject["task_count"]["open"],
                "closed": rawProject["task_count"]["closed"],
            },
            "status": rawProject["status"],
        }
    }
    return parsedProject


allProjects = fetchAllProjects(config)
isolatedProjects = allProjects["projects"]

print(parseAllProjects(isolatedProjects))

# print("RETURNED BOYE: ", singleProjectBuilder(allProjects["projects"][1]))

# oneProj = retObj["projects"][0]
# print("FROM API: ", oneProj)
# projBuild(oneProj)


