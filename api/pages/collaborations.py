from api.everything import *
from ..API.projects import getProject
from ..API.collaborators import *
from ..API.faculty import *


@app.route("/collaborations", methods = ["POST"])
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
    
  proj.numberStudents = numStu
  proj.save()
  if numCollab > 0:
    collabs = getCollaborators(g.user.username)
    return render_template ("pages/collaborations.html",
                            username = g.user.username,
                            cfg = cfg,
                            numCollab = numCollab,
                            collabs = collabs
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
  
  submitted_usernames = request.form.getlist("username[]") #This shall be our test function
  
  add_collaborators(proj.pID, submitted_usernames)
          
          
  delete_non_collaborators(proj.pID, submitted_usernames)
  

  return redirect ( url_for( "irbyn_GET" ))

@app.route("/check_username", methods = ["POST"])
@login_required
def check_username():
  """This function checks to see if a bnumber exists.
     It checks the LDAPFaculty table and if finds a User 
     it marks the bnum as good.
      Args:
        username (str): the user who is currently accessing the application
        bnum (str): POST the number that needs to be checked
       
      Returns:
        JSON: response that is either OK or NOTFOUND
  """
  username = request.json['u_name']
  #if bnumber[0] == "b":
   # bnumber = "B" + bnumber[1:]
  #  print ("Replaced Bnum: " + bnumber)
  # We are assuming BNumbers are less than 10 characters
  if (len(bnumber) < 12) and (bnumber.find("B") == 0):
    facQ = (LDAPFaculty.select()
      .where (LDAPFaculty.bnumber == bnumber)
      )
    if facQ.exists():
      if facQ[0].username == g.user.username:
        return jsonify({"response" : "USER"})
      return jsonify({ "response" : "OK" })
    else:
      return jsonify({ "response" : "NOTFOUND" })
  else:
    return jsonify({ "response" : "NOTFOUND" })