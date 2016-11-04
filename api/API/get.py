from everything import *
from applicationCycle import getCurrentCycle
# https://github.com/micha/resty
# Also, Postman in Chrome
# Also, http://blog.luisrei.com/articles/flaskrest.html
# Also, https://github.com/jpillora/jquery.rest
# For testing: http://unirest.io/python.html
# Also, the unittest library.
# Also for REST: http://restkit.readthedocs.org/en/latest/

@app.route ("/t/<path:path>", methods = ["GET"])
def templates (path):
  return render_template (path, username = os.getenv('USER'))

@app.route ("/urcpp/v1/programs/getAll", methods = ["POST"])
def programs_getAll ():
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  # This returns the program table
  
  progQ = (Programs.select())
  
  if progQ.exists():
    response = {  "response" : "OK" }
    progs = progQ.select()
    response['programs'] = map(m2d, progs)
    return jsonify(response)
  else:
    response = { "response": cfg["response"]["noResults"],
                 "details": "No results found for all programs." }
    return jsonify(response) 

@app.route("/urcpp/v1/projects/getTitle/<username>", methods = ["POST"])
def projects_getTitle (username):
  if username != os.getenv("USER"):
    return { "response": cfg["response"]["badUsername"] }
  
  # Look up the project title for this user.
  
  projQ = (Projects.select()
    .join (URCPPFaculty, on = (URCPPFaculty.pID == Projects.pID))
    .where (URCPPFaculty.username == username)
    .where (URCPPFaculty.corresponding == True)
  )
  
  if projQ.exists():
    response = {  "response" : "OK" }
    proj = projQ.get()
    response['project'] = m2d(proj)
    return jsonify(response)
  else:
    response = { "response": cfg["response"]["noResults"],
                 "details": "No results found for project title." }
    return jsonify(response) 


### Get Narrative ###  
@app.route("/urcpp/v1/projects/getNarrative/<username>", methods = ["POST"])
def getNarrative (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  

  applicationCycle = getCurrentCycle().year
  
  knownFiles = os.listdir()
  
  for filenames in knownFiles:
    if "narrative" in filenames:
      response = {"response": "OK",
      "narrative": filenames}
      return jsonify(response)
    else:
      response = { "response": cfg["response"]["noResults"],
                "details": "No results found for project Narrative." }
      return jsonify(response) 
  
  # projQ = (Projects.select()
  #   .join (URCPPFaculty, on = (URCPPFaculty.pID == Projects.pID))
  #   .where (URCPPFaculty.username == username)
  #   .where (URCPPFaculty.corresponding == True)
  # )
  
  # if projQ.exists():
  #   response = {  "response" : "OK" }
  #   proj = projQ.get()
  #   response['project'] = m2d(proj)
  #   return jsonify(response)
  # else:
  #   response = { "response": cfg["response"]["noResults"],
  #               "details": "No results found for project title." }
  #   return jsonify(response) 
###################################################
# JUNK BELOW THIS LINE

@app.route ("/urcpp/v1/faculty/details/<username>", methods = ["POST"])
def getFacultyDetails (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
    
  # FIXME: The funny library pushes things through as... form data?
  # force is for ignoring headers
  # data = request.get_json (force = True)
  data = request.form
  app.logger.info ("POST gfd: {0} {1}".format(username, data))

  response = {  "response" : "OK" }
  for k in data:
    response[k] = data[k]

  app.logger.info ("POST gfd: {0} {1}".format(username, data))

  return jsonify (response)
