from ..everything import *
from peewee import JOIN
import os
from api.API.parameters import getCurrentParameters

def getProjectByID(projectID):
  projQ = (Projects.select()
                  .where(Projects.pID == projectID)
          )
  if projQ.exists():
    return projQ.get()
  else:
    return None

def getProjectByYear(username, year):
  collaborated_projects = (Projects.select()
                           )
  
  #get the project belonging to this user during the given year
  projQ = (Projects.select(Projects,URCPPFaculty,Collaborators)
                   .join (URCPPFaculty).switch(Projects)
                   .join(Collaborators, JOIN.LEFT_OUTER)
                   .where ((URCPPFaculty.username == username) | (Collaborators.username == username))
                   .where (Projects.year == year)
                   .where (Projects.status != cfg['projectStatus']['Withdrawn']))
  
  if projQ.exists():
    proj = projQ.get()
    return proj
  else:
    return None
    
def getProject (username):
  #get project for this user in the current cycle
  currentCycle = getCurrentParameters()
  if currentCycle is not None:
    year = currentCycle.year
  else:
    year = None
  return getProjectByYear(username, year)
  
def getAllCurrentProjectsByYear(year):
  allProjQ = (Projects.select(Projects, URCPPFaculty)
                      .join (URCPPFaculty, JOIN.LEFT_OUTER).switch(Projects)
                      .where(Projects.year == year, Projects.status != cfg['projectStatus']['Withdrawn']))
  
  projects = {}
  for p in allProjQ:
    if p not in projects.keys():
        projects[p] = {"faculty": p.urcppfaculty.username, 
                       "program": p.urcppfaculty.programID}
    
    projects[p]["collaborators"] = [c.username for c in p.collaborators]

  return projects

def getAllCurrentProjects():
  # we only want to get projects for the current year
  currentCycle = getCurrentParameters()
  if currentCycle is not None:
    year = currentCycle.year
  
  return getAllCurrentProjectsByYear(year)

@app.route("/urcpp/v1/history/<username>", methods = ["GET"])
def getProjectsByUsername(username):
  #TODO: factor the project lists out to their own functions
  projects = (Projects.select()
              .join(URCPPFaculty, on = (URCPPFaculty.pID == Projects.pID))
              .where(URCPPFaculty.username == username)
              .order_by(-Projects.year))
  if projects.exists():
    project_list = []
    for project in projects:
      project_list.append(m2d(project))
  else:
    project_list = []
  
  historyDict = {}
  historyDict['primaryFaculty'] = project_list 
  
  collaborated_projects = (Projects.select()
                           .join(Collaborators, on = (Collaborators.pID == Projects.pID))
                           .where(Collaborators.username == username)
                           )
  if collaborated_projects.exists():
    collaborated_projects_list = []
    for collaborated_project in collaborated_projects:
      collaborated_projects_list.append(m2d(collaborated_project))
  else:
    collaborated_projects_list = []
  
  historyDict['collaborated'] = collaborated_projects_list
  
  return jsonify(historyDict)

    
@app.route("/urcpp/v1/projects/get/<username>", methods = ["POST"])
def projects_get (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  # Look up the project for this user.
  proj = getProject(username)

  if proj:
    response = {  "response" : "OK" }
    response["project"] = m2d(proj)
    return jsonify(response)
  else:
    response = { "response": cfg["response"]["noResults"],
                 "details": "No results found for project title."
                 }
    return jsonify(response)


### Get Duration ###
@app.route("/urcpp/v1/projects/getPossibleDurations", methods = ["POST"])
def projects_getPossibleDurations ():
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  response = { "response" : "OK" }
  response["durations"] = cfg["urcpp"]["possibleDurations"]
  return jsonify(response)


### Get Narrative ###  
@app.route("/urcpp/v1/projects/getNarrative/<username>/<path>", methods = ["POST"])
def projects_getNarrative (username, path):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  applicationCycle = getCurrentParameters()
  dirPath = cfg["filepaths"]["directory"]
  dirPath = dirPath.replace("%%username%%", username)
  dirPath = dirPath.replace("%%applicationCycle%%", applicationCycle.year)

  knownFiles = os.listdir(dirPath)

  for filenames in knownFiles:
    if path in filenames:
      response = {"response": "OK",
      "uploadType": filenames}
      # print "Path exists"
      return jsonify(response)
  response = { "response": cfg["response"]["noResults"],
            "details": "No results found for project file." }
  return jsonify(response) 
