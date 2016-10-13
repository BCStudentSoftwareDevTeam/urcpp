from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from collaborators import getCollaborators
from budget import getBudget

from pages import *

@app.route("/<username>/people", methods = ["GET"])
def people_GET (username):
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
  # Who knew... the collaborators all go through
  # as LDAPFaculty objects...
  collaborators = getCollaborators(username)
  budget = getBudget(username)
  
  return render_template (  "people.html",
                            proj = proj,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            ldap = ldapFaculty,
                            progs = programs,
                          )


@app.route("/<username>/people", methods = ["POST"])
def people_POST (username):
  user = AuthorizedUser()
  if not user.isAuthorized(username):
    return { "response": cfg["response"]["badUsername"] }
  if not user.canUpdateForm(username):
    return redirect("/")
    
  numStu    = int(request.form["numStu"])
  numCollab = int(request.form["numCollab"])
  
  app.logger.info("Found numStu '{0}' and numCollab '{1}' in POST"
                  .format(numStu, numCollab))
  
  # Update project
  proj = getProject(username)
  if proj is None:
    proj = Projects()
  
  proj.numberStudents = numStu
  proj.save()
  if numCollab > 0:
    return render_template (  "bnumbers.html",
                            username = username,
                            cfg = cfg,
                            numCollab = numCollab
                          )
  else:
    return redirect(username + "/history")
