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
from flask import jsonify

# We need peewee's playhouse to help us serialize results
from playhouse.shortcuts import model_to_dict as m2d

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
        # STEP 2
        # Asks the submitter for additional faculty and students.
        if case ("storecommunicating"):
          return storecommunicating (username)

        # STEP 3
        # Asks for additional faculty
        if case ("storeadditionalfaculty"):
          return storeadditionalfaculty ()

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
        return start(username)


#################################################################
# JSON HELPERS

def getcorresponding (username):
  facQ = (Faculty.select()
    .join(FacultyProjects, on = (FacultyProjects.fid == Faculty.fid))
    .join(Projects, on = (FacultyProjects.pid == Projects.pid))
    .where(Faculty.username == username)
    .where(FacultyProjects.corresponding == True)
      )

  if facQ.exists():
    fac = facQ.get()
    app.logger.info("Fetched Corresponding Faculty: {0}".format(fac))
    return fac
  else:
    app.logger.info("Corresponding faculty {0} not found.".format(username))
    return None

@app.route("/{0}/_/getcorresponding/<username>".format(cfg['tag']))
def _getcorresponding (username):
  fac = getcorresponding (username)
  json = jsonify(m2d(fac))
  return json

def getproject (username):
  # Run the query. There MUST be only one project for
  # which they are corresponding.
  theFaculty = getcorresponding(username)

  projectQ = (Projects.select()
    .join(Faculty, on = (theFaculty.fid == Projects.corresponding))
    )

  if projectQ.exists():
    return projectQ.get()
  else:
    return None

@app.route("/{0}/_/getproject/<username>".format(cfg['tag']))
def _getproject (username):
  proj = getproject (username)
  json = jsonify(m2d(proj))
  return json

#################################################################
# STEP 1
# FIXME: 20151116 - Need to update this to reflect the new data model.
def start (username):
  if request.method == 'GET':
    # Render the start page.
    # There used to be a lot of code here.
    # Now, it's a JSON query in the page itself. The pre-population
    # happens entirely in JavaScript, and here, we just render
    # the page. This seems cleaner, actually.
    return render_template('start.html',
                            username = username,
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
def storecommunicating (username):
  # FIXME 20151117 : This function is broken, due to datamodel changes.
  # It will need to be updated to reflect the new model.

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

    # Does this faculty member already have a project they are
    # corresponding on? If so, we need to populate this page with
    # information that is appropriate.
    facQ = (Faculty.select()
      .join(FacultyProjects, on = (FacultyProjects.fid == Faculty.fid))
      .join(Projects, on = (FacultyProjects.pid == Projects.pid))
      .where(Faculty.username == username)
      .where(FacultyProjects.corresponding == True)
      )


    # Create a Faculty() peewee ORM object
    fac = Faculty (firstname     = firstname,
                   lastname      = lastname,
                   email         = email,
                   username      = username,
                   bnumber       = bnumber,
                   corresponding = True)

    # Save the faculty member to the DB.
    # Only do the insert if the B# does not already exist.
    query = Faculty.select().where(Faculty.username == username)
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
