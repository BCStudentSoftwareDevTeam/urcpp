from api.flask_imports import *

from ..everything import cfg
from api.models import *

from api.committee import committee
from ..API.parameters import getCurrentParameters

from ..pages import *

@committee.route("/committee", methods = ["GET"])
@login_required
def committee_GET ():
  if not g.user.isCommitteeMember:
    abort(403)
  parameters = getCurrentParameters()

  return render_template ("committee/committee.html",
                           username = g.user.username,
                           ldap = g.user,
                           params = parameters,
                           cfg = cfg,

                           )
