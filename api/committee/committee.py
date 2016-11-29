from ..everything import *
from ..API.parameters import getParameters

from ..pages import *



@app.route("/committee", methods = ["GET"])
@login_required
def committee_GET ():
  if not g.user.isCommitteeMember:
    abort(403)
  parameters = getParameters()
  
  return render_template ("committee.html", 
                           username = g.user.username,
                           ldap = g.user,
                           params = parameters,
                           cfg = cfg,

                           )