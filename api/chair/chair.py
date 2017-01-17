from ..everything import *
from ..API.faculty import getFacultyWithAcceptedProjects, getFacultyWithRejectedProjects
from ..API.parameters import getCurrentParameters

from ..pages import *

@app.route("/chair", methods = ["GET"])
@login_required
def chair_GET ():
  if not g.user.isChair:
    abort(403)
    
  parameters = getCurrentParameters()
  
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
  
  return render_template ("pages/chair.html", 
                           username = g.user.username,
                           ldap = g.user,
                           params = parameters,
                           cfg = cfg,
                           acceptedFacultyEmail = acceptedFacultyEmail,
                           rejectedFacultyEmail = rejectedFacultyEmail
                           )