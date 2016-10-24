from everything import *
from faculty import  getFacultyWithProjects
from projects import getProjectByID
from collaborators import getAllCollaborators
from voting import getVote
# TODO: I dont think this import is being used anymore
from pages import *
from applicationCycle import getCurrentCycle

@app.route("/committee/allProjects", methods = ["GET"])
@login_required
def allProjects_GET ():
  if not g.user.isCommitteeMember:
    abort(403)
  # All of our queries
  # we need the current year to get current faculty with projects
  currentCycle = getCurrentCycle()
  
  faculty =  getFacultyWithProjects(currentCycle.year)
  collaborators = getAllCollaborators()
  previousVote = {}
  if faculty:
    for fac in faculty:
      if getVote(g.user.username, fac.pID.pID) is not None:
        previousVote[fac.pID.pID] = True
      else:
        previousVote[fac.pID.pID] = False
  
  return render_template (  "allProjects.html",
                            username = g.user.username,
                            cfg = cfg,
                            fac = faculty,
                            prev = previousVote,
                            collab = collaborators
                          )

@app.route("/committee/allProjects/updateStatus", methods = ["POST"])
@login_required
def updateStatus_POST ():
  if not g.user.isCommitteeMember:
    abort(403)
  
  data = request.form
  for key, value in data.iteritems():
    projectToSetStatus = getProjectByID(key)
    projectToSetStatus.status = value
    projectToSetStatus.save()

  # TODO: create redirect back function and use instead
  return redirect(url_for('allProjects_GET'))
