import requests
import json

config = {
    "domain": "https://projectsapi.zoho.com/restapi/portal/risepeople/projects/",
    "auth": "?authtoken=a62f7e0580c4233f34740979bd234442",
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
        print("IN THE FOR LOOP:", singleProjectBuilder(aProject))
        print("Parsed, in loop ", allParsedProjects)

    print("All Parsed Projies: ", allParsedProjects)
    

def singleProjectBuilder(rawProject):
    # Takes a single "rawProject" Zoho Project JSON object, returns a parsed object, "parsedProject"
    parsedProject = {
        rawProject["name"] : {
            "projectId": rawProject["id"],
            "owner": rawProject["owner_name"],
            "startDate": rawProject["start_date"],
            # "goLive": rawProject["custom_fields"][5]["Expected go-live date"],
            "tasks_open": rawProject["task_count"]["open"],
            "tasks_closed": rawProject["task_count"]["closed"],
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


