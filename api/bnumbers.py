from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from collaborators import getCollaborators
from budget import getBudget

from pages import validPageTemplate

@app.route("/<username>/bnumbers", methods = ["POST"])
def bnumbers_POST (username):
  # TODO: We really need to fix this function. We can do much better.
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
    
  data = request.form
  numCollab = int(data["numCollab"])
  
  proj = getProject(username)
  
  # So we can do a remove...
  submittedBNumbers = []
  
  # Now, update the collaborators.
  for ndx in range(0, numCollab + 1):
    if ("cbnumber" + str(ndx)) in data:
      bnumber = data["cbnumber" + str(ndx)]
      submittedBNumbers.append(bnumber)
      app.logger.info("Looking for collaborator by BNumber: " + bnumber)
    
      # Start with my project. We have my username. That is the
      # proj object up above. Then, we need to find the
      # collaborators submitted by BNumber.
    
      collabQ = (LDAPFaculty.select()
        .where (LDAPFaculty.bnumber == bnumber)
        # Try and leave ourselves out of this...
        .where (LDAPFaculty.username != username)
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
  
  # Now, I want to remove everyone who isn't in the set of submitted
  # numbers. I'm confident there is a better way to do this.
  collabsQ = (Collaborators.select()
    .where (Collaborators.pID == proj.pID)
    )
    
  if collabsQ.exists():
    collabs = collabsQ.select()
    # Now, if any of these don't have a BNumber in the list
    # of submittedBNumbers, they need to go.
    
    for c in collabs:
      fac = c.username
      
      app.logger.info("fac is : " + str(m2d(fac)))
        
      # If their bnumber is not in my submitted list...
      if fac.bnumber not in submittedBNumbers:
        app.logger.info ("Deleting collaborator: " + fac.username)
        c.delete_instance()

  return redirect (  "/{0}/history".format(username) )

@app.route("/<username>/checkBNumber", methods = ["POST"])
def checkBNumber (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }

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

