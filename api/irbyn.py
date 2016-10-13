from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from budget import getBudget

from pages import *

@app.route("/<username>/irbyn", methods = ["GET"])
def irbyn_GET (username):
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
  
  return render_template (  "irbyn.html",
                            proj = proj,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            ldap = ldapFaculty,
                            progs = programs,
                          )

# Sets the flag in the DB for IRB, and redirects to upload page.
@app.route("/<username>/irbyn", methods = ["POST"])
def irbyn_POST (username):
  user = AuthorizedUser()
  if not user.isAuthorized(username):
    return { "response": cfg["response"]["badUsername"] }
  if not user.canUpdateForm(username):
    return redirect("/")
  
  proj = getProject(username)
  proj.humanSubjects = (1 if request.form["irb"] == "Yes" else 0 )
  proj.save()
  
  if proj.humanSubjects:
    return redirect(username + '/upload/irb')
  else:
    return redirect(username + '/upload/vitae')
