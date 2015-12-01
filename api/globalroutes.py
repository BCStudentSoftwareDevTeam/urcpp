from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from collaborators import getCollaborators
from budget import getBudget

from pages import *

# @app.route ("/s/<path:path>", methods = ["GET"])
# def templates (path):
#   return send_from_directory (path)

@app.route ("/t/<path:path>", methods = ["GET"])
def templates (path):
  return render_template ( path, 
                           username = os.getenv('USER'),
                           cfg = cfg
                        )

@app.route("/", methods = ["GET"])
def main ():
  username = os.getenv("USER")
  
  ldap = getLDAPFaculty(username)
  
  return render_template ("start.html", 
                           username = os.getenv('USER'),
                           ldap = ldap
                           )


@app.route("/<username>", methods = ["GET"])
def main_with_username (username):
  print "Going home"
  return redirect('/')