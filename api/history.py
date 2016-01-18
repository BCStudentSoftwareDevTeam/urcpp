from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from collaborators import getCollaborators
from budget import getBudget

from pages import validPageTemplate

def buildJSONHistory (data, username):
  print "Starting JSON build for " + username
  jsonOut  = "{\n"

  for h in cfg["history"]:
    result = data.get((username + "-" + h["db"]), default = "")  
    # print "Result: " + result
    # print "Against: " + username + "-" + h["db"]
    if result == username + "-" + h["db"]:
      jsonOut += h["db"] + ": true, \n"
      # print "JSON LOOKS LIKE: " +jsonOut + "\n"
    
  jsonOut += "}"
  # print "JSON finale: " + jsonOut
  return (jsonOut)

@app.route("/<username>/history", methods = ["GET"])
def history_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  # All of our queries
  faculty = getFaculty(username)
  ldapFaculty = getLDAPFaculty(username)
  proj = getProject(username)
  programs = getAllPrograms()
  # Who knew... the collaborators all go through
  # as LDAPFaculty objects...
  collaborators = getCollaborators(username)
  budget = getBudget(username)
  if collaborators is None:
    collaborators = []    # Deals with null value
  
  return render_template (  "history.html",
                            proj = proj,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            ldap = ldapFaculty,
                            progs = programs,
                            collabs = collaborators,
                          )
                          
@app.route("/<username>/history", methods = ["POST"])
def history_POST (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  # Form data looks like... 
  # [('oneyr', u'oneyr'), ('sixToTenyr', u'sixToTenyr'), ('twoyr', u'twoyr'), ('threeToFiveyr', u'threeToFiveyr')]
  # If the tag exists, the box was checked; otherwise, not checked
  faculty = getFaculty(username)
  collaborators = getCollaborators(username)
  
  data = request.form
  
  # print data
  #Creates yearsFunded value for faculty member
  faculty.yearsFunded = buildJSONHistory(data, faculty.username.username)
  faculty.save()
  
  # Creates yearsFunded value for collaborators
  if collaborators:
    for collab in collaborators:
      # print "Output: " + buildJSONHistory(data, collab.username.username)
      collab.yearsFunded = buildJSONHistory(data, collab.username.username)
      
      # print "Before Save: " + collab.yearsFunded
      collab.save()
      # print "User saved: " + collab.username.username + ": " + collab.yearsFunded
  return redirect (  "/{0}/irbyn".format(username) )