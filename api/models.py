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

# To see the databases, do this:
# sqlite_web -p $PORT -H $IP -x data/test.sqlite
    
######################################################
# STATIC MODELS
######################################################

class LDAPFaculty (StaticModel):
  fID               = PrimaryKeyField()
  username          = TextField(unique = True)
  bnumber           = TextField()
  lastname          = TextField()
  firstname         = TextField()

class LDAPStudents (StaticModel):
  username          = PrimaryKeyField()
  bnumber           = TextField()
  lastname          = TextField()
  firstname         = TextField()
  
class Programs (StaticModel):
  pID               = PrimaryKeyField()
  name              = TextField()
  abbreviation      = TextField()

######################################################
# DYNAMIC MODELS
######################################################

class Budget (DynamicModel):
  bID                 = PrimaryKeyField()
  facultyStipend      = IntegerField()
  facultyStipendDesc  = TextField()
  miles               = IntegerField()
  milesDesc           = TextField()
  otherTravel         = IntegerField()
  otherTravelDesc     = TextField()
  equipment           = IntegerField()
  equipmentDesc       = TextField()
  materials           = IntegerField()
  materialsDesc       = TextField()
  other               = IntegerField()
  otherDesc           = TextField()
  
class PreSurvey (DynamicModel):
  psID              = PrimaryKeyField()

class PostSurvey (DynamicModel):
  psID              = PrimaryKeyField()

class Projects (DynamicModel):
  pID                   = PrimaryKeyField()
  title                 = TextField()
  budgetID              = ForeignKeyField(Budget, related_name = 'budget')
  duration              = IntegerField()
  startDate             = DateTimeField()
  year                  = IntegerField( default = cfg["urcpp"]["applicationCycle"])
  # Like the vitae; the file is in a folder.
  # /year/projid/title.pdf
  #proposal     = BlobField()
  hasCommunityPartner   = BooleanField()
  isServiceToCommunity  = BooleanField()
  humanSubjects         = BooleanField()
  # Like the vitae
  # /year/projid/irb.something
  # irb               = BlobField()
  numberStudents    = IntegerField()
  # Stati are in the config under the key
  # projectstatus: ... it is a list.
  status            = TextField(default = cfg["projectStatus"]["pending"])
  createdDate       = DateTimeField(default = datetime.datetime.now)

class URCPPStudents (DynamicModel):
  sID               = PrimaryKeyField()
  username          = ForeignKeyField(LDAPStudents)
  # We need to insert empty rows when we create the students.
  preSurveyID       = ForeignKeyField(PreSurvey)
  postSurveyID      = ForeignKeyField(PostSurvey)
  projectID         = ForeignKeyField(Projects)

class URCPPFaculty (DynamicModel):
  fID               = PrimaryKeyField()
  pID               = ForeignKeyField(Projects)
  username          = ForeignKeyField(LDAPFaculty, to_field = "username")
  # We will always name these ourselves, and 
  # choose where they go. It is in our config[] YAML.
  # Something like...
  # /year/projid/username.pdf
  # vitae         = BlobField()
  yearsFunded       = TextField( default = "" )
  relatedFunding    = TextField( default = "" )
  programID         = ForeignKeyField(Programs, default = 0) 

class Collaborators (DynamicModel):
  cID             = PrimaryKeyField()
  pID             = ForeignKeyField(Projects, related_name = "collaborators")
  username        = ForeignKeyField(LDAPFaculty, to_field = "username")
  yearsFunded     = TextField( default = "" )

class Parameters (DynamicModel):
  pID                 = PrimaryKeyField()
  year                = IntegerField()
  appOpenDate         = DateTimeField()
  appCloseDate        = DateTimeField()
  mileageRate         = FloatField() # Or Double?
  laborRate           = FloatField() # Or Double?

