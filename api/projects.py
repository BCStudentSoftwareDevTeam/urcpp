from everything import *
import os

def getProject (username):
  projQ = (Projects.select()
    .join (URCPPFaculty, on = (URCPPFaculty.pID == Projects.pID))
    .where (URCPPFaculty.username == username)
  )
  
  if projQ.exists():
    proj = projQ.get()
    return proj
  else:
    return None

def getAllProjects ():
  allProjQ = (Projects.select())
  
  if allProjQ.exists():
    projs = allProjQ.execute()
    return projs
  else:
    return None
    
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
  response = { "response" : "OK" }
  response["durations"] = cfg["urcpp"]["possibleDurations"]
  return jsonify(response)


### Get Narrative ###  
@app.route("/urcpp/v1/projects/getNarrative/<username>/<path>", methods = ["POST"])
def projects_getNarrative (username, path):
  if username != os.getenv("USER"):
    return { "response": cfg["response"]["badUsername"] }
  
  
  applicationCycle = str(cfg['urcpp']['applicationCycle'])
  dirPath = cfg["filepaths"]["directory"]
  dirPath = dirPath.replace("%%username%%", username)
  dirPath = dirPath.replace("%%applicationCycle%%", applicationCycle)

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

  
  
# ### Get IRB ###  
# @app.route("/urcpp/v1/projects/getIRB/<username>", methods = ["POST"])
# def projects_getIRB (username):
#   if username != os.getenv("USER"):
#     return { "response": cfg["response"]["badUsername"] }
  

#   applicationCycle = str(cfg['urcpp']['applicationCycle'])
  
#   path = cfg["filepaths"]["directory"]
#   path = path.replace("%%username%%", username)
#   path = path.replace("%%applicationCycle%%", applicationCycle)
  
#   knownFiles = os.listdir(path)
  
#   for filenames in knownFiles:
#     print filenames
#     if "irb" in filenames:
#       response = {"response": "OK",
#       "irb": filenames}
#       return jsonify(response)
    
#   response = { "response": cfg["response"]["noResults"],
#             "details": "No results found for project IRB." }
#   return jsonify(response) 