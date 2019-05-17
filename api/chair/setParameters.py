from ..everything import *
from ..redirectback import redirect_url
import datetime
from ..API.parameters import getCurrentParameters


@app.route("/chair/setParameters", methods = ["GET", "POST"])
@login_required
def setParameters_GET ():
  if not g.user.isChair:
    abort(403)
  if request.method == 'POST':
    data = request.form
    openDate = datetime.datetime.strptime(data['applicationOpenDate'], '%Y-%m-%d')
    closeDate = (datetime.datetime
                         .strptime(data['applicationCloseDate'], '%Y-%m-%d')
                         .replace(hour=11, minute=55) )
    parameters = Parameters(year = int(data['newYear']),
                            appOpenDate = openDate,
                            appCloseDate =closeDate,
                            mileageRate = data['mileageRate'],
                            laborRate = data['laborRate'])
    
    parameters.save()
    
    flash('New application year succesfully created')
    return redirect(url_for('setParameters_GET', username = g.user.username))
    
  parameters = getCurrentParameters()
  parameters_list = Parameters.select().order_by(-Parameters.year)
  
  return render_template ("chair/setParameters.html", 
                           username = g.user.username,
                           ldap = g.user,
                           params = parameters,
                           parameters_list = parameters_list,
                           cfg = cfg,
                           )
                           
@app.route("/delete/parameters/<pID>", methods=['GET'])
@login_required
def deleteParameters(pID):
  if not g.user.isChair:
    abort(403)
  try:
    parameters = Parameters.get(Parameters.pID == pID)
    parameters.delete_instance()
  
  except Parameters.DoesNotExist:
    flash('Parameters not found')
  return redirect(redirect_url())
  
  
