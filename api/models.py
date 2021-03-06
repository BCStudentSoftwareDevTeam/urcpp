import datetime
from peewee import *
import os

# Create a database
from api.config import load_config


here = os.path.dirname(__file__)

cfg = load_config(os.path.join(here, 'config.yaml'))

dynamicDB = MySQLDatabase(cfg['db']['name'], host=cfg['db']['host'], user=cfg['db']['user'], passwd=cfg['db']['password'])

class DynamicModel (Model):
  class Meta:
    database = dynamicDB

# To see the databases, do this:
# sqlite_web -p $PORT -H $IP -x data/test.sqlite

######################################################
# STATIC MODELS
######################################################

class LDAPFaculty (DynamicModel):
  fID               = PrimaryKeyField()
  username          = CharField(unique = True)
  bnumber           = TextField()
  lastname          = TextField()
  firstname         = TextField()
  isChair           = BooleanField(default=False)
  isCommitteeMember = BooleanField(default=False)

  def is_active(self):
      """All user will be active"""
      return True


  def get_id(self):
      return str(self.fID)

  def is_authenticated(self):
      """Return True if the user is authenticated"""
      return True

  def is_anonymous(self):
      return False

  def __repr__(self):
    return '{0} {1}'.format(self.firstname, self.lastname)
class LDAPStudents (DynamicModel):
  username          = PrimaryKeyField()
  bnumber           = TextField()
  lastname          = TextField()
  firstname         = TextField()

class Programs (DynamicModel):
  pID               = PrimaryKeyField()
  name              = TextField()
  abbreviation      = TextField()

######################################################
# DYNAMIC MODELS
######################################################

class Budget (DynamicModel):
  bID                 = PrimaryKeyField()
  facultyStipend      = IntegerField(default=0)
  facultyStipendDesc  = TextField(default = "")
  miles               = IntegerField(default=0)
  milesDesc           = TextField(default = "")
  otherTravel         = IntegerField(default=0)
  otherTravelDesc     = TextField(default = "")
  equipment           = IntegerField(default=0)
  equipmentDesc       = TextField(default = "")
  materials           = IntegerField(default=0)
  materialsDesc       = TextField(default = "")
  other               = IntegerField(default=0)
  otherDesc           = TextField(default = "")

class PreSurvey (DynamicModel):
  psID                = PrimaryKeyField()

class PostSurvey (DynamicModel):
  psID                = PrimaryKeyField()


class Parameters (DynamicModel):
  pID                 = PrimaryKeyField()
  year                = IntegerField(unique=True)
  appOpenDate         = DateTimeField()
  appCloseDate        = DateTimeField()
  ProposalAcceptanceDate = DateTimeField()
  AllSubmissionsClosedDate = DateTimeField()
  mileageRate         = FloatField() # Or Double?
  laborRate           = FloatField() # Or Double?
  isCurrentParameter  = BooleanField(default=False)
  IRBchair_id            = ForeignKeyField(LDAPFaculty, to_field = "username")
  currentchair_id        = ForeignKeyField(LDAPFaculty, to_field = "username")
  staffsupport_id        = ForeignKeyField(LDAPFaculty, to_field = "username")
class Projects (DynamicModel):
  pID                   = PrimaryKeyField()
  title                 = TextField()
  budgetID              = ForeignKeyField(Budget, related_name = 'budget')
  duration              = IntegerField()
  startDate             = DateTimeField()
  endDate               = DateTimeField()
  year                  = ForeignKeyField(Parameters, to_field = "year")
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
  status            = TextField(default = cfg["projectStatus"]["Incomplete"])
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
  pID               = ForeignKeyField(Projects, db_column="pid_id", related_name = "project")
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



class Voting (DynamicModel):
  vID                   = PrimaryKeyField()
  committeeID           = ForeignKeyField(LDAPFaculty, to_field = "username")
  projectID             = ForeignKeyField(Projects)
  studentLearning       = FloatField(null = True)
  studentAccessibility  = FloatField(null = True)
  qualityOfResearch     = FloatField(null = True)
  studentDevelopment    = FloatField(null = True)
  facultyDevelopment    = FloatField(null = True)
  development           = FloatField(null = True)
  collaborative         = FloatField(null = True)
  interaction           = FloatField(null = True)
  communication         = FloatField(null = True)
  scholarlySignificance = FloatField(null = True)
  proposalQuality       = FloatField(null = True)
  budget                = FloatField(null = True)
  timeline              = FloatField(null = True)
  comments              = TextField(null = True)

class EmailTemplates (DynamicModel):
  eID                   = PrimaryKeyField()
  Body                  = TextField(null = True)
  Subject               = TextField(null = True)
