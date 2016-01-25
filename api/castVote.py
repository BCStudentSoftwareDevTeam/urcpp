from everything import *
from faculty import getFacultyWithProjects, getLDAPFaculty, getFacultyForProject
from projects import getProjectByID
from programs import getAllPrograms
from budget import getAllBudgets
from voting import getVotes, getCommitteeVotes, getVote
from collaborators import getCollaborators

from pages import *
import pprint

@app.route("/<username>/committee/castVote/<pid>", methods = ["GET"])
def vote_GET (username, pid):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  project = getProjectByID(pid)
  if project is None:
    return render_template ("noProject.html", 
                            cfg = cfg)
  faculty =  getFacultyForProject(pid)
  collaborators = getCollaborators(faculty)
  
  # Get votes for pid and username
  # Prepopulate
  if (  Voting.select()
              .where(Voting.projectID == pid)
              .where(Voting.committeeID == username)
              .exists()
      ):
    app.logger.info("Vote already exists\n")
    votes = getVote(username, pid)
  else:
  #   app.logger.info("Creating new row for {0} and {1}\n".format(username, pid))
  #   votes = (Voting.create (committeeID = username, 
  #                         projectID = pid
  #                         )
  #           )
      votes = None
  return render_template (  "castVote.html",
                            proj = project,
                            username = username,
                            cfg = cfg,
                            votes = votes,
                            fac = faculty,
                            collab = collaborators,
                          )
  # # All of our queries
  # faculty =  getFacultyWithProjects()
  # programs = getAllPrograms()
  # budget = getAllBudgets()
  # # votes = getVotes()
  
  # for p in project:
  #   if (Voting.select()
  #             .where(Voting.projectID == p.pID)
  #             .exists()
  #     ):
  #     votes = getVote(username, p)
  #   else:
  #     votes = Voting.create(committeeID = username, projectID = p.pID)
  
  # theirVotes = getCommitteeVotes(username)
  # outVotes = []
  # if theirVotes is not None:
  #   for vote in theirVotes:
  #     outVotes.append(vote)
    
  # return render_template (  "vote.html",
  #                           proj = project,
  #                           username = username,
  #                           cfg = cfg,
  #                           fac = faculty,
  #                           progs = programs,
  #                           budg = budget,
  #                           votes = outVotes
  #                         )
  


@app.route("/<username>/committee/castVote/<pid>", methods = ["POST"])
def vote_POST (username, pid):
  # NOTE: username is the committee member, NOT the project creator
  faculty =  getFacultyForProject(pid)

  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  data = request.form

  print "Data is: " + str(data)
  
  votingTable = getVote(username, pid)
  if votingTable is None:
    votingTable = (Voting.create (committeeID = username, 
                           projectID = pid
                           )
                  )
  
  votingTable.committeeID             = username 
  votingTable.projectID               = pid
  votingTable.studentLearning         = data["studentLearning"]
  votingTable.studentAccessibility    = data["studentAccessibility"]
  votingTable.qualityOfResearch       = data["qualityOfResearch"] 
  votingTable.studentDevelopment      = data["studentDevelopment"]
  votingTable.facultyDevelopment      = data["facultyDevelopment"]
  votingTable.collaborative           = data["collaborative"]
  votingTable.interaction             = data["interaction"]
  votingTable.communication           = data["communication"]
  votingTable.scholarlySignificance   = data["scholarlySignificance"]
  votingTable.proposalQuality         = data["proposalQuality"]
  votingTable.budget                  = data["budget"]
  votingTable.timeline                = data["timeline"]
  votingTable.comments                = data["comments"]
  votingTable.save()

  project = getProjectByID(pid)
  return render_template (  "castVote.html",
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            votes = votingTable,
                            proj = project,
                            success = True
                          )
  
