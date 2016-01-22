import datetime
from peewee import *
import os

# Create a database
from api.config import load_config

# The path is relative to the top of the project.
print("GETCWD MODELS: " + os.getcwd())

cfg = load_config('api/config.yaml')
staticDB  = SqliteDatabase(cfg['databases']['static'])
dynamicDB = SqliteDatabase(cfg['databases']['dynamic'])

print ("SQLITE DATABASES LOADED.")

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
  facultyStipend      = IntegerField(null = True)
  facultyStipendDesc  = TextField(default = "")
  miles               = IntegerField(null = True)
  milesDesc           = TextField(default = "")
  otherTravel         = IntegerField(null = True)
  otherTravelDesc     = TextField(default = "")
  equipment           = IntegerField(null = True)
  equipmentDesc       = TextField(default = "")
  materials           = IntegerField(null = True)
  materialsDesc       = TextField(default = "")
  other               = IntegerField(null = True)
  otherDesc           = TextField(default = "")
  
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
  hasCommunityPartner   = BooleanField(default = False)
  isServiceToCommunity  = BooleanField(default = False)
  humanSubjects         = BooleanField(null = True)
  # Like the vitae
  # /year/projid/irb.something
  # irb               = BlobField()
  numberStudents    = IntegerField(default = 1)
  # Stati are in the config under the key
  # projectstatus: ... it is a list.
  status            = TextField(default = cfg["projectStatus"]["incomplete"])
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
  pID               = ForeignKeyField(Projects, related_name = "project")
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

class Voting (DynamicModel):
  vID                   = PrimaryKeyField()
  committeeID           = ForeignKeyField(LDAPFaculty, to_field = "username")
  projectID             = ForeignKeyField(Projects)
  studentLearning       = FloatField(null = True)
  studentAccessibility  = FloatField(null = True)
  qualityOfResearch     = FloatField(null = True)
  studentDevelopment    = FloatField(null = True)
  facultyDevelopment    = FloatField(null = True)
  collaborative         = FloatField(null = True)
  interaction           = FloatField(null = True)
  communication         = FloatField(null = True)
  scholarlySignificance = FloatField(null = True)
  proposalQuality       = FloatField(null = True)
  budget                = FloatField(null = True)
  timeline              = FloatField(null = True)
  