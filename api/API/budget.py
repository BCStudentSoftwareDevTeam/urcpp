from ..everything import *
from projects import getProject
from .parameters import getCurrentParameters

def getBudget (username):
   """  gets the budget for a user in the current application year.
    
        Args:
          username (str): the user to whom the budget should belong to
            
        Returns:
          Budget Model: the budget for the user
   """
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

def getTotalBudget(bID):
    """ Returns the sum of the budget """ 
    budgQ = (Budget.select()
          .where (Budget.bID == bID)
          )
    parameters = getCurrentParameters()
    if budgQ.exists():
        budget = budgQ.get()
        total = 0
        for fund in cfg["totalBudget"]:
            if fund == 'miles':
                amount = int(getattr(budget, fund)) * parameters.mileageRate
            else:
                amount = int(getattr(budget, fund))
            total += amount
        return total
    else:
        return None


def getAllBudgets ():
  """ Gets all of the budgets for the current application cycle """
  year = getCurrentCycle()
  
  budgQ = (Budget.select()
            .join(Projects)
            .where(Projects.year == year))
  
  app.logger.info("Looking for all budgets with query:\n\n" + budgQ + "\n\n")
  
  if budgQ.exists():
    return budgQ.execute()
  else:
    return None