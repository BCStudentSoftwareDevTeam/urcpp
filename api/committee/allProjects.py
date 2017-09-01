from ..everything import *
from ..API.faculty import  getFacultyWithProjects, getFacultyForProject
from ..API.projects import getProjectByID
from ..API.collaborators import getAllCollaborators
from ..API.voting import getVote
from ..API.parameters import getCurrentParameters
from ..API.files import removeFiles
from ..API.projects import getProject

@app.route("/committee/allProjects", methods = ["GET"])
@login_required
def allProjects_GET ():
  if not g.user.isCommitteeMember:
    abort(403)
  # All of our queries
  # we need the current year to get current faculty with projects
  currentCycle = getCurrentParameters()
  
  faculty =  getFacultyWithProjects(currentCycle.year)
  collaborators = getAllCollaborators()
  previousVote = {}
  if faculty:
    for fac in faculty:
      if getVote(g.user.username, fac.pID.pID) is not None:
        previousVote[fac.pID.pID] = True
      else:
        previousVote[fac.pID.pID] = False
  
  return render_template (  "committee/allProjects.html",
                            username = g.user.username,
                            cfg = cfg,
                            fac = faculty,
                            prev = previousVote,
                            collab = collaborators
                          )

@app.route("/committee/allProjects/updateStatus", methods = ["POST"])
@login_required

def updateStatus_POST ():
  
  data = request.form
  if not g.user.isCommitteeMember:
    try:
      proj = getProject(g.user.username)
      m = dict(data)
      proj.status = m[str(proj.pID)][0]
      proj.save()
      if proj.status == "withdrawn":
        print "project status: ", proj.status
        removeFiles(g.user.username)  
    except:
      abort(403)
      
  else:
    for key, value in data.iteritems():
      projectToSetStatus = getProjectByID(key)
      projectToSetStatus.status = value
      projectToSetStatus.save()
      
      professor = getFacultyForProject(key)
      if projectToSetStatus.status == "withdrawn":
        print "project status: ", projectToSetStatus.status
        removeFiles(professor.username.username)
      
      
  
  return redirect(url_for('allProjects_GET'))

