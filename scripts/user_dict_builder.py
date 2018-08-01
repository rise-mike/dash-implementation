import json
# from fetch_projects import writeProjectToJson

# OPEN THE PARSED ZOHO PROJECTS FILE

with open("../chart/output.json") as f:
    json_projects = json.load(f)

allParsedProjects = []
# print(json_projects[0])

def parseAllProjects(allProjects):
    for project in allProjects:
        parseProj(project)


def parseProj(project):
    print("GO LIVE: ", project["custom"]["go_live"])
    tempProj = {
        'specialist': project['owner'],
        'client': project['name'],
        
        # PLACEHOLDERS, THESE WILL NEED TO BE DELETED
        'mrr': 107,
        'weeksToStart': 9,

        # THESE NEED TO BE UNCOMMENTED ONCE THE FIELDS ARE ACTIVE
        # 'mrr': project['custom']['mrr'],
        # 'weeksToStart': project['custom']['']   THIS NEEDS DATE PARSING "startDate - go_live"
        
        'completionPctg': project['progress'],
        'goLive': project["custom"]["go_live"]
    }
    allParsedProjects.append(tempProj)
    # print("Number of Projects: ", len(allParsedProjects), "\n Current Proj: ", tempProj['client'])


parseAllProjects(json_projects)

print(allParsedProjects)

# CREATE DICT OF USERS "USER_NAME: DICT_OF_USER'S_PROJECTS"

# Create a function that takes a dict of all parsed projects, and returns an array with one dict for each
# implementation specialist.

# A function that takes in a project dict and returns
# name
# specialist
# mrr
# weeksToStart
# completionPctg
# goLive

# A function that takes an array of parsed dict, combines them based on specialist name


# Create a function that takes an individual project dict, 

# def parseUsers(projects): 
#     users_dict = []
#     for project in projects:

#         users_dict.append()

#         print("PROJECT: ", project, "\n")

#         current_owner = project["owner"]
        
#         if current_owner not in users_dict.keys():
#             users_dict[current_owner] = {"project_count" : 1}
#             users_dict[]
#         else:
#             users_dict[current_owner]["project_count"] += 1

#         users_dict[current_owner][project["name"]] = project
#     return users_dict

# def combineProjects(userDict):
#     # print('USER DICT ', userDict)
#     parsedList = []
#     for aUser in userDict:
#         for 
#         tempDict = {
#             'name' : aUser,
#         }
#         # print(aUser['project_count'])
    

    # This needs to add a dict that contains...
    # MRR in progress (loop through and sum)
    # AVG weeks to start - need to calculate them, and take an average
    # AVG completion % - need to calculate completion for each project, take an overall avg
    # AVG completion of all work - weighted avg?
    # Next go-live date - using MIN?




# proj_by_user = parseUsers(json_projects)
# combineProjects(proj_by_user)
# writeProjectToJson(proj_by_user, "../data/proj_by_user.json")