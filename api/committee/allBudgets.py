from api.flask_imports import *

from ..everything import cfg
from api.models import *

from api.committee import committee

from ..API.faculty import getFacultyWithProjects
from ..API.parameters import getCurrentParameters
from ..API.parameters import getParametersByYear
from ..API.makeExcel import getFilename

from ..pages import *


@committee.route("/committee/allBudgets", methods = ["GET"])
@committee.route("/committee/allBudgets/<int:year>", methods = ["GET"])
@login_required
def allBudgets(year=None):
  if not g.user.isCommitteeMember:
    return abort(403)

  if year is None:
    params = getCurrentParameters()
  else:
    flash("You are viewing budgets from applicationCycle {}".format(year), 'warning')
    params = getParametersByYear(year)


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
