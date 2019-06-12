from ..everything import *
from projects import getProject
from .parameters import getCurrentParameters


def getBudget (username):
   """  gets the budget for a user in the current application year 
    
        Args:
          username (str): the user to whom the budget should belong to
            
        Returns:
          BudgQ: the budget for the user specified
   """
   proj = getProject(username); # gets projects associated with the user
   if proj:
     budgQ = (Budget.select()  # BudgQ is the budget for the user's specific project
          .where (Budget.bID == proj.budgetID) # checks to see if the Budget bID number is the same as the project budgetID number
          )
     app.logger.info("Looking for budget with query:\n\n" + budgQ + "\n\n") # print statement to show the budget
   
     if budgQ.exists():
        return budgQ.get() # if BudgQ exists, it's returned
     else:
        return None # else, nothing happens
   else:
      return None # ditto, line 24


def getTotalBudget(bID):
    """   gets the sum of the budget
    
          Args:
            bID: the budget for the user
    
          Returns:
           The sum of the budget 
    """ 
    budgQ = (Budget.select() # Here budgQ gets all of the budgets associated with that user
          .where (Budget.bID == bID)
          )
    parameters = getCurrentParameters() # see parameters.py, checks to see which isCurrentParameter is set to 1
    if budgQ.exists():  
        budget = budgQ.get() # gets the value for budgQ, see line 39, and sets it equal to budget
        total = 0 # sets initial total to 0
        for fund in cfg["totalBudget"]: 
            if fund == 'miles': 
                amount = int(getattr(budget, fund)) * parameters.mileageRate # Uses config.yaml file in order to get the mileage rate for the entire budget
            else:
                amount = int(getattr(budget, fund)) # get all other funds related to the budget
            total += amount
        return total
    else:
        return None


def getAllBudgets ():
    """   gets the sum of all budgets in existence
    
          Args:
            None
    
          Returns:
            All budgets that exists for all projects for every year
    """ 
  year = getCurrentCycle() # sets year equal to the current cycle
  
  budgQ = (Budget.select() # gets the budgets assocciated with all projects in the database for all years as far back as 1998
            .join(Projects)
            .where(Projects.year == year))
  
  app.logger.info("Looking for all budgets with query:\n\n" + budgQ + "\n\n") # tis a print statement
  
  if budgQ.exists():
    return budgQ.execute() # returns all budgets that exist 
  else:
    return None # else return none