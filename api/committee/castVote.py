from api.everything import *
from api.faculty import getFacultyWithProjects, getLDAPFaculty, getFacultyForProject
from api.projects import getProjectByID
from api.programs import getAllPrograms
from api.pages.budget import getAllBudgets
from api.voting import getVotes, getCommitteeVotes, getVote
from api.pages.collaborators import getCollaborators

from api.pages import *
import pprint

@app.route("/committee/castVote/<pid>", methods = ["GET"])
@login_required
def vote_GET ( pid):
  if not g.user.isCommitteeMember:
    abort(403)
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
              .where(Voting.committeeID == g.user.username)
              .exists()
      ):
    app.logger.info("Vote already exists\n")
    votes = getVote(g.user.username, pid)
  else:
  #   app.logger.info("Creating new row for {0} and {1}\n".format(username, pid))
  #   votes = (Voting.create (committeeID = username, 
  #                         projectID = pid
  #                         )
  #           )
      votes = None
  return render_template (  "castVote.html",
                            proj = project,
                            username = g.user.username,
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
  


@app.route("/committee/castVote/<pid>", methods = ["POST"])
@login_required
def vote_POST (pid):
  if not g.user.isCommitteeMember:
    abort(403)
  # NOTE: username is the committee member, NOT the project creator
  faculty =  getFacultyForProject(pid)
  
  data = request.form

  print "Data is: " + str(data)
  
  votingTable = getVote(g.user.username, pid)
  if votingTable is None:
    votingTable = (Voting.create (committeeID = g.user.username, 
                           projectID = pid
                           )
                  )
  
  votingTable.committeeID             = g.user.username 
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
                            username = g.user.username,
                            cfg = cfg,
                            fac = faculty,
                            votes = votingTable,
                            proj = project,
                            success = True
                          )
  
