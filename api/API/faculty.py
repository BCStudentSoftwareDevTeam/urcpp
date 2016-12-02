from ..everything import *
import json
import projects

def getLDAPFaculty (username):
    
  ldapQ = (LDAPFaculty.select()
    .where (LDAPFaculty.username == username)
    )
  
  if ldapQ.exists():
    return ldapQ.get()
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
    
def getFacultyByYear (username, year):
  facQ = (URCPPFaculty.select().join(Projects)
    .where (URCPPFaculty.username == username)
    .where (Projects.year == year)
    )

  if facQ.exists():
    return facQ.get()
  else:
    return None


def getFacultyWithProjects (year):
  facQ = (URCPPFaculty.select().join(Projects).where(Projects.year == year))

  if facQ.exists():
    return facQ.execute()
  else:
    return None


def getFacultyWithPendingProjects ():
  facQ = (URCPPFaculty.select()
                        .join(Projects)
                        .where(Projects.status == cfg["projectStatus"]["pending"])
                        .where(Projects.pID == URCPPFaculty.pID)
                        )

  if facQ.exists():
    return facQ.execute()
  else:
    return None
    
def getFacultyForProject (pid):
  facQ =  ( URCPPFaculty.select()
                        .where(URCPPFaculty.pID == pid)
          )
  if facQ.exists():
    return facQ.get()
  else:
    return None

def getFacultyWithAcceptedProjects():
  facQ = ( URCPPFaculty.select()
                        .join(Projects)
                        .where(Projects.status == cfg["projectStatus"]["accept"])
          )
  if facQ.exists():
    return facQ.execute()
  else:
    return None

def getFacultyWithRejectedProjects():
  facQ = ( URCPPFaculty.select()
                        .join(Projects)
                        .where(Projects.status == cfg["projectStatus"]["reject"])
          )
  if facQ.exists():
    return facQ.execute()
  else:
    return None
    
@app.route("/urcpp/v1/faculty/get/<username>", methods = ["POST"])
def faculty_get (username):
  if username != authUser(request.environ):
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

