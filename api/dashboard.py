from everything import *
from API.faculty import getLDAPFaculty
from API.projects import getProject
from API.parameters import getCurrentParameters
from datetime import datetime

@app.route("/dashboard", methods = ["GET"])
@login_required
def dashboard():
  """ This page generate the dasboard """
  ldap = getLDAPFaculty(g.user.username)
  project = getProject(g.user.username)
  currentCycle = getCurrentParameters()
  today = datetime.now()

  return render_template ("dashboard.html", cfg=cfg, ldap=ldap, proj=project, currentCycle=currentCycle, today=today)