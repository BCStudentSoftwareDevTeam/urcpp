
from api.flask_imports import *

from ..everything import cfg
from api.models import *
from ..API.projects import getProject
from ..API.collaborators import delete_all_collaborators, getCollaborators

from api.pages import pages

@pages.route("/people", methods = ["GET"])
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


@pages.route("/people", methods = ["POST"])
def people_POST ():

  numStu    = int(request.form["numStu"])
  numCollab = int(request.form["numCollab"])

  current_app.logger.info("Found numStu '{0}' and numCollab '{1}' in POST"
                  .format(numStu, numCollab))

  # Update project
  proj = getProject(g.user.username)


  # should we really be trying to create a project here?
  if proj is None:
    proj = Projects()

  if proj.status == cfg["projectStatus"]["Pending"]:
    flash("Application has already been submitted.")
    return redirect(url_for("main_with_username", username = g.user.username))

  proj.numberStudents = numStu
  proj.save()
  if numCollab > 0:
    collabs = getCollaborators(g.user.username)
    return render_template (  "pages/bnumbers.html",
                            username = g.user.username,
                            cfg = cfg,
                            numCollab = numCollab,
                            collabs = collabs
                          )
  else:
    delete_all_collaborators(proj.pID)
    return redirect(url_for('pages.history_GET'))
