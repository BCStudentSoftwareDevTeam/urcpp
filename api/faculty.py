from everything import *
import json

def previousYearsFunded (username):
  urcppFacultyQ = (URCPPFaculty.select()
    .where (URCPPFaculty.username == username)
  )
  
  if urcppFacultyQ.exists():
    return urcppFacultyQ.get()
  else:
    return None

def getFaculty (username):
  facQ = (URCPPFaculty.select()
    .where (URCPPFaculty.username == username)
    )
  
  if facQ.exists():
    return facQ.get()
  else:
    return None
    
@app.route("/urcpp/v1/faculty/get/<username>", methods = ["POST"])
def faculty_get (username):
  if username != os.getenv("USER"):
    return { "response": cfg["response"]["badUsername"] }
  
  fac = getFaculty(username)  
  
  if fac:
    response = {  "response" : "OK" }
    response["faculty"] = m2d(fac)
    return jsonify(response)
  else:
    response = { "response": cfg["response"]["noResults"],
                 "details": "No faculty found for username {0}.".format(username)
                 }
    return jsonify(response)  


@app.route ("/urcpp/v1/faculty/previousYearsFunded/<username>", methods = ["POST"])
def faculty_previousYearsFunded (username):
  if username != os.getenv("USER"):
    return { "response": cfg["response"]["badUsername"] }

  urcppFaculty = previousYearsFunded(username)
  
  if urcppFaculty:
    response = {  "response" : "OK" }
    if urcppFaculty.yearsFunded != "": 
      fundedDict = json.loads(urcppFaculty.yearsFunded)
      response["urcppFaculty"] = fundedDict
    else: 
      response["urcppFaculty"] = ""
    
    return jsonify(response)
  else:
    response = { "response": cfg["response"]["noResults"],
                 "details": "No results found for project for user {0}.".format(username)
                 }
    return jsonify(response) 
    
