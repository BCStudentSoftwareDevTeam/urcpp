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

def getLDAPFaculty (username):
    
  ldapQ = (LDAPFaculty.select()
    .where (LDAPFaculty.username == username)
    )
  
  if ldapQ.exists():
    ldap = ldapQ.get()
    return ldap
  else:
    return None
  

def getFaculty (username):
  facQ = (URCPPFaculty.select()
    .where (URCPPFaculty.username == username)
    )

  if facQ.exists():
    fac  = facQ.get()
    return facQ.get()
  else:
    return None
    
@app.route("/urcpp/v1/faculty/get/<username>", methods = ["POST"])
def faculty_get (username):
  if username != os.getenv("USER"):
    return { "response": cfg["response"]["badUsername"] }
  
  fac = getFaculty(username)  
  ldap = getLDAPFaculty(username)
  
  if fac and ldap:
    response = {  "response" : "OK" }
    response["faculty"] = m2d(fac)
    response["details"] = m2d(ldap)
    return jsonify(response)
  else:
    response = { "response": cfg["response"]["noResults"],
                 "details": "No faculty found for username {0}.".format(username)
                 }
    return jsonify(response)  

