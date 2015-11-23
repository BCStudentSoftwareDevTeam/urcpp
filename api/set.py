from everything import *
from projects import getProject
from faculty import getFaculty
from budget import getBudget

# FIXME: I'm pretty sure there are better ways to do almost 
# everything in here... probably some nice SQL ways to search
# better, etc. Also, I don't handle the case that someone
# got the BNumber wrong. The user can enter a bogus BNumber,
# and they have no idea it happened.
@app.route("/urcpp/v1/set/people/<username>", methods = ["POST"])
def set_people (username):
  if username != os.getenv("USER"):
    return { "response": cfg["response"]["badUsername"] }
  # Grab the .body() from the aja() POST
  data = request.get_json()
  
  # This is what our post from this page looks like
  # {cbnumber0: "B00660000", cname0: "Scott Heggen", numCollab: "1", numStu: "3"}
  
  app.logger.info("Setting people page: " + json.dumps(data))
  
  # We want to insert the number of students into the projects table,
  # and the collaborators into the collab table... if they don't 
  # already exist.
  
  # Update project
  proj = getProject(username)
  if proj is None:
    proj = Project()
  
  proj.numberStudents = data["numStu"]
  proj.save()
  
  # So we can do a remove...
  submittedBNumbers = []
  
  # Now, update the collaborators.
  for ndx in range(0, int(data["numCollab"])):
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
      # If their bnumber is not in my submitted list...
      if fac.bnumber not in submittedBNumbers:
        app.logger.info ("Deleting collaborator: " + fac.username)
        # FIXME: This is not deleting anything from the table.
        c.delete_instance()
      
  response = { "response" : "OK" }
  return jsonify(response)

@app.route("/urcpp/v1/set/create/<username>", methods = ["POST"])
def set_start (username):
  if username != os.getenv("USER"):
    return { "response": cfg["response"]["badUsername"] }

  # Grab the .body() from the aja() POST
  data = request.get_json()

  # This is what our post from this page looks like
  # {duration: "8", program: "1", startDate: "May 1", title: "URCPP Software Also"}
  
  # First, update the project title
  proj = getProject(username)
  budg = getBudget(username)
  
  if proj is None:
    proj = Projects()
  
  if budg is None:
    budg = Budget()
    budg.save()
  
  proj.title      = data["title"]
  proj.startDate  = data["startDate"]
  proj.duration   = int(data["duration"])
  proj.budgetID   = budg.bID
  proj.save()  
  
  # Next, update the faculty's program
  fac = getFaculty(username)
  # If they don't exist yet, create one.
  if fac is None:
    fac               = URCPPFaculty()
    fac.username      = username
    fac.corresponding = True
  
  fac.pID       = proj.pID
  fac.programID = int(data["program"])
  fac.save()
  
  # Next, we need 
  
  response = { "response" : "OK" }
  return jsonify(response)
