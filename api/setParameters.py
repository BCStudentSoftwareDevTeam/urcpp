from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from budget import getBudget
from parameters import getParameters
import datetime

from pages import *

@app.route("/<username>/chair/setParameters", methods = ["GET", "POST"])
def setParameters_GET (username):
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
    return redirect(url_for('setParameters_GET', username = username))
    
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  parameters = getParameters()
  ldap = getLDAPFaculty(username)
  
  return render_template ("setParameters.html", 
                           username = username,
                           ldap = ldap,
                           params = parameters,
                           cfg = cfg,
                           )
