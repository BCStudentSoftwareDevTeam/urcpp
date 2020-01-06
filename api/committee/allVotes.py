from ..everything import *
from ..API.faculty import getFacultyWithProjects
from ..API.voting import getVotesByProject
from ..API.parameters import getCurrentParameters
from ..API.parameters import getParametersByYear
@app.route("/committee/allVotes/<int:year>", methods = ["GET"])
@app.route("/committee/allVotes", methods = ["GET"])
def allVotes(year=None):
  if not g.user.isCommitteeMember:
    abort(403)

  # we need the current year to get the current projects
  if year is None:
    applicationCycle = getCurrentParameters()
  else:
    flash("You are viewing votes from applicationCycle: {}".format(year), 'warning')
    applicationCycle = getParametersByYear(year)

  # All of our queries
  faculty = getFacultyWithProjects(applicationCycle.year)

  # For each project, get average of votes in each category
  votes = []
  if  faculty is not None:
    for fac in faculty:
      votes.append(getVotesByProject(fac.pID.pID))

  return render_template ("committee/allVotes.html",
                          cfg = cfg,
                          fac = faculty,
                          votes = votes,
                         )
