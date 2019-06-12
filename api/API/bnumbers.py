# This file probably won't be used anymore. There is a chance it will be deleted by the time that Bria and Hailey are done with it. However, just to be safe, we are going to document it now.

from api.everything import *
from projects import getProject
from collaborators import delete_non_collaborators, add_collaborators
from faculty import get_faculty_by_bnumbers


@app.route("/bnumbers", methods = ["POST"]) # reroutes to the /bnumbers page
@login_required  # requires user to be logged in, cannot access straight from URL without being logged in
def update_collaborators ():
  """This function updates the collaborators table in the database

    Args:
      username (str): The username of the person accessing the app (user)
      numCollab (str): POST number of collaborators project hasattr
      cnumber<index> (str): POST the collaborators c number; there maybe one or more of these
    
    Returns:
      Redirect: redirects to history_GET

    """ 
   
  proj = getProject(g.user.username) # gets project in current year associated with the person who is accessing the app (user), see projects.py
  
  submitted_bnumbers = request.form.getlist("cbnumbers[]") # creates a list of collaborator B# to be submitted to database
  
  add_collaborators(proj.pID, submitted_bnumbers) # add collabs to database by using the pID and B# entered
          
  delete_non_collaborators(proj.pID, submitted_bnumbers) # deletes all collabs from database with that project ID who are not included in the submittedB#
  
  return redirect ( url_for( "history_GET" )) # redirects to page /history - this page has been deleted #oops


@app.route("/checkBNumber", methods = ["POST"])
@login_required
def checkBNumber():
  """This function checks to see if a bnumber exists.
     It checks the LDAPFaculty table and if finds a User it marks the bnum as good.
      Args:
        username (str): the user who is currently accessing the application
        bnum (str): POST the number that needs to be checked
       
      Returns:
        JSON: response that is either OK or NOTFOUND
  """
  bnumber = request.json['bnum']
  if bnumber[0] == "b":              # this if statement checks to make sure the "B" in the bnumber is capitalized
    bnumber = "B" + bnumber[1:] 
    print ("Replaced Bnum: " + bnumber)
  # we are assuming bnumbers are less than 12 characters
  if (len(bnumber) < 12) and (bnumber.find("B") == 0): 
    facQ = (LDAPFaculty.select() # this gets the bnumbers of the faculty members that are entered into the input box
      .where (LDAPFaculty.bnumber == bnumber) 
      )
    if facQ.exists():
      if facQ[0].username == g.user.username:
        return jsonify({"response" : "USER"}) # this js error pops up if the Bnumber belongs to the user who is logged in
      return jsonify({ "response" : "OK" }) # this response shows that bnumber is recognized by the database
    else:
      return jsonify({ "response" : "NOTFOUND" }) # this error shows if the faculty member does not exist
  else:
    return jsonify({ "response" : "NOTFOUND" }) # this error shows if the bnumber entered is too long or too short
   
   
