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

# We need the app
from web import app

# We need to import the DB object
from models import theDB

# Don't forget to import your own models!
from models import Secret, RegLinks

@app.route('/createold', methods = ['GET', 'POST'])
def create ():
  if request.method == 'GET':
    return render_template('create.html')
  elif request.method == 'POST':
    pass
