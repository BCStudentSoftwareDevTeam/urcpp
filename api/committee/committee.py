from ..everything import *
from ..API.parameters import getCurrentParameters

from ..pages import *



@app.route("/committee", methods = ["GET"])
@login_required
def committee_GET ():
  if not g.user.isCommitteeMember:
    abort(403)
  parameters = getCurrentParameters()
  
  return render_template ("committee/committee.html", 
                           username = g.user.username,
                           ldap = g.user,
                           params = parameters,
                           cfg = cfg,

                           )