# We need to import the DB object
from api.models import *
import os, sys
import importlib

# Don't forget to import your own models!
from api.config import load_config
from api.models import *

# The path is relative to the top of the project.
conf = load_config('api/config.yaml')

# Get the names of the databases we want to work with
sqlite_dbs  = [
                # conf['databases']['dynamic'],
                conf['databases']['static']
              ]

# Remove them, then create them.
for fname in sqlite_dbs:
  try:
    print ("Removing {0}.".format(fname))
    os.remove(fname)
  except OSError:
    pass

for fname in sqlite_dbs:
  if os.path.isfile(fname):
    print ("Database {0} should not exist at this point!".format(fname))
  print ("Creating empty SQLite file: {0}.".format(fname))
  open(fname, 'a').close()

def class_from_name (module_name, class_name):
    # load the module, will raise ImportError if module cannot be loaded
    # m = __import__(module_name, globals(), locals(), class_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(module_name, class_name)
    return c

def get_classes (db):
  classes = []
  for str in conf['models'][db]:
    print ("\tCreating model for '{0}'".format(str))
    c = class_from_name(sys.modules[__name__], str)
    classes.append(c)
  return classes

# staticDB.create_tables(get_classes('static'))
dynamicDB.create_tables(get_classes('static'))

# Add some dummy data.
fac = LDAPFaculty ( firstname     = "Matt",
                    lastname      = "Jadud",
                    username      = "jadudm",
                    bnumber       = "B00669796"
                 )
fac.save()

fac = LDAPFaculty ( firstname     = "Scott",
                    lastname      = "Heggen",
                    username      = "heggens",
                    bnumber       = "B00660000"
                 )
fac.save()

fac = LDAPFaculty ( firstname     = "Mario",
                    lastname      = "Nakazawa",
                    username      = "nakazawam",
                    bnumber       = "B00661111"
                 )
fac.save()

prog = Programs ( name = "Computer and Information Science",
                  abbreviation = "CSC"
                )
prog.save()

prog = Programs ( name = "Biology",
                  abbreviation = "BIO"
                )
prog.save()

prog = Programs ( name = "Physics",
                  abbreviation = "PHY"
                )
prog.save()
