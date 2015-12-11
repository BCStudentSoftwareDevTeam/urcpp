from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from budget import getBudget
from parameters import getParameters

from pages import *

@app.route("/<username>/committee", methods = ["GET"])
def committee_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  parameters = getParameters()
  ldap = getLDAPFaculty(username)
  
  return render_template ("committee.html", 
                           username = username,
                           ldap = ldap
                           )