# TODO: we need to either prune this page or add functions for different parameter years - ??????

from ..everything import *


def getCurrentParameters():
  """   A function that checks to see the current year parameters by finding the year that isCurrentParameter is set to 1 and returns the parameter information
  
        Args: 
          None
  
        Returns: 
          The parameters for the current year. This includes pID, year, appOpenDate, appCloseDate, milegaeRate, laborRate, and isCurrntParameter
  """
   
  paramsQ = (Parameters.select().where(Parameters.isCurrentParameter)) # this pulls all the parameter information if isCurrentParameter = 1 in the database
   
  app.logger.info("Looking for parameters with query:\n\n" + paramsQ + "\n\n") # just another print statement
   
  if paramsQ.exists(): # if one of the isCurrentParameter is = 1 
    return paramsQ.get() # return the the row information from the database
  else:
    return None # else return none
    
    
def getParameters(parameters_id):
  """   A function that returns the parameters for the specific ID entered
  
        Args: 
          parameters_id: the parameter ID
  
        Returns: 
          The parameters for the parameters_id entered. This includes pID, year, appOpenDate, appCloseDate, milegaeRate, laborRate, and isCurrntParameter
  
  """

  parameters = (Parameters.select() # parameters is all the parameter information with a specific parameters_id
                    .where(Parameters.pID == parameters_id))
                    
  if parameters.exists():
    return parameters.get() # if parameters listed above exists, returns all parameter information
  else:
    return None # else return none


def getParametersByYear(year):
  """   A function that returns the parameter information for the specific year
  
        Args: 
          year: the year entered - can go as far back as 1998
  
        Returns:
          The parameters for the year
  
  """
  
  parameters = (Parameters.select() # parameters is all the parameter information within a specific year
                    .where(Parameters.year == year)) # checks to see if year is in the database parameters.year
  
  if parameters.exists():
    return parameters.get() # if parameters listed above exists, returns all parameter information
  else:
    return None # else return none
 
  
@app.route("/set/current_parameters/<int:parameters_id>", methods=["GET"]) # reroutes to /set/current_parameters/<int:parameters_id page
@login_required # requires user to be logged in, cannot access straight from URL without being logged in
def set_current_parameters(parameters_id):
  """   If user can access chair page, this function allows the user to change isCurrentParameter
    
        Args: 
          parameters_id: the parameter ID
  
        Returns: 
          Success
        
  """
  
  if not current_user.isChair: # if the user is not a Chair, abort - cannot access page
    abort(403)
  
  # lets the user change isCurrentParameter to false AKA 0
  current_parameters = getCurrentParameters()
  current_parameters.isCurrentParameter = False
  current_parameters.save()
  
  # lets the user change isCurrentParameter to true AKA 1
  new_current_parameters = getParameters(parameters_id)
  new_current_parameters.isCurrentParameter = True
  new_current_parameters.save()
  
  return json.dumps({'success':True}), 200, {'ContentType':'application/json'} # returns success
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  
  