# We need to import the DB object
from web.models import webdb
import os

# Don't forget to import your own models!
from web.models import Secret, RegLinks
from web.config import load_config

# The path is relative to config.py...
cfg = load_config('web/config.yaml')

# Get the names of the databases we want to work with
sqlite_dbs  = [cfg['database']]

# Remove them, then create them.
for file in sqlite_dbs:
  try:
    fname = "data/{0}".format(file)
    print ("Removing {0}.".format(fname))
    os.remove(fname)
  except OSError:
    pass

for file in sqlite_dbs:
  fname = 'data/{0}'.format(file)
  print ("Creating {0}.".format(fname))
  open(fname, 'a').close()

# Recreate it
webdb.connect()

# We can grab these from the config as well.
# http://stackoverflow.com/questions/1176136/convert-string-to-python-class-object
def class_from_name(module_name, class_name):
    # load the module, will raise ImportError if module cannot be loaded
    m = __import__(module_name, globals(), locals(), class_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c

classes = []
for str in cfg['models']:
  classes.append(class_from_name("web.models", str))

print ("Creating tables.")
webdb.create_tables(classes)

