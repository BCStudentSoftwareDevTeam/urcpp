from ..everything import *
from ..API.faculty import getFacultyWithProjects
from ..API.parameters import getCurrentParameters
from ..API.makeExcel import getFilename
from ..pages import *

@app.route("/committee/allLabor", methods = ["GET"])
@login_required
def allLabor_GET ():
  if not g.user.isCommitteeMember:
    abort(403)
  # TODO: choose get parameter or application year
  # we need the year so that we can get the current projects
  parameters = getCurrentParameters()
  # All of our queries
  faculty = getFacultyWithProjects(parameters.year)
  
  downloadFileName = getFilename("allLabor")
  
  return render_template (  "committee/allLabor.html",
                            username = g.user.username,
                            cfg = cfg,
                            fac = faculty,
                            params = parameters,
                            downloadFileName = downloadFileName
                          )
