from api.everything import *
from api.parameters import getParameters

from api.pages import *



@app.route("/committee", methods = ["GET"])
@login_required
def committee_GET ():
  if not g.user.isCommitteeMember:
    abort(403)
  parameters = getParameters()
  ldap = getLDAPFaculty(g.user.username)
  
  return render_template ("committee.html", 
                           username = g.user.username,
                           ldap = g.user,
                           params = parameters,
                           cfg = cfg,

                           )