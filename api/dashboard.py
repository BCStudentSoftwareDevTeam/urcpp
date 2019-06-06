from everything import *
from API.faculty import getLDAPFaculty
from API.projects import getProject
from API.parameters import getCurrentParameters
from datetime import datetime

@app.route("/dashboard", methods = ["GET"])
@app.route("/", methods = ["GET"])
@login_required
def dashboard():
  """ This page generate the dasboard """
  ldap = getLDAPFaculty(g.user.username)
  project = getProject(g.user.username)
  currentCycle = getCurrentParameters()
  today = datetime.now()
  email_address_IRBchair = "%s@berea.edu" % (str(currentCycle.IRBchair_id.username))
  email_address_currentchair = "%s@berea.edu" % (str(currentCycle.currentchair_id.username))
  email_address_staffsupport = "%s@berea.edu" % (str(currentCycle.staffsupport_id.username))
  return render_template ("dashboard.html",  cfg=cfg, ldap=ldap, proj=project, currentCycle=currentCycle, today=today, email_IRBchair=email_address_IRBchair, email_currentchair=email_address_currentchair,email_staffsupport=email_address_staffsupport)
  