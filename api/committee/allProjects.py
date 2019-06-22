from api.flask_imports import *

from ..everything import cfg
from api.models import *

from api.committee import committee
from ..API.faculty import  getFacultyWithProjects, getFacultyForProject
from ..API.projects import getProjectByID
from ..API.collaborators import getAllCollaborators
from ..API.voting import getVote
from ..API.parameters import getCurrentParameters
from ..API.parameters import getParametersByYear
from ..API.files import removeFiles
from ..API.projects import getProject

@committee.route("/committee/allProjects/<int:year>", methods = ["GET"])
@committee.route("/committee/allProjects", methods = ["GET"])
@login_required
def allProjects(year=None):
  if not g.user.isCommitteeMember:
    abort(403)
  # All of our queries
  # we need the current year to get current faculty with projects
  if year is None:
    currentCycle = getCurrentParameters()
  else:
    flash("You are viewing projects from applicationCycle: {}".format(year), category='warning')
    currentCycle = getParametersByYear(year)


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

@committee.route("/committee/allProjects/updateStatus", methods = ["POST"])
@login_required
def updateStatus_POST ():

  data = request.form
  if not g.user.isCommitteeMember:
    try:
      proj = getProject(g.user.username)
      m = dict(data)
      proj.status = m[str(proj.pID)][0]
      proj.save()
      if proj.status == "Withdrawn":
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
      if projectToSetStatus.status == "Withdrawn":
        print "project status: ", projectToSetStatus.status
        removeFiles(professor.username.username)



  return redirect(url_for('allProjects'))
