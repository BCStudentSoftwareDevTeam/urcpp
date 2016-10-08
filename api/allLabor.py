from everything import *
from faculty import getFacultyWithProjects
from projects import getAllCurrentProjects
from programs import getAllPrograms
from budget import getAllBudgets
from parameters import getParameters
from makeExcel import getFilename

from pages import *

@app.route("/<username>/committee/allLabor", methods = ["GET"])
def allLabor_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  # All of our queries
  faculty = getFacultyWithProjects()
  project = getAllCurrentProjects()
  programs = getAllPrograms()
  budget = getAllBudgets()
  parameters = getParameters()
  downloadFileName = getFilename("allLabor")
  
  return render_template (  "allLabor.html",
                            proj = project,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            progs = programs,
                            budg = budget,
                            params = parameters,
                            downloadFileName = downloadFileName
                          )
