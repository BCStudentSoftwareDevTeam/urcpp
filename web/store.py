from everything import *
from endpoints import getproject

#################################################################
# STEP 2: storesubmitter()
# METHOD: POST
# Stores the faculty member making the URCPP request and
# proceeds on to requesting any additional faculty.
@app.route('/{0}/storecommunicating'.format(cfg['tag']), methods = ['GET', 'POST'])
def storecommunicating ():
  username = session['username']
  if (username != os.getenv('USERNAME')):    
    redirect (url_for ("init"))

  app.logger.info("storecommunicating: Storing the communicating faculty member.")
  app.logger.info("storecommunicating: username is {0}".format(username))
  
  if (request.method == 'POST'):
    app.logger.info("storecommunicating: POST")
    
    # Flask gets very upset if you request a field that does not exist.
    # It might be good to wrap all of these in a function that checks,
    # and if the field does not exist, then a sensible error is output.
    title     = request.form['title']
    firstname = request.form['firstname']
    lastname  = request.form['lastname']
    email     = request.form['email']
    bnumber   = request.form['bnumber']
    
    # If the faculty member exists, pull their record for update.
    facQ = (Faculty.select()
      .where (Faculty.username == username))
    
    # Create a faculty object
    fac = Faculty()
    # If we have an existing faculty member, grab them.
    if facQ.exists():
      fac = facQ.get()

    # Set values on the object
    fac.lastname   = lastname
    fac.firstname  = firstname
    fac.email      = email
    fac.bnumber    = bnumber
    fac.username   = username
    # Save the updated faculty member
    fac.save()
    
    # Do we have an existing project? This involves both the 
    # linking table and the Projects model...
    # Now, make sure the project title is up to date.
    fpQ = (FacultyProjects.select()
      .where (FacultyProjects.fid == fac.fid)
      .where (FacultyProjects.corresponding == True)
      )

    project = Projects()
        
    if fpQ.exists():
      fp = fpQ.get()
      projQ = (Projects.select()
        .where (Projects.pid == fp.pid)
        ) 
      if projQ.exists():
        project = projQ.get()
    
    project.title = title
    project.save()
    
    # If we don't have a linking entry, we need one.
    if not fpQ.exists():
      fp = FacultyProjects (
        fid = fac.fid,
        pid = project.pid,
        corresponding = True
      )
      fp.save()

    return redirect (url_for ("addadditionalfaculty"))

  if (request.method == 'GET'):
    app.logger.error("storecommunicating: GET request not handled.")
    return "Thanks for all the fish."

# If the collaborator is not yet in the database,
# this method will add them. It checks to prevent
# duplicates, and it does this based on the Bnumber.
# It will update everything around the Bnumber, which
# makes it a bit fragile... someone can basically 
# rename me... Hm.
def add_collaborator (firstname = "", lastname = "", email = "", bnumber = ""):
  
  collabQ = (Collaborators.select()
    .where (Collaborators.bnumber == bnumber)
  )
  
  collab = None
  
  if collabQ.exists():
    collab = collabQ.get()
  else:
    collab = Collaborators (
      firstname = firstname,
      lastname  = lastname,
      email     = lastname,
      bnumber   = bnumber
    )
    collab.save()

  return collab  

def add_collaborator_to_project (collaborator = None, project = None):
  fpQ = (FacultyProjects.select()
    .where (FacultyProjects.pid == project.pid)
    .where (FacultyProjects.fid == collaborator.cid)
    )
  
  # If we cannot find this collaborator on this project...
  if not fpQ.exists():
    newfp = FacultyProjects (
      fid = collaborator.cid,
      pid = project.pid,
      corresponding = False
    )
    newfp.save()
  else:
    app.logger.error("add_collaborator_to_project: Could not find project: {0} [pid: {1}]"
      .format(project.title, project.pid)
    )
  
@app.route('/{0}/storeadditionalfaculty'.format(cfg['tag']), methods = ['POST'])
def storeadditionalfaculty ():
  username = session['username']
  if (username != os.getenv('USERNAME')):    
    redirect (url_for ("init"))
  
  lastnames = []
  firstnames = []
  emails = []
  bnumbers = []
  
  fieldcount = request.form['fieldcount']
  app.logger.info("storeadditionalfaculty: fieldcount is {0}".format(fieldcount))
  
  for ndx in range(0, int(fieldcount) + 1):
    app.logger.info("storeadditionalfaculty: Looking for %s" % ndx)
    lastnames.append (request.form['lastnames{0}'.format(ndx)])
    firstnames.append (request.form['firstnames{0}'.format(ndx)])
    emails.append (request.form['emails{0}'.format(ndx)])
    bnumbers.append (request.form['bnumbers{0}'.format(ndx)])
  
  # First, we'll make sure all of these people are collaborators in
  # the database. They are different than faculty... because we don't
  # have guaranteed correct usernames for these... people...
  collabs = []
  for first, last, email, bnum in zip (firstnames, lastnames, emails, bnumbers):
    c = add_collaborator (firstname = first, 
                          lastname = last,
                          email    = email,
                          bnumber  = bnum
                          )
    collabs.append(c)
    
  # Next, they need to be attached to the project.
  # Grab this faculty member's project
  proj = getproject (username)
  for c in collabs:
    add_collaborator_to_project (collaborator = c, project = proj)
  
  
  
  return ""
  
  