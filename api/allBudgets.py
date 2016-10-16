from everything import *
from applicationCycle import getCurrentCycle
from faculty import getFacultyWithProjects
from parameters import getParameters
from makeExcel import getFilename

from pages import *

@app.route("/<username>/committee/allBudgets", methods = ["GET"])
def allBudgets_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  # we need the current year to get the current projects
  # TODO: either keep this or keep line 22 not both
  applicationCycle = getCurrentCycle()
  # All of our queries
  faculty = getFacultyWithProjects(applicationCycle.year)
  params = getParameters()
  downloadFileName = getFilename("allBudgets")

  return render_template (  "allBudgets.html",
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            params = params,
                            downloadFileName = downloadFileName
                          )
