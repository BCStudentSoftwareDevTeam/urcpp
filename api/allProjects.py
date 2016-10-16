from everything import *
from faculty import  getFacultyWithProjects
from projects import getProjectByID
from collaborators import getAllCollaborators
from voting import getVote
from pages import *
from applicationCycle import getCurrentCycle

@app.route("/<username>/committee/allProjects", methods = ["GET"])
def allProjects_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  # All of our queries
  # we need the current year to get current faculty with projects
  currentCycle = getCurrentCycle()
  
  faculty =  getFacultyWithProjects(currentCycle.year)
  collaborators = getAllCollaborators()
  previousVote = {}
  if faculty:
    for fac in faculty:
      if getVote(username, fac.pID.pID) is not None:
        previousVote[fac.pID.pID] = True
      else:
        previousVote[fac.pID.pID] = False
  
  return render_template (  "allProjects.html",
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            prev = previousVote,
                            collab = collaborators
                          )

@app.route("/<username>/committee/allProjects/updateStatus", methods = ["POST"])
def updateStatus_POST (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  data = request.form
  for key, value in data.iteritems():
    projectToSetStatus = getProjectByID(key)
    projectToSetStatus.status = value
    projectToSetStatus.save()

  # TODO: create redirect back function and use instead
  return redirect(url_for('allProjects_GET', username=username))
