import json
import datetime
# from fetch_projects import writeProjectToJson

# OPEN THE PARSED ZOHO PROJECTS FILE
with open("../data/projects.json") as f:
    json_projects = json.load(f)

# Calculate weeks to start
def formatDate(dateList):
  # Returns a list of ints representing a date in the format [YYYY, MM, DD], with leading zeros removed
  noZero = []
  for date in dateList.split('-'):
    if date[0] != "0":
      noZero.append(int(date))
    else:
      noZero.append(int(date[1]))
  noZero.reverse()
  return noZero

# Datetime needs three ints to represent a date
def makeDateTime(dateList):
  day = dateList[1]
  month = dateList[2]
  year = dateList[0]
  dateTimeObj = datetime.date(year, month, day)
  return dateTimeObj

def timeBtweenWeeks(startWk, endWk):
  # Takes in a "start" date and a "go_live" date, and returns the weeks between them
  start = makeDateTime(formatDate(startWk))
  end = makeDateTime(formatDate(endWk))
  diff = (end - start).days
  weeks = round(diff / 7)
  return weeks


def parseAllProjects(allProjects):
    allParsedProjects = []
    for project in allProjects:
        allParsedProjects.append(parseProj(project))
    return allParsedProjects

def parseProj(project):
    tempProj = {
        'specialist': project['owner'],
        'client': project['name'],
        'mrr': 107,
        # 'mrr': project['custom']['mrr'],                                      UNCOMMENT ONCE DATA IS ENTERED
        'completionPctg': project['progress'],
        'goLive': '08-30-2018',                                                # CHANGE TO DICT VALUES ONCE DATA IS ENTERED 
        'weeksToStart': timeBtweenWeeks(project['startDate'], '08-30-2018')    # CHANGE TO DICT GO_LIVE DATE ONCE DATA IS ENTERED 
    }
    return tempProj

def perSpecialist(projects):
    specialists = {}

    for project in projects:
        name = project['specialist']

        if project['specialist'] in specialists.keys():
            tempName = project['specialist']
            specialists[tempName]['projects'] += 1
            specialists[tempName]['mrr'] += project['mrr']
            specialists[tempName]['wksToStart'].append(project['weeksToStart'])
            specialists[tempName]['completion'].append(project['completionPctg'])
            specialists[tempName]['goLive'].append(makeDateTime(formatDate(project['goLive'])))
        else:
            specialists[name] = {
                'projects' : 1,
                'mrr' : int(project['mrr']),
                'wksToStart' : [project['weeksToStart']],
                'completion' : [project['completionPctg']],
                'goLive' : [makeDateTime(formatDate(project['goLive']))]
            }
    
    return specialists


def combineProjects(perSpec):
    print(perSpec)
    for aspec in perSpec:
        print(perSpec[aspec]['mrr'] / perSpec[aspec]['projects'])
    

parsedProjDict = parseAllProjects(json_projects)
projectsPerSpec = perSpecialist(parsedProjDict)
combineProjects(projectsPerSpec)
