from everything import *
from faculty import getFacultyWithProjects
from parameters import getParameters
from makeExcel import getFilename
from applicationCycle import getCurrentCycle
from pages import *

@app.route("/committee/allLabor", methods = ["GET"])
@login_required
def allLabor_GET ():
  if not g.user.isCommitteeMember:
    abort(403)
  # TODO: choose get parameter or application year
  # we need the year so that we can get the current projects
  applicationCycle =  getCurrentCycle()
  # All of our queries
  faculty = getFacultyWithProjects(applicationCycle.year)
  parameters = getParameters()
  downloadFileName = getFilename("allLabor")
  
  return render_template (  "allLabor.html",
                            username = g.user.username,
                            cfg = cfg,
                            fac = faculty,
                            params = parameters,
                            downloadFileName = downloadFileName
                          )
