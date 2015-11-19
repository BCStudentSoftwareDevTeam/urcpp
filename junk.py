def updateprojecttitle (username):
  app.logger.info("updateprojecttitle: Updating project title.")
  app.logger.info("updateprojecttitle: username is {0}".format(username))

  if request.method == 'POST':
    app.logger.info("updateprojecttitle: POST")
    
    facQ = (Faculty.select()
      .join(FacultyProjects, on = (FacultyProjects.fid == Faculty.fid))
      .join(Projects, on = (FacultyProjects.pid == Projects.pid))
      .where(Faculty.username == username)
      .where(FacultyProjects.corresponding == True)
      )
    theFaculty = facQ.get()
    
    projectQ = (Projects.select()
      .join(Faculty, on = (theFaculty.fid == Projects.corresponding))
      )
    theProject = projectQ.get()
    
    theProject.title = request.form['newTitle']
    
    # FIXME: This should be a redirect to a get of 
    # the add additional faculty handler?
    return render_template('addadditionalfaculty.html',
                            username = username,
                            tag  = cfg['tag'],
                            next = "addadditionalfaculty"
                            )
    


def init ():
  from datetime import timedelta, datetime

  # FIXME: It is not clear what value sessions are playing at this point.
  # FIXME: We should also make sure that what we are storing is correct
  #        and timely. We're going to rely on that cookie, perhaps.
  #        Or, something... I want to make sure that when the user re-enters
  #        elsewhere that we check these things... perhaps this should be
  #        broken out into a separate function, and used everywhere?
  if 'username' in session:
    # Check if we should time out our session value.
    if 'lastlogin' in session:
      app.logger.info("init: last login for {0} was {1}"
        .format(session['username'], session['lastlogin']))
      # Import the library we need for timedeltas
      timeout_duration = timedelta (minutes = cfg['timeout'])
      then = session['lastlogin']
      # datetime.strptime(session['lastlogin'], '%Y-%M-%D %H:%M:%S')
      app.logger.info("init: then was {0}".format(then))
      difference = datetime.now() - then

      app.logger.info("init: time difference is {0}".format(difference))
      if difference > timeout_duration:
        app.logger.info("init: difference is greater than {0} minutes.".format(cfg['timeout']))
        session['username'] = os.getenv('USERNAME')
        app.logger.info ("init: Found username in environment 1: {0}".format(session['username']))
      else:
        # Keep the session username
        pass
    # They haven't logged in before, so we have no info...
    else:
      session['lastlogin'] = datetime.now()
      session['username'] = os.getenv('USERNAME')
      app.logger.info ("init: Found username in environment 2: {0}".format(session['username']))

  # If the username is not in the session
  else:
    session['username'] = os.getenv('USERNAME')
    app.logger.info ("init: Found username in environment 3: {0}".format(session['username']))

  # Redirect everyone
  return redirect('/{0}/{1}/start'.format(cfg['tag'], session['username']))






#################################################################
# ROUTER
# Routes all requests.
def router (owner, step):
  # If they come in via GET, we're resuming a session.
  # If we're proceeding through a session, it is by POST.
  # GET sessions should restore information from the DB, while
  # POST should present the forms as-is.

  username = session['username']
  if (owner != username):
    return render_template ('wronguser.html', 
                            owner = owner,
                            username = username)
  

  app.logger.info("User: {0} Step: {1}".format(username, step))
  
  if request.method == 'POST':

    # We should already be in the session at this point.
    # If not, kick them to an 'else' that sends them back to the start.
    # FIXME: Note above how usernames in sessions are handled, and
    # think seriously about how we should check who's-who, here.
    if not session['username']:
      return redirect(url_for('/'))

    # If things don't match, also kick them back to try again.
    elif session['username'] != username:
      session['username'] = None
      return redirect(url_for('/'))

    # Otherwise, lets run the app.
    else:
      for case in switch(step):
        username = session['username']
        # STEP 2
        # Asks the submitter for additional faculty and students.
        if case ("storecommunicating"):
          return storecommunicating (username)
          
        # STEP 3
        # Asks for additional faculty
        if case ("addadditionalfaculty"):
          return addadditionalfaculty (username)

        if case():
          app.logger.error ("Something went wrong.")

  if request.method == 'GET':
    if session['username'] != username:
      return "ERROR"

    # The first step will necessarily be a GET request.
    # Most likely redirected from '/'.
    for case in switch(step):
      # FIXME: These should always be the same.
      # STEP 1
      # Step one asks for the name of the URCPP request
      # submitter and their B#.
      if case("start"):
        app.logger.info("router: calling start.")
        return start(username)
