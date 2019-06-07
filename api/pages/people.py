from api.everything import *
from ..API.projects import getProject
from ..API.collaborators import delete_all_collaborators, getCollaborators

@app.route("/people", methods = ["GET"])
def people_GET ():
  # All of our queries
  proj = getProject(g.user.username)
  
  if proj.status == cfg["projectStatus"]["Pending"]:
    flash("Application has already been submited.")
    return redirect(url_for("main_with_username", username = g.user.username))
    
  collabs = getCollaborators(g.user.username)
  
  
  return render_template (  "pages/people.html",
                            proj = proj,
                            username = g.user.username,
                            cfg = cfg,
                            ldap = g.user,
                            collabs = collabs
                          )