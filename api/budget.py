from everything import *
from projects import getProject
def getBudget (username):
   proj = getProject(username);
   if proj:
     budgQ = (Budget.select()
          .where (Budget.bID == proj.budgetID)
          )
     app.logger.info("Looking for budget with query:\n\n" + budgQ + "\n\n")
   
     if budgQ.exists():
        return budgQ.get()
     else:
        return None
   else:
      return None

def getAllBudgets ():
  
  year = getCurrentCycle()
  
  budgQ = (Budget.select()
            .join(Projects)
            .where(Projects.year == year))
  
  app.logger.info("Looking for all budgets with query:\n\n" + budgQ + "\n\n")
  
  if budgQ.exists():
    return budgQ.execute()
  else:
    return None