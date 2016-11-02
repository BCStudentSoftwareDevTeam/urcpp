from everything import *
from faculty import getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from collaborators import getCollaborators
from pages.budget import getBudget
from pages import *
from applicationCycle import getCurrentCycle
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



@app.route("/", methods = ["GET"])
@login_required
def main ():
  ldap = getLDAPFaculty(g.user.username)
  project = getProject(g.user.username)
  currentCycle = getCurrentCycle()
  today = datetime.now()

  return render_template ("start.html", 
                           username = g.user.username,
                           ldap = ldap,
                           proj = project,
                           cfg = cfg,
                           currentCycle = currentCycle,
                           today = today
                           )
                          

@app.route("/<username>", methods = ["GET"])
@login_required
def main_with_username (username):
  print "Going home"
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
