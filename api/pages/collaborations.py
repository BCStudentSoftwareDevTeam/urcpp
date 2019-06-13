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
  #(request.form["getCollabUsernames"]) # only gets one collab #1?
  print(newCollab)
  # request.data.getlist("getCollabUsernames") # gets the data from the form
  # TODO: Insert the collaborators to the DB for this PID
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


@login_required
def update_collaborators ():
  """This function updates the collaborators table

    Args:
      username (str): The username of the person accessing the app
      numCollab (str): POST number of collaborators project hasattr
      cnumber<index> (str): POST the collaborators c number; there maybe one or more of these
    
    Returns:
      Redirect: redirects to irbyn_GET

    """ 
   
  proj = getProject(g.user.username)
  
  submitted_usernames = request.form.getlist("username[]") 
  
  add_collaborators(proj.pID, submitted_usernames)
          
  delete_non_collaborators(proj.pID, submitted_usernames)
  
  return redirect ( url_for( "irbyn_GET" ))
  

@app.route("/check_username", methods = ["POST"])
@login_required
def check_username():
  """This function checks to see if a username  exists.
     It checks the LDAPFaculty table and if finds a User 
     it marks the u_num  as good.
      Args:
        username (str): the user who is currently accessing the application
        u_num (str): POST the username that needs to be checked
       
      Returns:
        JSON: response that is either OK or NOTFOUND
  """
  username = request.json['u_name']

  facQ = (LDAPFaculty.select())
  
  if facQ.exists():
    if facQ[0].username == g.user.username:
      return jsonify({"response" : "USER"})
    return jsonify({ "response" : "OK" })
  else:
    return jsonify({ "response" : "NOTFOUND" })