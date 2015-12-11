from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getAllProjects
from programs import getAllPrograms
from budget import getAllBudgets

from pages import *

@app.route("/<username>/committee/allProjects", methods = ["GET"])
def allProjects_GET (username):
  # All of our queries
  faculty = getFaculty(username)
  ldapFaculty = getLDAPFaculty(username)
  project = getAllProjects()
  programs = getAllPrograms()
  budget = getAllBudgets()
  
  return render_template (  "allProjects.html",
                            proj = project,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            ldap = ldapFaculty,
                            progs = programs,
                            budg = budget,
                            fields =["Duration", "Start Date", "Comm. Partner/Service", "# Students", "Status", "Created"],
                          )
