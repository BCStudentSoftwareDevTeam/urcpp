from api.everything import *
from api.applicationCycle import getCurrentCycle
from api.faculty import getFacultyWithProjects
from api.parameters import getParameters
from api.makeExcel import getFilename

from api.pages import *


@app.route("/committee/allBudgets", methods = ["GET"])
@login_required
def allBudgets_GET ():
  if not g.user.isCommitteeMember:
    return abort(403)
  
  # we need the current year to get the current projects
  # TODO: either keep this or keep line 22 not both
  applicationCycle = getCurrentCycle()
  # All of our queries
  faculty = getFacultyWithProjects(applicationCycle.year)
  params = getParameters()
  downloadFileName = getFilename("allBudgets")

  return render_template (  "allBudgets.html",
                            username = g.user.username,
                            cfg = cfg,
                            fac = faculty,
                            params = params,
                            downloadFileName = downloadFileName
                          )
