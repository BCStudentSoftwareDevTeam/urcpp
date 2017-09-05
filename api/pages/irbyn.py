from api.everything import *
from ..API.projects import getProject


@app.route("/irbyn", methods = ["GET"])
@login_required
def irbyn_GET ():
  # All of our queries
  proj = getProject(g.user.username)
  
  if proj.status == cfg["projectStatus"]["Pending"]:
    return redirect(url_for("main_with_username", username = g.user.username))
  
  return render_template (  "pages/irbyn.html",
                            proj = proj,
                            username = g.user.username,
                            cfg = cfg,
                            ldap = g.user,
                          )

@app.route("/irbyn", methods = ["POST"])
@login_required
def irbyn_POST ():
  
  proj = getProject(g.user.username)
  
  if proj.status == cfg["projectStatus"]["Pending"]:
    return redirect(url_for("main_with_username", username = g.user.username))
    
  proj.humanSubjects = (1 if request.form["irb"] == "Yes" else 0 )
  proj.save()
  
  if proj.humanSubjects:
    return redirect(url_for("generic_file_upload", uploadType = "irb"))
  else:
    return redirect(url_for("generic_file_upload", uploadType = 'vitae'))
