from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from collaborators import getCollaborators
from budget import getBudget
from pages import *
from applicationCycle import getCurrentCycle
from datetime import datetime
import pprint
from authTool import AuthorizedUser


@app.route ("/s/<path:path>", methods = ["GET"])
def statics (path):
  return app.send_static_file (path)

@app.route ("/t/<path:path>", methods = ["GET"])
def templates (path):
  return render_template ( path, 
                           username = authUser(request.environ),
                           cfg = cfg
                        )


@app.route("/", methods = ["GET"])
def main ():
  authorizedUser = AuthorizedUser()
  username = authorizedUser.get_username()
  # print(pprint.pformat (request.environ, depth = 5))
  print username  
  ldap = getLDAPFaculty(username)
  project = getProject(username)
  currentCycle = getCurrentCycle()
  today = datetime.now()

  return render_template ("start.html", 
                           username = username,
                           ldap = ldap,
                           proj = project,
                           cfg = cfg,
                           currentCycle = currentCycle,
                           today = today
                           )
@app.route("/<username>", methods = ["GET"])
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
