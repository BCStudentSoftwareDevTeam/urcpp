from api.everything import *
from api.API.faculty import getLDAPFaculty
from api.API.projects import getProject
from api.API.programs import getAllPrograms
from api.API.collaborators import getCollaborators
from api.pages.budget import getBudget
from api.pages import *
from api.API.parameters import getCurrentParameters
from datetime import datetime
import pprint


@app.route ("/s/<path:path>", methods = ["GET"])
@login_required
def statics (path):
  return app.send_static_file (path)

@login_required
@app.route ("/t/<path:path>", methods = ["GET"])
def templates (path):
  return render_template ( path, 
                           username = g.user.username,
                           cfg = cfg
                        )



#@app.route("/old_start", methods = ["GET"])
#@login_required
#def main ():
#  ldap = getLDAPFaculty(g.user.username)
#  project = getProject(g.user.username)
#  currentCycle = getCurrentParameters()
#  today = datetime.now()
#
#  return render_template ("start.html", 
#                           username = g.user.username,
#                           ldap = ldap,
#                           proj = project,
#                           cfg = cfg,
#                           currentCycle = currentCycle,
#                           today = today
#                           )
                          

@app.route("/<username>", methods = ["GET"])
@login_required
def main_with_username (username):
  return redirect('/')


# Tests the application's liveness
@app.route("/ping", methods = ["GET", "POST"])
def ping ():
  return jsonify({"response" : "OK"})


# Tests the application's database response  
@app.route("/stress", methods = ["GET", "POST"])
def stress ():
  ldap = getLDAPFaculty("heggens")
  if ldap is not None:
    return jsonify({"response" : "OK"})
  else:
    return jsonify({"response" : "NOTFOUND"})
