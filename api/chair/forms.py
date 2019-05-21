from ..everything import *
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtfpeewee.fields import SelectMultipleQueryField
from wtforms.validators import DataRequired
from ..API.committee import getCommitteeMembers

class ManageCommitteeForm(FlaskForm):
    committeeMember = SelectMultipleQueryField(query = LDAPFaculty.select())
        
