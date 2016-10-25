from api.everything import *
from api.faculty import getFaculty, getLDAPFaculty
from api.projects import getProject
from api.programs import getAllPrograms
from api.budget import getBudget
from api.parameters import getParameters

from api.pages import *

@app.route("/<username>/chair/manageCommittee", methods = ["GET"])
def manageCommittee_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
    
  parameters = getParameters()
  ldap = getLDAPFaculty(username)
  
  return render_template ("manageCommittee.html", 
                           username = username,
                           ldap = ldap,
                           params = parameters,
                           cfg = cfg,
                           )