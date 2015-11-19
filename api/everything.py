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

# We need peewee's playhouse to help us serialize results
from playhouse.shortcuts import model_to_dict as m2d

# We need to import the DB object
from models import theDB

# For unique values
import uuid

######################################################
# SETUP
######################################################
# Set up the Flask app
app = Flask(__name__)

from api.switch import switch
from api.config import load_config
cfg = load_config('web/config.yaml')
