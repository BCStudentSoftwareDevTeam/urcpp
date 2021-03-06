from ..everything import *

def getAllPrograms ():
  # This returns the program table
  progQ = (Programs.select()
                   .order_by(+Programs.abbreviation)) # + is short for Sort ascending
  
  if progQ.exists():
    return progQ.select()
  else:
    return None

@app.route ("/urcpp/v1/programs/getAll", methods = ["POST"])
def programs_getAll ():
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  progs = getAllPrograms()
  
  if progs:
    response = {  "response" : "OK" }
    dicts = map(m2d, progs)
    app.logger.info("Programs: {0}".format(dicts))
    
    response['programs'] = dicts
    return jsonify(response)
  else:
    response = { "response": cfg["response"]["noResults"],
                 "details": "No results found for all programs." }
    return jsonify(response) 