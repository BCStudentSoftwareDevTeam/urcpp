from everything import *
from projects import getProject
from faculty import getFaculty

@app.route("/urcpp/v1/set/start/<username>", methods = ["POST"])
def set_start(username):
  if username != os.getenv("USER"):
    return { "response": cfg["response"]["badUsername"] }

  # Grab the .body() from the aja() POST
  data = request.get_json()

  # This is what our post from this page looks like
  # {duration: "8", program: "1", startDate: "May 1", title: "URCPP Software Also"}
  
  # First, update the project title
  proj = getProject(username)
  if proj is None:
    proj = Project()
  
  proj.title      = data["title"]
  proj.startDate  = data["startDate"]
  proj.duration   = int(data["duration"])
  proj.save()  
  
  # Next, update the faculty's program
  fac = getFaculty(username)
  # If they don't exist yet, create one.
  if fac is None:
    fac               = URCPPFaculty()
    fac.username      = username
    fac.corresponding = True
  
  fac.pID       = proj.pID
  fac.programID = int(data["program"])
  fac.save()
  
  # Next, we need 
  
  response = { "response" : "OK" }
  return jsonify(response)
