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
                conf['databases']['dynamic'],
                # conf['databases']['static']
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
dynamicDB.create_tables(get_classes('dynamic'))

# Add some dummy data.

budget = Budget (
  facultyStipend      = 12,
  facultyStipendDesc  ="Awesome!",
  miles               = 12,
  milesDesc           ="Awesome!",
  otherTravel         = 12,
  otherTravelDesc     ="Awesome!",
  equipment           = 12,
  equipmentDesc       ="Awesome!",
  materials           = 12,
  materialsDesc       ="Awesome!",
  other               = 12,
  otherDesc           ="Awesome!",
  )
budget.save()

proj = Projects (
  title                 = "Super Dooper Robots",
  budgetID              = 1,
  duration              = 8,
  startDate             = "2015-12-15",
  endDate               = "2016-02-09",
  year                  = 2016,
  hasCommunityPartner   = True,
  isServiceToCommunity  = True,
  humanSubjects         = True,
  numberStudents        = 3
  )
proj.save()

collab = Collaborators (
  pID = proj.pID,
  username = "heggens"
  )
collab.save()

fac = URCPPFaculty (
  pID               = proj.pID,
  username          = "jadudm",
  # Possible values: oneyr, twoyr, threeToFiveyr, sixToTenyr, elevenPlus
  yearsFunded       = "{oneyr:1,twoyr:1,threeToFiveyr:1,sixToTenyr:1,elevenPlus:1}",
  relatedFunding    = "I got big bucks and I cannot lie.",
  programID         = 1,
  )
fac.save()

params = Parameters(
  year                = 2016,
  appOpenDate         = "2015-12-15",
  appCloseDate        = "2016-01-31",
  mileageRate         = 0.52,
  laborRate           = 8.00,
  )
params.save()