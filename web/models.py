from peewee import *

# Create a database
# FIXME: This should be in a config file...
from web.config import load_config

# The path is relative to config.py...
cfg = load_config('web/config.yaml')

webdb = SqliteDatabase(cfg['database'], threadlocals = True)

# This is the parent class.
class OTPModel (Model):
  class Meta:
    database = webdb 

######################################################
# MODELS
######################################################
# FIXME: Create some models
# To see the databases, do this:
# sqlite_web -p $PORT -H $IP -x data/test.sqlite

class Secret (OTPModel):
  sid       = PrimaryKeyField()
  email     = TextField()
  secret    = TextField()

class RegLinks (OTPModel):
  sid       = PrimaryKeyField()
  email     = TextField()
  link      = TextField()