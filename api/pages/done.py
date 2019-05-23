from api.everything import *
from ..API.projects import getProject, getProjectByID
from budget import getBudget
from ..API.parameters import getCurrentParameters
from ..API.collaborators import getCollaborators, getCollaboratorsByProjectId
from ..API.faculty import getFacultyForProject
from api.models import *
from upload import checkForFile


@app.route("/done", methods = ["GET"])
@login_required
def done_GET ():
   # All of our queries
  proj = getProject(g.user.username)
  parameters = getCurrentParameters()
  collaborators = getCollaboratorsByProjectId(proj.pID)
  faculty = URCPPFaculty.get(URCPPFaculty.pID == proj.pID)
  uploadedFiles = [];
  
  if proj.status == cfg["projectStatus"]["Pending"]:
    flash("Application has already been submitted.")
    return redirect(url_for("main_with_username", username = g.user.username))
  
  for files in cfg["filepaths"]["allowedFileNames"]:
    if checkForFile != "":
      uploadedFiles.append(checkForFile(g.user.username, files, parameters.year))
   
  return render_template (  "pages/done.html",
                            proj = proj,
                            cfg = cfg,
                            ldap = g.user,
                            uploadedFiles = uploadedFiles,
                            params = parameters,
                            collabs = collaborators,
                            username = g.user.username,
                            faculty = faculty
                          )


@app.route("/finalize", methods = ["POST"])
@login_required
def finalize_POST ():
  
  proj = getProject(g.user.username)
  proj.status = cfg["projectStatus"]["Pending"]
  proj.save()
  flash("Application has been submitted." , "success")
  return redirect('/')


@app.route("/review", methods = ["GET"])
@login_required
def review_GET ():
  proj = getProject(g.user.username)
  budget = getBudget(g.user.username)
  parameters = getCurrentParameters()
  collaborators = getCollaboratorsByProjectId(proj.pID)
  faculty = URCPPFaculty.get(URCPPFaculty.pID == proj.pID)
  
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
    
  return render_template (  "pages/projectView.html",
                            proj = proj,
                            cfg = cfg,
                            uploadedFiles = uploadedFiles,
                            params = parameters,
                            collabs = collaborators,
                            previous_url = previous_url,
                            ldap = g.user,
                            username = g.user.username,
                            faculty = faculty
                          )

@app.route("/urcpp/v1/project/<pID>/<username>/<year>", methods = ["GET"])
@login_required
def project_GET (pID, username, year):
  if not current_user.isCommitteeMember:
    abort(403)
   # All of our queries
  proj = getProjectByID(pID)
  parameters = getCurrentParameters()
  collaborators = getCollaboratorsByProjectId(pID)
  uploadedFiles = [];

  if request.referrer:
    previous_url = request.referrer
  else:
    previous_url = "/"
  
  for files in cfg["filepaths"]["allowedFileNames"]:
    if checkForFile != "":
      uploadedFiles.append(checkForFile(username, files, year))
    
  return render_template (  "pages/projectView.html",
                            proj = proj,
                            cfg = cfg,
                            uploadedFiles = uploadedFiles,
                            params = parameters,
                            collabs = collaborators,
                            previous_url = previous_url,
                            username=username
                          )
