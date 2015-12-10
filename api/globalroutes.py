from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from collaborators import getCollaborators
from budget import getBudget
from pages import *

import pprint

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
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  # print(pprint.pformat (request.environ, depth = 5))
  
  ldap = getLDAPFaculty(username)
  project = getProject(username)
  
  return render_template ("start.html", 
                           username = username,
                           ldap = ldap,
                           proj = project
                           )
@app.route("/<username>", methods = ["GET"])
def main_with_username (username):
  print "Going home"
  return redirect('/')