from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from budget import getBudget

from pages import *

@app.route("/<username>/create", methods = ["GET"])
def create_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }

  # All of our queries
  faculty = getFaculty(username)
  ldapFaculty = getLDAPFaculty(username)
  proj = getProject(username)
  programs = getAllPrograms()
  
  
  return render_template (  "create.html",
                            proj = proj,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            ldap = ldapFaculty,
                            progs = programs,
                          )

@app.route("/<username>/create", methods = ["POST"])
def create_POST (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }

  # Grab the .body() from the aja() POST
  data = request.form

  # This is what our post from this page looks like
  # {duration: "8", program: "1", startDate: "May 1", title: "URCPP Software Also"}
  
  # First, update the project title
  faculty = getFaculty(username)
  ldapFaculty = getLDAPFaculty(username)
  proj = getProject(username)
  programs = getAllPrograms()
  
  proj = getProject(username)
  budg = getBudget(username)
  
  if proj is None:
    proj = Projects()
  
  if budg is None:
    budg = Budget()
    budg.save()
  
  proj.title      = data["title"]
  proj.startDate  = data["startDate"]
  proj.duration   = int(data["duration"])
  proj.budgetID   = budg.bID
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
  
  #response = { "response" : "OK" }
  #return jsonify(response)
  
  return render_template (  "people.html",
                            proj = proj,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            ldap = ldapFaculty,
                            progs = programs,
                          )
