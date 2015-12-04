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
  username = authUser(request.environ)

  # print(pprint.pformat (request.environ, depth = 5))
  
  ldap = getLDAPFaculty(username)
  
  return render_template ("start.html", 
                           username = username,
                           ldap = ldap
                           )

# This looks like file upload, but it isn't.
# This renders a "generic" upload page, where the upload type
# is one of three types. The page configures itself based 
# on the type of upload being requested.
@app.route("/<username>/upload/<uploadType>", methods = ["GET"])
def generic_file_upload (username, uploadType):
  if uploadType in cfg["filepaths"]["allowedFileNames"]:
    # All of our queries
    faculty = getFaculty(username)
    ldapFaculty = getLDAPFaculty(username)
    proj = getProject(username)
    programs = getAllPrograms()
    collaborators = getCollaborators(username)
    budget = getBudget(username)
    
    
    return render_template (  "upload.html",
                              proj = proj,
                              username = username,
                              cfg = cfg,
                              fac = faculty,
                              ldap = ldapFaculty,
                              uploadType = uploadType
                            )
  else:
    return "File upload type not recognized."
