from everything import *
from faculty import  getFacultyWithProjects, getLDAPFaculty
from projects import getAllProjects, getProjectByID
from collaborators import getAllCollaborators
from programs import getAllPrograms
from budget import getAllBudgets
from voting import getVote
from pages import *

@app.route("/<username>/committee/allProjects", methods = ["GET"])
def allProjects_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  # All of our queries
  faculty =  getFacultyWithProjects()
  project = getAllProjects()
  programs = getAllPrograms()
  budget = getAllBudgets()
  collaborators = getAllCollaborators()
  previousVote = {}
  if project:
    for proje in project:
      if getVote(username, proje.pID) is not None:
        previousVote[proje.pID] = True
      else:
        previousVote[proje.pID] = False
  
  return render_template (  "allProjects.html",
                            proj = project,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            progs = programs,
                            budg = budget,
                            prev = previousVote,
                            collab = collaborators
                          )

@app.route("/<username>/committee/allProjects/updateStatus", methods = ["POST"])
def updateStatus_POST (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  faculty =  getFacultyWithProjects()
  programs = getAllPrograms()
  budget = getAllBudgets()
  
  data = request.form
  for key, value in data.iteritems():
    projectToSetStatus = getProjectByID(key)
    projectToSetStatus.status = value
    projectToSetStatus.save()

  project = getAllProjects()
  return render_template (  "allProjects.html",
                            proj = project,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            progs = programs,
                            budg = budget,
                          ) 
