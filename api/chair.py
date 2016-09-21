from everything import *
from faculty import getFaculty, getLDAPFaculty, getFacultyWithAcceptedProjects, getFacultyWithRejectedProjects
from projects import getProject
from programs import getAllPrograms
from budget import getBudget
from parameters import getParameters

from pages import *

@app.route("/<username>/chair", methods = ["GET"])
def chair_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
    
  parameters = getParameters()
  ldap = getLDAPFaculty(username)
  
  acceptedFaculty = getFacultyWithAcceptedProjects()
  acceptedFacultyEmail = ""
  if acceptedFaculty is not None:
    for fac in acceptedFaculty:
      acceptedFacultyEmail += "{}@berea.edu;".format(fac.username.username)
      
  rejectedFaculty = getFacultyWithRejectedProjects()
  rejectedFacultyEmail = ""
  if rejectedFaculty is not None:
    for fac in rejectedFaculty:
      rejectedFacultyEmail += "{}@berea.edu;".format(fac.username.username)
  
  return render_template ("chair.html", 
                           username = username,
                           ldap = ldap,
                           params = parameters,
                           cfg = cfg,
                           acceptedFacultyEmail = acceptedFacultyEmail,
                           rejectedFacultyEmail = rejectedFacultyEmail
                           )