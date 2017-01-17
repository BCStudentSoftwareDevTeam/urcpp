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
  facultySelect = ManageCommitteeForm()
  facultySelect.committeeMember.default = getCommitteeMembers()
  facultySelect.process()
  parameters = getCurrentParameters()
  return render_template ("pages/manageCommittee.html", 
                           username = g.user.username,
                           ldap = g.user,
                           params = parameters,
                           cfg = cfg,
                           facultySelect  = facultySelect
                           )
                           
@app.route("/editCommitteeMember", methods = ["GET", "POST"])
@login_required
# check to see if the user has permission
def addCommitteMember():
  if not g.user.isChair:
    abort(403)
    
  desiredCommitteeList = request.form.getlist('committeeMember') # get the list of chair
  print desiredCommitteeList
  #remove old committee Members
  removeCommitteeMembers(desiredCommitteeList)
  
  # add new committee members
  addCommitteeMembers(desiredCommitteeList)
  
  flash("Committee edited")
  return redirect(url_for('manageCommittee_GET'))