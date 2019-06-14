from api.everything import *
from ..API.projects import getProject
from ..API.collaborators import *
from ..API.faculty import getLDAPFaculty


@app.route("/insertcollaborators", methods = ["POST"])
@login_required
def insert_collaborators ():
  # endpoint for inserting collaborators from collaborations.html
  
  proj = getProject(g.user.username)
  newCollab = request.form.getlist("getCollabUsernames") #get all users but list includes 
  # print(newCollab)
  add_collaborators(proj.pID, newCollab)
  return redirect(url_for('irbyn_GET'))
  
  

@app.route("/collaborations", methods = ["POST"])
@login_required
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
  
  if proj.status == cfg["projectStatus"]["Pending"]:
    flash("Application has already been submitted.")
    return redirect(url_for("main_with_username", username = g.user.username))
    
  #Save the number of students to the project
  proj.numberStudents = numStu
  proj.save()
  
  # Get all the faculty for the dropdown
  allFaculty = LDAPFaculty.select().order_by(LDAPFaculty.username)
  
  if numCollab > 0:
    delete_all_collaborators(proj.pID)
    return render_template ("pages/collaborations.html",
                            username = g.user.username,
                            cfg = cfg,
                            numCollab = numCollab,
                            allFaculty = allFaculty
                          )
  else:
    delete_all_collaborators(proj.pID)
    return redirect(url_for('irbyn_GET'))