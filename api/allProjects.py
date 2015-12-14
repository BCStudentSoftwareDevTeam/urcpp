from everything import *
from faculty import  getFacultyWithProjects, getLDAPFaculty
from projects import getAllProjects
from programs import getAllPrograms
from budget import getAllBudgets

from pages import *

@app.route("/<username>/committee/allProjects", methods = ["GET"])
def allProjects_GET (username):
  # All of our queries
  faculty =  getFacultyWithProjects()
  project = getAllProjects()
  programs = getAllPrograms()
  budget = getAllBudgets()
  
  return render_template (  "allProjects.html",
                            proj = project,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            progs = programs,
                            budg = budget,
                          )
