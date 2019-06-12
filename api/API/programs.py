from ..everything import *

def getAllPrograms ():
  """ This function gets  all the programs that exist to date 
  
      Args:
        None
  
      Returns:
        All programs in existence
        
  """
  # This returns the program table from the database
  progQ = (Programs.select()
                   .order_by(+Programs.abbreviation)) # + is how you sort information in ascending order
 
  # if program exists, returns all the programs that exist to date, else return none
  if progQ.exists():
    return progQ.select()
  else:
    return None


@app.route ("/urcpp/v1/programs/getAll", methods = ["POST"]) # reroutes to /urcpp/v1/programs/getAll
def programs_getAll ():
  """ Gives response based on if program exists
  
      Args:
        None
  
      Returns:
         A json response depending on the if the programs can be found
  """
  
  # if the username is not authorized, return badUsername
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
    
  # sets all program, see getProgram function above  
  progs = getAllPrograms()
  
  # if programs can be found, give success response
  if progs:
    response = {  "response" : "OK" }
    dicts = map(m2d, progs) # value within the response dictionary
    app.logger.info("Programs: {0}".format(dicts))
    
    response['programs'] = dicts # response dictionary with the key programs set to the value dicts
    return jsonify(response)
    
  # else it will give an error that there are no results for all programs  
  else:
    response = { "response": cfg["response"]["noResults"],
                 "details": "No results found for all programs." }
    return jsonify(response) 