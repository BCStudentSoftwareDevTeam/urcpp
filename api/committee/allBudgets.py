from api.everything import *
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
  params = getParameters()
  # All of our queries
  faculty = getFacultyWithProjects(params.year)
  
  downloadFileName = getFilename("allBudgets")

  return render_template (  "allBudgets.html",
                            username = g.user.username,
                            cfg = cfg,
                            fac = faculty,
                            params = params,
                            downloadFileName = downloadFileName
                          )
