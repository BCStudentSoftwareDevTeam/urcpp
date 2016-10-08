from everything import *
import os
from applicationCycle import getCurrentCycle

def getProjectByID(projectID):
  projQ = (Projects.select()
                  .where(Projects.pID == projectID)
          )
  if projQ.exists():
    return projQ.get()
  else:
    return None

def getProjectByYear(username, year):
  
  #get the project belonging to this user during some year
  projQ = (Projects.select()
    .join (URCPPFaculty, on = (URCPPFaculty.pID == Projects.pID))
    .where (URCPPFaculty.username == username)
    .where (Projects.year == year)
  )
  
  if projQ.exists():
    proj = projQ.get()
    return proj
  else:
    return None
    
def getProject (username):
  #get project for this user in the current cycle
  currentCycle = getCurrentCycle()
  if currentCycle is not None:
	year = currentCycle.year
  else:
	year = None
  return getProjectByYear(username, year)
  
# Do we need this function? We aren't really using it anymore.
def getAllCurrentProjectsByYear(year):
  allProjQ = (Projects.select()).where(Projects.year == year)
  
  if allProjQ.exists():
    return allProjQ
  else:
    return None

def getAllCurrentProjects():
  # we only want to get projects for the current year
  currentCycle = getCurrentCycle()
  if currentCycle is not None:
	year = currentCycle.year
  
  return getAllCurrentProjectsByYear(year)

@app.route("/urcpp/v1/history/<username>", methods = ["GET"])
def getProjectsByUsername(username):
  projects = (Projects.select()
              .join(URCPPFaculty, on = (URCPPFaculty.pID == Projects.pID))
              .where(URCPPFaculty.username == username))
              
  if projects.exists():
    project_list = []
    for project in projects:
      project_list.append(m2d(project))
  
  return jsonify(project_list)

    
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
  
  applicationCycle = getCurrentCycle()
  dirPath = cfg["filepaths"]["directory"]
  dirPath = dirPath.replace("%%username%%", username)
  dirPath = dirPath.replace("%%applicationCycle%%", applicationCycle.year)

  knownFiles = os.listdir(dirPath)

  for filenames in knownFiles:
    if path in filenames:
      response = {"response": "OK",
      "uploadType": filenames}
      print "Path exists"
      return jsonify(response)
  response = { "response": cfg["response"]["noResults"],
            "details": "No results found for project file." }
  return jsonify(response) 
