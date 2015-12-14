from everything import *
from faculty import getFaculty, getLDAPFaculty, getFacultyWithProjects
from projects import getAllProjects
from programs import getAllPrograms
from budget import getAllBudgets

from pages import *

@app.route("/<username>/committee/allBudgets", methods = ["GET"])
def allBudgets_GET (username):
  # All of our queries
  faculty = getFacultyWithProjects()
  proj = getAllProjects()
  programs = getAllPrograms()
  budget = getAllBudgets()

  return render_template (  "allBudgets.html",
                            proj = proj,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            progs = programs,
                            budg = budget,
                          )
