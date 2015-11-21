from everything import *

@app.route ("/urcpp/v1/programs/getAll", methods = ["POST"])
def programs_getAll ():
  # This returns the program table
  
  progQ = (Programs.select())
  
  if progQ.exists():
    response = {  "response" : "OK" }
    progs = progQ.select()
    
    dicts = map(m2d, progs)
    app.logger.info("Programs: {0}".format(dicts))
    
    response['programs'] = dicts
    return jsonify(response)
  else:
    response = { "response": cfg["response"]["noResults"],
                 "details": "No results found for all programs." }
    return jsonify(response) 