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

class Secret (BaseModel):
  sid       = PrimaryKeyField()
  email     = TextField()
  secret    = TextField()

class RegLinks (BaseModel):
  sid       = PrimaryKeyField()
  email     = TextField()
  link      = TextField()