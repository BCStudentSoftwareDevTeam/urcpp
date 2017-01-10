from api.everything import *
from ..API.projects import getProject, getProjectByID
from budget import getBudget
from ..API.parameters import getParameters
from ..API.collaborators import getCollaborators, getCollaboratorsByProjectId

from upload import checkForFile


@app.route("/done", methods = ["GET"])
@login_required
def done_GET ():
   # All of our queries
  proj = getProject(g.user.username)
  # TODO change budg to project.bID... in done.html will remove this line
  budget = getBudget(g.user.username)
  parameters = getParameters()
  collaborators = getCollaborators(g.user.username)
  uploadedFiles = [];
  
  if not proj.status == cfg["projectStatus"]["incomplete"]:
    return redirect(url_for("main"))
  
  for files in cfg["filepaths"]["allowedFileNames"]:
    if checkForFile != "":
      uploadedFiles.append(checkForFile(g.user.username, files, parameters.year))
   
  return render_template (  "done.html",
                            proj = proj,
                            cfg = cfg,
                            ldap = g.user,
                            budg = budget,
                            uploadedFiles = uploadedFiles,
                            params = parameters,
                            collabs = collaborators,
                            username = g.user.username
                          )


@app.route("/finalize", methods = ["POST"])
@login_required
def finalize_POST ():
  
  proj = getProject(g.user.username)
  proj.status = cfg["projectStatus"]["pending"]
  proj.save()
  
  return redirect('/')


@app.route("/review", methods = ["GET"])
@login_required
def review_GET ():
  proj = getProject(g.user.username)
  budget = getBudget(g.user.username)
  parameters = getParameters()
  collaborators = getCollaborators(g.user.username)
  uploadedFiles = [];
  
  # TODO: I don't think this is being used, keeping it for now, but need to check
  # if it is removed
  if request.referrer:
    previous_url = request.referrer
  else:
    previous_url = "/"
  
  for files in cfg["filepaths"]["allowedFileNames"]:
    if checkForFile != "":
      uploadedFiles.append(checkForFile(g.user.username, files, parameters.year))
    
  return render_template (  "projectView.html",
                            proj = proj,
                            cfg = cfg,
                            uploadedFiles = uploadedFiles,
                            params = parameters,
                            collabs = collaborators,
                            previous_url = previous_url,
                            ldap = g.user
                          )

# TODO: move outside of this file. It is an API endpoint
@app.route("/urcpp/v1/project/<pID>/<username>/<year>", methods = ["GET"])
@login_required
def project_GET (pID, username, year):
  # TODO: add check to see if user seeing this is a committee member
  
   # All of our queries
  proj = getProjectByID(pID)
  # TODO: get cycle instead
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
                            uploadedFiles = uploadedFiles,
                            params = parameters,
                            collabs = collaborators,
                            previous_url = previous_url
                          )
