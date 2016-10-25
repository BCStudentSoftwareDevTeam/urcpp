from api.everything import *
from api.faculty import getFaculty, getLDAPFaculty
from api.projects import getProject
from api.programs import getAllPrograms
from api.budget import getBudget
from api.parameters import getParameters
import datetime

from api.pages import *

@app.route("/chair/setParameters", methods = ["GET", "POST"])
@login_required
def setParameters_GET ():
  if not g.user.isChair:
    abort(403)
  if request.method == 'POST':
    data = request.form
    openDate = datetime.datetime.strptime(data['applicationOpenDate'], '%Y-%m-%d')
    closeDate = datetime.datetime.strptime(data['applicationCloseDate'], '%Y-%m-%d')
    parameters = Parameters(year = int(data['newYear']),
                            appOpenDate = openDate,
                            appCloseDate =closeDate,
                            mileageRate = data['mileageRate'],
                            laborRate = data['laborRate'])
    
    parameters.save()
    
    flash('New application year succesfully created')
    return redirect(url_for('setParameters_GET', username = g.user.username))
    
  parameters = getParameters()
  parameters_list = Parameters.select().order_by(-Parameters.year)
  
  return render_template ("setParameters.html", 
                           username = g.user.username,
                           ldap = g.user,
                           params = parameters,
                           parameters_list = parameters_list,
                           cfg = cfg,
                           )
