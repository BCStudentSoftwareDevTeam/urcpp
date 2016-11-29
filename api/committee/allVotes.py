from ..everything import *
from ..API.faculty import getFacultyWithProjects
from ..API.voting import getVotesByProject
from ..API.parameters import getParameters

@app.route("/committee/allVotes", methods = ["GET"])
def allVotes_GET ():
  if not g.user.isCommitteeMember:
    abort(403)
    
  # we need the current year to get the current projects
  applicationCycle = getParameters()
  # All of our queries
  faculty = getFacultyWithProjects(applicationCycle.year)

  # For each project, get average of votes in each category
  votes = []
  if  faculty is not None:
    for fac in faculty:
      votes.append(getVotesByProject(fac.pID.pID))
  
  return render_template ("allVotes.html",
                          cfg = cfg,
                          fac = faculty,
                          votes = votes,
                         )
