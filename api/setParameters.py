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
    print data
    openDate = datetime.datetime.strptime(data['applicationOpenDate'], '%Y-%m-%d')
    closeDate = datetime.datetime.strptime(data['applicationCloseDate'], '%Y-%m-%d')
    parameters = Parameters(year = int(data['newYear']),
                            appOpenDate = openDate,
                            appCloseDate =closeDate,
                            mileageRate = data['mileageRate'],
                            laborRate = data['laborRate'])
    
    parameters.save()
    
    applicationCycle = ApplicationCycle(year      = int(data['newYear']),
                                        startDate = openDate,
                                        endDate   = closeDate)

    applicationCycle.save(force_insert=True)
    flash('New year succesfully created')
    
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