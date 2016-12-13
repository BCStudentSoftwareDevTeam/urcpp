from api.everything import *
from projects import getProject
from collaborators import delete_non_collaborators

@app.route("/bnumbers", methods = ["POST"])
@login_required
def bnumbers_POST (username):
  """This function updates the collaborators table

    Args:
      username (str): The username of the person accessing the app
      numCollab (str): POST number of collaborators project hasattr
      cnumber<index> (str): POST the collaborators c number; there maybe one or more of these
    
    Returns:
      Redirect: redirects to history_GET

    """ 
  post_variables = request.form
  number_of_collaborators = int(post_variables["numCollab"])
  
  proj = getProject(g.user.username)
  
  # So we can do a remove...
  submittedBNumbers = []
  
  # Now, update the collaborators.
  for ndx in range(0, number_of_collaborators + 1):
    if ("cbnumber" + str(ndx)) in post_variables:
      bnumber = post_variables["cbnumber" + str(ndx)]
      submittedBNumbers.append(bnumber)
      app.logger.info("Looking for collaborator by BNumber: " + bnumber)
    
      # Start with my project. We have my username. That is the
      # proj object up above. Then, we need to find the
      # collaborators submitted by BNumber.
    
      collabQ = (LDAPFaculty.select()
        .where (LDAPFaculty.bnumber == bnumber)
        # Try and leave ourselves out of this...
        .where (LDAPFaculty.username != g.user.username)
        )
      
      # We now have my full info if this exists. That means that 
      # a correct BNumber was entered into the field.
      if collabQ.exists():
        app.logger.info ("Found them!")
        # Now, we have their full info.
        collabFac = collabQ.get()
        app.logger.info("collabFac.username is : " + collabFac.username)
        
        # At this point, we need to see if they're in
        # the Collaborators table already.
        centryQ = (Collaborators.select()
          .where (Collaborators.username == collabFac.username)
          .where (Collaborators.pID == proj.pID)
          )
        
        # If they're in the table, we don't want to
        # do anything. If they're not, we do.
        if not centryQ.exists():
          c = Collaborators()
          c.username = collabFac.username
          c.pID = proj.pID
          # And, save.
          c.save()
  # I think this is better
  
  delete_non_collaborators(submittedBNumbers, proj.pID)
  

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
       
      Returns:
        JSON: response that is either OK or NOTFOUND
  """
  bnumber = request.json['bnum']
  print bnumber
  if bnumber[0] == "b":
    bnumber = "B" + bnumber[1:]
    print ("Replaced Bnum: " + bnumber)
  # We are assuming BNumbers are less than 10 characters
  if (len(bnumber) < 12) and (bnumber.find("B") == 0):
    facQ = (LDAPFaculty.select()
      .where (LDAPFaculty.bnumber == bnumber)
      )
    if facQ.exists():
      return jsonify({ "response" : "OK" })
    else:
      return jsonify({ "response" : "NOTFOUND" })
  else:
    return jsonify({ "response" : "NOTFOUND" })
   
   
