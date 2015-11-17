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
  # We have to use the username as a unique property.
  # Users log in via this token, and therefore, there
  # can only be one faculty member with a given username.
  username      = TextField(unique = True)

class Projects (BaseModel):
  pid           = PrimaryKeyField()
  title         = TextField()
  corresponding = ForeignKeyField(Faculty)
  created_date  = DateTimeField(default = datetime.datetime.now)

class FacultyProjects (BaseModel):
  fpid          = PrimaryKeyField()
  pid           = ForeignKeyField(Projects)
  fid           = ForeignKeyField(Faculty)
  corresponding = BooleanField()
