import datetime
from peewee import *

# Create a database
from api.config import load_config

# The path is relative to the top of the project.
cfg = load_config('api/config.yaml')

class SqliteModel (Model):

  def __init__ (self):
    self.dbs = {}

  def connect (self, name):
    if not name in self.dbs:
      self.dbs[name] = SqliteDatabase(None)

    self.dbs[name].init(cfg['databases'][name])
    self.dbs[name].connect()

  def close (self, name):
    self.dbs[name].close()

######################################################
# MODELS
######################################################
# FIXME: Create some models
# To see the databases, do this:
# sqlite_web -p $PORT -H $IP -x data/test.sqlite

class Faculty (SqliteModel):
  fid           = PrimaryKeyField()
  bnumber       = TextField()
  lastname      = TextField()
  firstname     = TextField()
  email         = TextField()
  # We have to use the username as a unique property.
  # Users log in via this token, and therefore, there
  # can only be one faculty member with a given username.
  username      = TextField(unique = True)

class LDAPFaculty (SqliteModel):
  fid       = PrimaryKeyField()
  lastname  = TextField()
  firstname = TextField()
  username  = TextField(unique = True)
  bnumber   = TextField()
  email     = TextField()

class Projects (SqliteModel):
  pid           = PrimaryKeyField()
  title         = TextField()
  created_date  = DateTimeField(default = datetime.datetime.now)

class FacultyProjects (SqliteModel):
  fpid          = PrimaryKeyField()
  pid           = ForeignKeyField(Projects)
  fid           = ForeignKeyField(Faculty)
  corresponding = BooleanField()
