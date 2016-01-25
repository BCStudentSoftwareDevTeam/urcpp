from everything import *

def getVotesByProject(proj):
  """This function gets the average of all votes for a given project"""
  print "Starting query"
  paramsQ =  (Voting.select(
               Voting.projectID,
               fn.Avg(Voting.studentLearning),
                # fn.Avg(Voting.urcppGoalsVote)
                #   .over(partition_by=[Voting.projectID]),
                fn.Avg(Voting.studentAccessibility),
                #   .over(partition_by=[Voting.projectID]),
                fn.Avg(Voting.qualityOfResearch),
                #   .over(partition_by=[Voting.projectID]),
                fn.Avg(Voting.studentDevelopment),
                #   .over(partition_by=[Voting.projectID]),
                fn.Avg(Voting.facultyDevelopment),
                #   .over(partition_by=[Voting.projectID]),
                fn.Avg(Voting.collaborative),
                fn.Avg(Voting.interaction),
                fn.Avg(Voting.communication),
                fn.Avg(Voting.scholarlySignificance),
                fn.Avg(Voting.proposalQuality),
                fn.Avg(Voting.budget),
                fn.Avg(Voting.timeline)
              )
              .where(Voting.projectID == proj)
              .tuples()
              )
  print "Query built"
  if paramsQ.exists():
    return paramsQ.execute()
  else:
    print "No results"
    return None


def getVotes():
   
   paramsQ = (Voting.select())
   
   app.logger.info("Looking for votes with query:\n\n" + paramsQ + "\n\n")
   
   if paramsQ.exists():
      return paramsQ.get()
   else:
      return None

def getCommitteeVotes(committee):
   
   paramsQ = (Voting.select()
                    .where(Voting.committeeID == committee)
              )
   
   app.logger.info("Looking for votes with query:\n\n" + paramsQ + "\n\n")
   
   if paramsQ.exists():
      return paramsQ.execute()
   else:
      return None

def getVote(username, pid):
  # Gets votes for a committee member (username) for a particular project (pid)
  paramsQ = ( Voting.select()
                    .where(Voting.committeeID == username)
                    .where(Voting.projectID == pid)
            )
  app.logger.info("Looking for {0}'s votes for project {1}\n".format(username, pid))
  
  if paramsQ.exists():
    return paramsQ.get()
  else:
    return None
    
# def getVote(committee, project):
   
#   paramsQ = (Voting.select()
#                     .where(Voting.committeeID == committee and
#                           Voting.projectID == project)
#               )
   
#   app.logger.info("Looking for votes with query:\n\n" + paramsQ + "\n\n")
   
#   if paramsQ.exists():
#       return paramsQ.get()
#   else:
#       return None

