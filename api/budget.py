from everything import *

def getBudget (username):
   
   budgQ = (Budget.select()
      .join (URCPPFaculty, on = (URCPPFaculty.pID == Projects.pID))
      .join (Projects, on = (Projects.budgetID == Budget.bID))
      .where (URCPPFaculty.username == username)
      )
   
   app.logger.info("Looking for budget with query:\n\n" + budgQ + "\n\n")
   
   if budgQ.exists():
      return budgQ.get()
   else:
      return None
