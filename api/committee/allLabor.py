from ..everything import *
from ..API.faculty import getFacultyWithProjects
from ..API.parameters import getCurrentParameters
from ..API.parameters import getParametersByYear
from ..API.makeExcel import getFilename
from ..pages import *

@app.route("/committee/allLabor/<int:year>", methods = ["GET"])
@app.route("/committee/allLabor", methods = ["GET"])
@login_required
def allLabor(year=None):
  if not g.user.isCommitteeMember:
    abort(403)
    
  if year is None:
    parameters = getCurrentParameters()
  else:
    flash("You are viewing labor from applicationCycle: {}".format(year), 'warning')
    parameters = getParametersByYear(year)
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
