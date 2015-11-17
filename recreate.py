# We need to import the DB object
from web.models import theDB
import os
import importlib

# Don't forget to import your own models!
from web.config import load_config
import web.models

# The path is relative to the top of the project.
conf = load_config('web/config.yaml')

# Get the names of the databases we want to work with
sqlite_dbs  = [conf['database']]

# Now, dynamically import the models
#for module in conf['models']:
#  importlib.import_module(module, package = "web.models")
  
# Remove them, then create them.
for fname in sqlite_dbs:
  try:
    print ("Removing {0}.".format(fname))
    os.remove(fname)
  except OSError:
    pass

for fname in sqlite_dbs:
  print ("Creating {0}.".format(fname))
  open(fname, 'a').close()

# Connect to the database
theDB.connect()

# The model names are in the config file. 
# They need to be defined in the models module as well, but this lets us list them 
# in the config for creation in the DB...
# http://stackoverflow.com/questions/1176136/convert-string-to-python-class-object
def class_from_name(module_name, class_name):
    # load the module, will raise ImportError if module cannot be loaded
    m = __import__(module_name, globals(), locals(), class_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c

# First, dynamically import the models
classes = []
for str in conf['models']:
  c = class_from_name("web.models", str)
  classes.append(c)

# Create the tables in the database.
theDB.create_tables(classes)




