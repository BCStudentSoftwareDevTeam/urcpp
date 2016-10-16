from everything import *
from faculty import getFacultyWithProjects
from voting import getVotesByProject
from applicationCycle import getCurrentCycle

@app.route("/<username>/committee/allVotes", methods = ["GET"])
def allVotes_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
    
  # we need the current year to get the current projects
  applicationCycle = getCurrentCycle()
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
