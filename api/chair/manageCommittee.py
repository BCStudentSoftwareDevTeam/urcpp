from ..everything import *
from ..API.parameters import getCurrentParameters
from forms import ManageCommitteeForm
from ..API.committee import addCommitteeMembers, removeCommitteeMembers, getCommitteeMembers

from ..pages import *

@app.route("/chair/manageCommittee", methods = ["GET"])
@login_required
def manageCommittee_GET ():
  if not g.user.isChair:
    abort(403)
  #facultySelect = ManageCommitteeForm()
  
 # facultySelect.committeeMember.default = getCommitteeMembers()
  #facultySelect.process()
  
  notCommittee = LDAPFaculty.select().where(LDAPFaculty.isCommitteeMember == False)
  committee = LDAPFaculty.select().where(LDAPFaculty.isCommitteeMember == True)

  parameters = getCurrentParameters()
  return render_template ("chair/manageCommittee.html", 
                           username = g.user.username,
                           ldap = g.user,
                           params = parameters,
                           cfg = cfg,
                           #facultySelect  = facultySelect,
                           notCommittee = notCommittee,
                           committee = committee
                           )
                           
@app.route("/addCommitteeMember", methods = ["GET", "POST"])
@login_required
# check to see if the user has permission
def addCommitteeMember():
  if not g.user.isChair:
    abort(403)
    
  desiredCommitteeList = request.form.getlist('addCommitteeMember') # get the list of chair
  
  print desiredCommitteeList

  #remove old committee Members

  # add new committee members
  addCommitteeMembers(desiredCommitteeList)
  
  flash("Committee edited")
  return redirect(url_for('manageCommittee_GET'))
  
  
@app.route("/removeCommitteeMember", methods = ["GET", "POST"])
@login_required
# check to see if the user has permission
def removeCommitteeMember():
  if not g.user.isChair:
    abort(403)
    

  undesiredCommitteeList = request.form.getlist('removeCommitteeMember') # get the list of chair

  #remove old committee Members
  removeCommitteeMembers(undesiredCommitteeList)
  

  flash("Committee edited")
  return redirect(url_for('manageCommittee_GET'))