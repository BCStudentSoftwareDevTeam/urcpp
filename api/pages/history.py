from api.everything import *
from api.faculty import getFaculty, getLDAPFaculty
from api.projects import getProject
from api.programs import getAllPrograms
from collaborators import getCollaborators
from budget import getBudget

def buildJSONHistory (data, username):
  jsonOut  = "{\n"

  for h in cfg["history"]:
    result = data.get((username + "-" + h["db"]), default = "")  
    if result == username + "-" + h["db"]:
      jsonOut += h["db"] + ": true, \n"
    
  jsonOut += "}"
  # print "JSON finale: " + jsonOut
  return (jsonOut)

@login_required
@app.route("/history", methods = ["GET"])
def history_GET ():
  faculty = getFaculty(g.user.username)
  collaborators = getCollaborators(g.user.username)
  if collaborators is None:
    collaborators = []    # Deals with null value
  
  return render_template (  "history.html",
                            username = g.user.username,
                            cfg = cfg,
                            fac = faculty,
                            ldap = g.user.username,
                            collabs = collaborators,
                          )
               
@login_required
@app.route("/history", methods = ["POST"])
def history_POST ():
  
  faculty = getFaculty(g.user.username)
  collaborators = getCollaborators(g.user.username)
  
  data = request.form
  
  #Creates yearsFunded value for faculty member
  faculty.yearsFunded = buildJSONHistory(data, faculty.username.username)
  faculty.save()
  
  # Creates yearsFunded value for collaborators
  if collaborators:
    for collab in collaborators:
      collab.yearsFunded = buildJSONHistory(data, collab.username.username)
      collab.save()
      
  return redirect(url_for("irbyn_GET"))