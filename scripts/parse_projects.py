import json

# OPEN THE PARSED ZOHO PROJECTS FILE
with open("../chart/output.json") as f:
    projectDict = json.load(f)

def parseAllProjects(rawProjects):
    # Takes in a dict of "rawProjects" from Zoho Projects, returns a list of parsed projects 
    allParsedProjects = []
    for aProject in rawProjects:
        currentProject = (singleProjectBuilder(aProject))
        allParsedProjects.append(currentProject)
        print("Current", currentProject)
    return allParsedProjects
    
def singleProjectBuilder(rawProject):
    # Takes a single "rawProject" Zoho Project JSON object, returns a parsed object, "parsedProject"
    print("RAW ", rawProject)
    # projProgress = progresCalc(rawProject["task_count"]["open"], rawProject["task_count"]["closed"])
    # parsedProject = {
    #         "name": rawProject["name"],  
    #         "projectId": rawProject["id"],
    #         "owner": rawProject["owner_name"],
    #         "startDate": rawProject["start_date"],
    #         "custom": customIsolateSingle(rawProject["custom_fields"]),
    #         "tasks_open": rawProject["task_count"]["open"],
    #         "tasks_closed": rawProject["task_count"]["closed"],
    #         "status": rawProject["status"],
    #         "progress" : str(projProgress),
    #         "progress_val" : projProgress
    # }
  
def customIsolateSingle(customObj):
    # Takes in a dict of "custom_fields" from Zoho, and parses them into a flat dict.
    returnCustom = {}
    for dicty in customObj:
        for key, value in dicty.items():
            returnCustom[key] = value

    return returnCustom

def progresCalc(open, closed):
    # Takes a number of open and closed tasks, returns a completion percentage, rounded.
    if closed == 0:
        return 0
    else:
        total = open + closed
        return round(closed/total*100)

parsedDict = parseAllProjects(projectDict)
