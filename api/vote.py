from everything import *
from faculty import  getFacultyWithProjects, getLDAPFaculty
from projects import getAllProjects
from programs import getAllPrograms
from budget import getAllBudgets
from voting import getVotes, getCommitteeVotes, getVote

from pages import *
import pprint

@app.route("/<username>/committee/vote", methods = ["GET"])
def vote_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  # All of our queries
  faculty =  getFacultyWithProjects()
  project = getAllProjects()
  programs = getAllPrograms()
  budget = getAllBudgets()
  # votes = getVotes()
  
  for p in project:
    if (Voting.select()
              .where(Voting.projectID == p.pID)
              .exists()
       ):
      votes = getVote(username, p)
    else:
      votes = Voting.create(committeeID = username, projectID = p.pID)
  
  theirVotes = getCommitteeVotes(username)
  outVotes = []
  if theirVotes is not None:
    for vote in theirVotes:
      outVotes.append(vote)
    
  return render_template (  "vote.html",
                            proj = project,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            progs = programs,
                            budg = budget,
                            votes = outVotes
                          )

@app.route("/<username>/committee/vote", methods = ["POST"])
def vote_POST (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  data = request.form

  print "Data is: " + str(data)
  
  # TODO: Need to test if row exists to update votes OR create a new row; 
  # currently always writes to the first row, and in random order (based on dictionary order)
  for key, value in data.iteritems():
    projectAndColumn = key.split("-")
    votes = getCommitteeVotes(username)
    
    print projectAndColumn  
    
    if (Voting.select()
              .where(Voting.projectID == projectAndColumn[0]).exists()
       ):
      votes = getVote(username, projectAndColumn[0])
    else:
      votes = Voting.create(committeeID = username, projectID = projectAndColumn[0])
      
    # print "Key " + key
    # print "Value " + value
    print votes.projectID
    votes.urcppGoalsVote      = (value if projectAndColumn[1] == "urcppGoalsVote" else votes.urcppGoalsVote)
    votes.projectDetailsVote  = (value if projectAndColumn[1] == "projectDetailsVote" else votes.projectDetailsVote)
    votes.facultyRoleVote     = (value if projectAndColumn[1] == "facultyRoleVote" else votes.facultyRoleVote)
    votes.studentRoleVote     = (value if projectAndColumn[1] == "studentRoleVote" else votes.studentRoleVote)
    votes.feasibilityVote     = (value if projectAndColumn[1] == "feasibilityVote" else votes.feasibilityVote)
    votes.save()
  
  theirVotes = getCommitteeVotes(username)
  outVotes = []
  for vote in theirVotes:
    outVotes.append(vote)
  # print(pprint.pformat(theirVotes))
  # print theirVotes
  faculty =  getFacultyWithProjects()
  return render_template (  "vote.html",
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            votes = outVotes
                          )
  
