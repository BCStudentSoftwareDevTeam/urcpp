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
  corresponding = BooleanField()

class Projects (BaseModel):
  pid           = PrimaryKeyField()
  faculty       = ForeignKeyField(Faculty, related_name = 'projects')
  title         = TextField()
  created_date  = DateTimeField(default = datetime.datetime.now)
