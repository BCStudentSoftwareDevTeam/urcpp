from api.everything import *
from api.faculty import getFacultyWithProjects
from api.parameters import getParameters
from api.makeExcel import getFilename
from api.applicationCycle import getCurrentCycle
from api.pages import *

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
