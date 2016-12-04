######################################################
# IMPORTS
######################################################
# Python 2/3 compat
from __future__ import print_function
import os, pprint
# We need a bunch of Flask stuff
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import json
from flask import url_for
from flask import g
from flask import session
from flask import jsonify
from flask import send_from_directory
from flask import flash
from flask import abort
from werkzeug import secure_filename

# need to import g from flask_login
from flask_login import login_user, logout_user, current_user, LoginManager, login_required
# We need peewee's playhouse to help us serialize results
from playhouse.shortcuts import model_to_dict as m2d

# Import the models
from models import *

# For unique values
import uuid

def authUser(env):
  envK = "eppn"
  #app.logger.info("Found remote user: " + env.get("HTTP_X_REMOTE_USER") + env.get("PHP_AUTH_USER"))
  if (envK in env):
    app.logger.info("We're live"+  env[envK].split("@")[0]+ ";")
    return env[envK].split("@")[0]
  elif ("DEBUG" in app.config) and app.config["DEBUG"]:
    app.logger.info("We're in debug: " + cfg["DEBUG"]["user"])
    return cfg["DEBUG"]["user"]
  else:
    return None

######################################################
# SETUP
######################################################
# Set up the Flask app
here = os.path.dirname(__file__)
app = Flask(__name__)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from api.switch import switch
from api.config import load_config

# cfg = load_config('/var/www/html/urcpp-flask/api/config.yaml')
cfg = load_config(os.path.join(here, 'config.yaml'))
app.config['SECRET_KEY'] = open(os.path.join(here, 'secret_key'), 'rb').read()
app.config['TEMPLATE_AUTO_RELOAD'] = True

@app.before_request
def before_request():
    g.dbDynamic = dynamicDB.connect()
    g.user = current_user

@app.teardown_request
def teardown_request(exception):
    dbS = getattr(g, 'dbStatic', None)
    dbD = getattr(g, 'dbDynamic', None)
    if (dbS is not None) and (not dbS.is_closed()):
      dbS.close()
    if (dbD is not None) and (not dbD.is_closed()):
      dbD.close()

@login_manager.user_loader
def load_user(fID):
  return LDAPFaculty.get(LDAPFaculty.fID == fID)