from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from budget import getBudget
from parameters import getParameters

from pages import *

@app.route("/<username>/chair/setParameters", methods = ["GET"])
def setParameters_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  parameters = getParameters()
  ldap = getLDAPFaculty(username)
  
  return render_template ("setParameters.html", 
                           username = username,
                           ldap = ldap,
                           params = parameters,
                           cfg = cfg,
                           )