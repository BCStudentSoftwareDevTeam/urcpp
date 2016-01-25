from everything import *
from faculty import getFaculty, getLDAPFaculty, getFacultyWithProjects
from projects import getAllProjects
from programs import getAllPrograms
from budget import getAllBudgets
from voting import getVotesByProject

from pages import *
import pprint

@app.route("/<username>/committee/allVotes", methods = ["GET"])
def allVotes_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  # All of our queries
  faculty = getFacultyWithProjects()
  proj = getAllProjects()
  programs = getAllPrograms()
  budget = getAllBudgets()

  # For each project, get average of votes in each category
  votes = []
  for p in proj:
    votes.append(getVotesByProject(p.pID))
  
  return render_template ("allVotes.html",
                          proj = proj,
                          username = username,
                          cfg = cfg,
                          fac = faculty,
                          progs = programs,
                          budg = budget,
                          votes = votes,
                         )
