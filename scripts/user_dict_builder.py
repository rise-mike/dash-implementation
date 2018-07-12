import json
from fetch_projects import writeProjectToJson

# OPEN THE PARSED ZOHO PROJECTS FILE
with open("../chart/output.json") as f:
    json_projects = json.load(f)

# CREATE DICT OF USERS "USER_NAME: DICT_OF_USER'S_PROJECTS"

def parseUsers(projects): 
    users_dict = {}
    for project in projects:
        current_owner = project["owner"]
        
        if current_owner not in users_dict.keys():
            users_dict[current_owner] = {"project_count" : 1}
        else:
            users_dict[current_owner]["project_count"] += 1

        users_dict[current_owner][project["name"]] = project

    return users_dict


proj_by_user = parseUsers(json_projects)

writeProjectToJson(proj_by_user, "proj_by_user.json")