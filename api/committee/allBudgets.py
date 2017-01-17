from ..everything import *
from ..API.faculty import getFacultyWithProjects
from ..API.parameters import getCurrentParameters
from ..API.makeExcel import getFilename

from ..pages import *


@app.route("/committee/allBudgets", methods = ["GET"])
@login_required
def allBudgets_GET ():
  if not g.user.isCommitteeMember:
    return abort(403)
  
  # we need the current year to get the current projects
  # TODO: either keep this or keep line 22 not both
  params = getCurrentParameters()
  # All of our queries
  faculty = getFacultyWithProjects(params.year)
  
  downloadFileName = getFilename("allBudgets")

  return render_template (  "committee/allBudgets.html",
                            username = g.user.username,
                            cfg = cfg,
                            fac = faculty,
                            params = params,
                            downloadFileName = downloadFileName
                          )
