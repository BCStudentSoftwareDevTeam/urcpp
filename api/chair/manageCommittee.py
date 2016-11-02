from api.everything import *
from api.parameters import getParameters

from api.pages import *

@app.route("/<username>/chair/manageCommittee", methods = ["GET"])
@login_required
def manageCommittee_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
    
  parameters = getParameters()
  return render_template ("manageCommittee.html", 
                           username = username,
                           ldap = g.user,
                           params = parameters,
                           cfg = cfg,
                           )