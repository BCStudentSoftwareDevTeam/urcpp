from everything import *
from applicationCycle import getCurrentCycle
from faculty import getFaculty, getLDAPFaculty, getFacultyWithProjects
from projects import getAllCurrentProjects
from programs import getAllPrograms
from budget import getAllBudgets
from parameters import getParameters
from makeExcel import getFilename

from pages import *

@app.route("/<username>/committee/allBudgets", methods = ["GET"])
def allBudgets_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  # we need the current year to get the current projects
  applicationCycle = getCurrentCycle()
  # All of our queries
  faculty = getFacultyWithProjects(applicationCycle.year)
  proj = getAllCurrentProjects()
  programs = getAllPrograms()
  budget = getAllBudgets()
  params = getParameters()
  downloadFileName = getFilename("allBudgets")

  return render_template (  "allBudgets.html",
                            proj = proj,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            progs = programs,
                            budg = budget,
                            params = params,
                            downloadFileName = downloadFileName
                          )
