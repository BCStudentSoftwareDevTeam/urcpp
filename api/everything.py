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
from flask import json
from flask import url_for
from flask import g
from flask import session
from flask import jsonify
from flask import send_from_directory
from werkzeug import secure_filename

# We need peewee's playhouse to help us serialize results
from playhouse.shortcuts import model_to_dict as m2d

# Import the models
from models import *

# For unique values
import uuid

def authUser(env):
  envK = "HTTP_X_PROXY_REMOTE_USER"
  # app.logger.info("Found remote user: " + env.get("HTTP_X_REMOTE_USER"))
  if (envK in env) and env.get(envK):
    return env.get(envK)
  elif ("DEBUG" in app.config) and app.config["DEBUG"]:
    return cfg["DEBUG"]["user"]
  else:
    return None

######################################################
# SETUP
######################################################
# Set up the Flask app

app = Flask(__name__)

from api.switch import switch
from api.config import load_config
cfg = load_config('api/config.yaml')
