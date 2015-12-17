from everything import *

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

