######################################################
# IMPORTS
######################################################
# Python 2/3 compat
from __future__ import print_function
import os
# We need a bunch of Flask stuff
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import g
from flask import session
# We need to import the DB object
from models import theDB

# Import all of the classes used in the data model
from web.models import *

# For switch()
from switch import switch

# For unique values
import uuid

######################################################
# SETUP
######################################################
# Set up the Flask app
from web import app
from web.switch import switch
from web.config import load_config
cfg = load_config('web/config.yaml')

# We have to set up and break down the DB on every request.
@app.before_request
def before_request():
  g.db = theDB
  g.db.connect()

@app.after_request
def after_request(response):
  g.db.close()
  return response

######################################################
# ROUTES
######################################################

# STEP 1: We begin by going to the root, which bounces
# us over to the signin page.
@app.route("/")
def init ():
  if 'username' not in session:
    # Store their username in the session, creating a cookie
    # so we can keep track of them as they go through the app.
    session['username'] = os.getenv('USERNAME')    
  else:
    app.logger.info ("Found '{0}' in session.".format(session['username']))
      
  # Redirect everyone
  return redirect('/{0}/{1}/start'.format(cfg['tag'], session['username']))

@app.route('/s/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)


#################################################################
# ROUTER
# Routes all requests.
@app.route('/{0}/<username>/<step>'.format(cfg['tag']), methods = ['GET', 'POST'])
def router (username, step):
  # If they come in via GET, we're resuming a session.
  # If we're proceeding through a session, it is by POST.
  # GET sessions should restore information from the DB, while
  # POST should present the forms as-is.
  
  app.logger.info("User: {0} Step: {1}".format(username, step))

  if request.method == 'POST':
    
    # We should already be in the session at this point.
    # If not, kick them to an ELSE that sends them back to the start.
    if not session['username']:
      return redirect(url_for('/'))

    # If things don't match, also kick them back to try again.
    elif session['username'] != username:
      session['username'] = None
      return redirect(url_for('/'))
      
    # Otherwise, lets run the app.
    else:
      for case in switch(step):      
        # STEP 2
        # Asks the submitter for additional faculty and students.
        if case ("storecommunicating"):
          return storecommunicating ()
        
        # STEP 3
        # Asks for additional faculty
        if case ("storeadditionalfaculty"):
          return storeadditionalfaculty ()
          
        if case():
          app.logger.error ("Something went wrong.")

  if request.method == 'GET':
    # The first step will necessarily be a GET request.
    # Most likely redirected from '/'.
    for case in switch(step):
      # STEP 1
      # Step one asks for the name of the URCPP request 
      # submitter and their B#.
      if case("start"):
        return start()


#################################################################
# STEP 1
def start ():
  if request.method == 'GET':
    
    # If we come in by GET, we might have some data we want to 
    # pre-populate into the form.
    query = Faculty.select().where(Faculty.username == session['username'])
    
    # If the query is valid, then this faculty member has been into 
    # the system before, and we can do some pre-populating.
    if query.exists():
      # Run the query
      facultymember = query.get()
      # If they have some projects, put the title here.
      if facultymember.projects.exists():
        app.logger.info("start: Faculty member has one or more projects.")
        facultymember.projecttitle = facultymember.projects[0].title
      else:
        app.logger.info("start: Faculty member has no projects.")
        facultymember.projecttitle = None
    # If they aren't in the system, we can make sure the variable is None.
    else:
      facultymember = None
    
    # Render the start page.
    return render_template('start.html', 
                            autofill = facultymember,
                            username = session['username'],
                            tag  = cfg['tag'],
                            next = "storecommunicating"
                            )
  else:
    app.logger.error("Somehow, the user arrived at the start handler by POST.")
    return "We should never arrive at this page via POST. Error."

#################################################################
# STEP 2: storesubmitter()
# METHOD: POST
# Stores the faculty member making the URCPP request and 
# proceeds on to requesting any additional faculty.
def storecommunicating ():
  app.logger.info("storecommunicating: Storing the communicating faculty member.")
  
  if request.method == 'POST':
    app.logger.info("storecommunicating: POST")
    
    # Flask gets very upset if you request a field that does not exist.
    # It might be good to wrap all of these in a function that checks,
    # and if the field does not exist, then a sensible error is output.
    title     = request.form['projectitle']
    firstname = request.form['firstname']
    lastname  = request.form['lastname']
    email     = request.form['email']
    bnumber   = request.form['bnumber']

    # Create a Faculty() peewee ORM object
    fac = Faculty (firstname     = firstname,
                   lastname      = lastname,
                   email         = email,
                   username      = session['username'],
                   bnumber       = bnumber,
                   corresponding = True)

    # Save the faculty member to the DB.
    # Only do the insert if the B# does not already exist.
    query = Faculty.select().where(Faculty.username == session['username'])
    # If we already exist, we don't know the ID. This is a problem
    # in the next step.
    
    # FIXME: If the faculty member already exists, we might say that they
    # cannot be a corresponding faculty member on more than one project.
    # Hence, we should perhaps... do something different here.
    if query.exists():
      # Get the faculty member from the DB, so we have a faculty id.
      fac = query.get()
      print (fac)
    else:
      fac.save()
      
    # Create a partial project entry.
    proj = Projects (faculty = fac.fid, 
                     title   = title
                     # The date is automatically filled in with 'now'
                     )
    
 
    
    # Save the Project to the DB.
    # Only do this if the project title does not already exist.
    query = Projects.select().where(Projects.faculty == fac.fid)
    if not query.exists():
      proj.save()
    
    return render_template('additionalfaculty.html', 
                            username = session['username'],
                            tag  = cfg['tag'],
                            next = "storeadditionalfaculty"
                            )
  else:
    app.logger.error("storecommunicating: GET request not handled.")
    return "Thanks for all the fish."
    
  


#################################################################
# STEP 3: addfaculty()
# POST
#   Store the data. Redirect to the GET.
# GET
#   Allow the user to enter more faculty.
def storeadditionalfaculty ():
  app.logger.info("Made it to storeadditionalfaculty().")
  
  if request.method == 'POST':
    pass
    
  else:
    app.logger.error("storeadditionalfaculty: GET request not handled.")
    return "Thanks for all the fish."
    
  
  