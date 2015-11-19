import datetime
from peewee import *

# Create a database
from api.config import load_config

# The path is relative to the top of the project.
cfg = load_config('api/config.yaml')
staticDB  = SqliteDatabase(cfg['databases']['static'])
dynamicDB = SqliteDatabase(cfg['databases']['dynamic'])

class StaticModel (Model):
  class Meta:
    database = staticDB
  
class DynamicModel (Model):
  class Meta:
    database = dynamicDB

    
######################################################
# MODELS
######################################################
# FIXME: Create some models
# To see the databases, do this:
# sqlite_web -p $PORT -H $IP -x data/test.sqlite

class LDAPFaculty (StaticModel):
  fid           = PrimaryKeyField()
  bnumber       = TextField()
  lastname      = TextField()
  firstname     = TextField()
  email         = TextField()
  username      = TextField(unique = True)

class Faculty (DynamicModel):
  fid           = PrimaryKeyField()
  username      = TextField()
  
class Projects (DynamicModel):
  pid           = PrimaryKeyField()
  title         = TextField()
  created_date  = DateTimeField(default = datetime.datetime.now)

class FacultyProjects (DynamicModel):
  fpid          = PrimaryKeyField()
  pid           = ForeignKeyField(Projects)
  fid           = ForeignKeyField(LDAPFaculty)
  corresponding = BooleanField()
