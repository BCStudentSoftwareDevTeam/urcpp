from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from budget import getBudget

from pages import *


@app.route("/irbyn", methods = ["GET"])
@login_required
def irbyn_GET ():
  # All of our queries
  proj = getProject(g.user.username)
  
  if proj.status == cfg["projectStatus"]["pending"]:
    return redirect(url_for("main"))
  
  return render_template (  "irbyn.html",
                            proj = proj,
                            username = g.user.username,
                            cfg = cfg,
                            ldap = g.user,
                          )

@app.route("/irbyn", methods = ["POST"])
@login_required
def irbyn_POST ():
  
  proj = getProject(g.user.username)
  
  if proj.status == cfg["projectStatus"]["pending"]:
    return redirect(url_for("main"))
  proj.humanSubjects = (1 if request.form["irb"] == "Yes" else 0 )
  proj.save()
  
  if proj.humanSubjects:
    return redirect(url_for("generic_file_upload", uploadType = "irb"))
  else:
    return redirect(url_for("generic_file_upload", uploadType = 'vitae'))
