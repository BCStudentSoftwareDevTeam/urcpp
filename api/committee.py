from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from budget import getBudget
from parameters import getParameters

from pages import *



@app.route("/committee", methods = ["GET"])
@login_required
def committee_GET ():
  if not g.user.isCommitteeMember:
    abort(403)
  parameters = getParameters()
  ldap = getLDAPFaculty(g.user.username)
  
  return render_template ("committee.html", 
                           username = g.user.username,
                           ldap = ldap,
                           params = parameters,
                           cfg = cfg,

                           )