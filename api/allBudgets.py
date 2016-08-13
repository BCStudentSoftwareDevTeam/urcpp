from everything import *
from applicationCycle import getCurrentCycle
from faculty import getFaculty, getLDAPFaculty, getFacultyWithProjects
from projects import getAllProjects
from programs import getAllPrograms
from budget import getAllBudgets
from parameters import getParameters
from makeExcel import getFilename

from pages import *

@app.route("/<username>/committee/allBudgets", methods = ["GET"])
def allBudgets_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  # All of our queries
  faculty = getFacultyWithProjects()
  proj = getAllProjects()
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
