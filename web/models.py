import datetime
from peewee import *

# Create a database
# FIXME: This should be in a config file...
from web.config import load_config

# The path is relative to the top of the project.
cfg = load_config('web/config.yaml')
theDB = SqliteDatabase(cfg['database'])

# This is the parent class.
class BaseModel (Model):
  class Meta:
    database = theDB

######################################################
# MODELS
######################################################
# FIXME: Create some models
# To see the databases, do this:
# sqlite_web -p $PORT -H $IP -x data/test.sqlite

class Faculty (BaseModel):
  fid           = PrimaryKeyField()
  bnumber       = TextField()
  lastname      = TextField()
  firstname     = TextField()
  email         = TextField()
  username      = TextField()

class Projects (BaseModel):
  pid           = PrimaryKeyField()
  title         = TextField()
  created_date  = DateTimeField(default = datetime.datetime.now)

class FacultyProjects (BaseModel):
  fpid          = PrimaryKeyField()
  pid           = IntegerField()
  fid           = IntegerField()
  corresponding = BooleanField()
