from everything import *

def getVotesByProject(proj):
  print "Starting query"
  paramsQ =  (Voting.select(
               Voting.projectID,
               fn.Avg(Voting.urcppGoalsVote),
                # fn.Avg(Voting.urcppGoalsVote)
                #   .over(partition_by=[Voting.projectID]),
                fn.Avg(Voting.projectDetailsVote),
                #   .over(partition_by=[Voting.projectID]),
                fn.Avg(Voting.facultyRoleVote),
                #   .over(partition_by=[Voting.projectID]),
                fn.Avg(Voting.studentRoleVote),
                #   .over(partition_by=[Voting.projectID]),
                fn.Avg(Voting.feasibilityVote),
                #   .over(partition_by=[Voting.projectID])
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

def getVote(committee, project):
   
   paramsQ = (Voting.select()
                    .where(Voting.committeeID == committee and
                           Voting.projectID == project)
              )
   
   app.logger.info("Looking for votes with query:\n\n" + paramsQ + "\n\n")
   
   if paramsQ.exists():
      return paramsQ.get()
   else:
      return None

