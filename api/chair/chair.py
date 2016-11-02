from api.everything import *
from api.faculty import getFacultyWithAcceptedProjects, getFacultyWithRejectedProjects
from api.parameters import getParameters

from api.pages import *

@app.route("/chair", methods = ["GET"])
@login_required
def chair_GET ():
  if not g.user.isChair:
    abort(403)
    
  parameters = getParameters()
  
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
                           username = g.user.username,
                           ldap = g.user,
                           params = parameters,
                           cfg = cfg,
                           acceptedFacultyEmail = acceptedFacultyEmail,
                           rejectedFacultyEmail = rejectedFacultyEmail
                           )