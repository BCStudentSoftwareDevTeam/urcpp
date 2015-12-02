from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from budget import getBudget

from pages import *

@app.route("/<username>/committee", methods = ["GET"])
def committee_GET (username):
  username = os.getenv("USER")
  
  ldap = getLDAPFaculty(username)
  
  return render_template ("committee.html", 
                           username = os.getenv('USER'),
                           ldap = ldap
                           )