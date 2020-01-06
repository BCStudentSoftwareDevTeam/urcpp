from ..everything import *
from ..API.faculty import getFacultyForProject
from ..API.projects import getProjectByID
from ..API.voting import getCommitteeVotes, getVote
from ..API.collaborators import getCollaborators

@app.route("/committee/castVote/<pid>", methods = ["GET"])
@login_required
def vote_GET ( pid):
  if not g.user.isCommitteeMember:
    abort(403)
  project = getProjectByID(pid)
  if project is None:
    return render_template ("committee/noProject.html",
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
  return render_template (  "committee/castVote.html",
                            proj = project,
                            username = g.user.username,
                            cfg = cfg,
                            votes = votes,
                            fac = faculty,
                            collab = collaborators,
                          )

@app.route("/committee/castVote/<pid>", methods = ["POST"])
@login_required
def vote_POST (pid):
  if not g.user.isCommitteeMember:
    abort(403)
  # NOTE: username is the committee member, NOT the project creator
  faculty =  getFacultyForProject(pid)

  data = request.form.todict()

  print "Data is here: " + str(data)

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
#  The fields that are commented out are like so because they no longer show in the UI so
#   there is no way to gather data for them, else the page will get a bad request when the user
# submits a vote.
  #votingTable.studentDevelopment      = data["studentDevelopment"]
  #votingTable.facultyDevelopment      = data["facultyDevelopment"]
  votingTable.development             = data["development"]
  votingTable.collaborative           = data["collaborative"]
  #votingTable.interaction             = data["interaction"]
  #votingTable.communication           = data["communication"]
  #votingTable.scholarlySignificance   = data["scholarlySignificance"]
  votingTable.proposalQuality         = data["proposalQuality"]
  votingTable.budget                  = data["budget"]
  votingTable.timeline                = data["timeline"]
  votingTable.comments                = data["comments"]
  votingTable.save()

  project = getProjectByID(pid)
  return render_template (  "committee/castVote.html",
                            username = g.user.username,
                            cfg = cfg,
                            fac = faculty,
                            votes = votingTable,
                            proj = project,
                            success = True
                          )
