from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from collaborators import getCollaborators
from budget import getBudget

from pages import *

@app.route("/people", methods = ["GET"])
def people_GET ():
  # All of our queries
  proj = getProject(g.user.username)
  
  if proj.status == cfg["projectStatus"]["pending"]:
    return redirect(url_for('main'))
  
  return render_template (  "people.html",
                            proj = proj,
                            username = g.user.username,
                            cfg = cfg,
                            ldap = g.user,
                          )


@app.route("/people", methods = ["POST"])
def people_POST ():
    
  numStu    = int(request.form["numStu"])
  numCollab = int(request.form["numCollab"])
  
  app.logger.info("Found numStu '{0}' and numCollab '{1}' in POST"
                  .format(numStu, numCollab))
  
  # Update project
  proj = getProject(g.user.username)
  
  
  # should we really be trying to create a project here?
  if proj is None:
    proj = Projects()
  
  if proj.status == cfg["projectStatus"]["pending"]:
    return redirect(url_for('main'))
    
  proj.numberStudents = numStu
  proj.save()
  if numCollab > 0:
    return render_template (  "bnumbers.html",
                            username = g.user.username,
                            cfg = cfg,
                            numCollab = numCollab
                          )
  else:
    return redirect(url_for('history_GET'))
