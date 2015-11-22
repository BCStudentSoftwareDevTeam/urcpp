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

@app.route("/urcpp/v1/faculty/checkBNumber/<bnumber>", methods = ["POST"])
def faculty_checkBNumber (bnumber):
  # We are assuming BNumbers are less than 10 characters
  if (len(bnumber) < 10) and (bnumber.find("B") == 0):
    facQ = (LDAPFaculty.select()
      .where (LDAPFaculty.bnumber == bnumber)
      )
    if facQ.exists():
      return jsonify({ "response" : "OK" })
    else:
      return jsonify({ "response" : "NOTFOUND" })

