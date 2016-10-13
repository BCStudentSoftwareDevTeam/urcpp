from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject, getProjectByID
from programs import getAllPrograms
from budget import getBudget
from parameters import getParameters
from collaborators import getCollaborators, getCollaboratorsById

from pages import *
from upload import checkForFile

@app.route("/<username>/done", methods = ["GET"])
def done_GET (username):
  user = AuthorizedUser()
  if not user.isAuthorized(username):
    return { "response": cfg["response"]["badUsername"] }
  if not user.canUpdateForm(username):
    return redirect("/")
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
      uploadedFiles.append(checkForFile(username, files, parameters.year))
    
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
  user = AuthorizedUser()
  if not user.isAuthorized(username):
    return { "response": cfg["response"]["badUsername"] }
  
  proj = getProject(username)
  proj.status = cfg["projectStatus"]["pending"]
  proj.save()
  
  return redirect('/')

@app.route("/<username>/review", methods = ["GET"])
def review_GET (username):
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
  
  if request.referrer:
    previous_url = request.referrer
  else:
    previous_url = "/"
  
  for files in cfg["filepaths"]["allowedFileNames"]:
    if checkForFile != "":
      uploadedFiles.append(checkForFile(username, files, parameters.year))
    
  return render_template (  "projectView.html",
                            proj = proj,
                            cfg = cfg,
                            progs = programs,
                            uploadedFiles = uploadedFiles,
                            params = parameters,
                            collabs = collaborators,
                            previous_url = previous_url
                          )

@app.route("/urcpp/v1/project/<pID>/<username>/<year>", methods = ["GET"])
def project_GET (pID, username, year):
  user = AuthorizedUser()
  if not user.isAuthorized(username):
    return { "response": cfg["response"]["badUsername"] }
   # All of our queries
  proj = getProjectByID(pID)
  programs = getAllPrograms()
  parameters = getParameters()
  collaborators = getCollaboratorsById(pID)
  uploadedFiles = [];

  if request.referrer:
    previous_url = request.referrer
  else:
    previous_url = "/"
  
  for files in cfg["filepaths"]["allowedFileNames"]:
    if checkForFile != "":
      uploadedFiles.append(checkForFile(username, files, year))
    
  return render_template (  "projectView.html",
                            proj = proj,
                            cfg = cfg,
                            progs = programs,
                            uploadedFiles = uploadedFiles,
                            params = parameters,
                            collabs = collaborators,
                            previous_url = previous_url
                          )
