from api.everything import *
from projects import getProject
from collaborators import delete_non_collaborators, add_collaborators
from faculty import get_faculty_by_bnumbers

@app.route("/bnumbers", methods = ["POST"])
@login_required
def update_collaborators ():
  """This function updates the collaborators table

    Args:
      username (str): The username of the person accessing the app
      numCollab (str): POST number of collaborators project hasattr
      cnumber<index> (str): POST the collaborators c number; there maybe one or more of these
    
    Returns:
      Redirect: redirects to history_GET

    """ 
   
  proj = getProject(g.user.username)
  
  submitted_bnumbers = request.form.getlist("cbnumbers[]")
  
  add_collaborators(proj.pID, submitted_bnumbers)
          
          
  delete_non_collaborators(proj.pID, submitted_bnumbers)
  

  return redirect ( url_for( "history_GET" ))
  

@app.route("/checkBNumber", methods = ["POST"])
@login_required
def checkBNumber():
  """This function checks to see if a bnumber exists.
     It checks the LDAPFaculty table and if finds a User 
     it marks the bnum as good.
      Args:
        username (str): the user who is currently accessing the application
        bnum (str): POST the number that needs to be checked
       
      Returns:python
        JSON: response that is either OK or NOTFOUND
  """
  bnumber = request.json['bnum']
  if bnumber[0] == "b":
    bnumber = "B" + bnumber[1:]
    print ("Replaced Bnum: " + bnumber)
  # We are assuming BNumbers are less than 10 characters
  
  if (len(bnumber) < 12) and (bnumber.find("B") == 0):
    facQ = (LDAPFaculty.select()
      .where (LDAPFaculty.bnumber == bnumber)
      )
    if facQ.exists() and (bnumber != "B00000000"):
      if facQ[0].username == g.user.username:
        return jsonify({ "response" : "USER" })
      else:
        return jsonify({"response" : "OK"})
    else:
      if facQ.exists() and (bnumber == "B00000000"):
        return jsonify({ "response" : "ZERO" })
  else:
    return jsonify({ "response" : "NOTFOUND" })
   
   
   
   
   
   # return jsonify({ "response" : "ZERO" })
