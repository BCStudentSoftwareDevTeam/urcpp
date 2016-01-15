from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from budget import getBudget
from parameters import getParameters
from collaborators import getCollaborators

from pages import *
from upload import checkForFile

@app.route("/<username>/done", methods = ["GET"])
def done_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
   # All of our queries
  faculty = getFaculty(username)
  ldapFaculty = getLDAPFaculty(username)
  proj = getProject(username)
  programs = getAllPrograms()
  budget = getBudget(username)
  parameters = getParameters()
  collaborators = getCollaborators(username)
  uploadedFiles = [];
  
  for files in cfg["filepaths"]["allowedFileNames"]:
    if checkForFile != "":
      uploadedFiles.append(checkForFile(username, files))
    
  return render_template (  "done.html",
                            proj = proj,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            ldap = ldapFaculty,
                            progs = programs,
                            budg = budget,
                            uploadedFiles = uploadedFiles,
                            params = parameters,
                            collabs = collaborators,
                          )


@app.route("/<username>/finalize", methods = ["POST"])
def finalize_POST (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  proj = getProject(username)
  proj.status = cfg["projectStatus"]["pending"]
  proj.save()
  
  return redirect('/')