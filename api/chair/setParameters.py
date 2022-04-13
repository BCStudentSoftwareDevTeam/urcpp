from ..everything import *
from ..redirectback import redirect_url
import datetime
from ..API.parameters import getCurrentParameters

dateFormat = '%m/%d/%Y'
@app.route("/chair/setParameters", methods = ["GET", "POST"])
@login_required
def setParameters_GET ():
  if not g.user.isChair:
    abort(403)
  if request.method == 'POST':
    data = request.form
    openDate = datetime.datetime.strptime(data['applicationOpenDate'], dateFormat)
    closeDate = (datetime.datetime
                         .strptime(data['applicationCloseDate'], dateFormat)
                         .replace(hour=23, minute=59) )
#    ProposalOpenDate = datetime.datetime.strptime(data['ProposalOpenDate'], dateFormat)
    ProposalAcceptanceDate = datetime.datetime.strptime(data['ProposalAcceptanceDate'], dateFormat)
#    ProposalClosedDate = ( datetime.datetime.strptime(data['ProposalClosedDate'], dateFormat).replace(hour=11, minute=55) )

 #   AbstractnarrativesAcceptanceDate = ( datetime.datetime.strptime(data['AbstractnarrativesAcceptanceDate'], dateFormat).replace(hour=11, minute=55) )

    AllSubmissionsClosedDate = ( datetime.datetime.strptime(data['AllSubmissionsClosedDate'], dateFormat)
						  .replace(hour=23, minute=59) )



    try:
	    parameters = Parameters.get(year = int(data['newYear']))
    except:
	    parameters = Parameters.create(year = int(data['newYear']),
					   appOpenDate = openDate,
					   appCloseDate = closeDate,
					   mileageRate = data['mileageRate'],
					   laborRate = data['laborRate'],
					   isCurrentParameter = False,
                       stipend = data['stipend']
			 )

    print("Date: ", data['applicationOpenDate'])
    parameters.IRBchair_id = data['IRBchair_id']
    parameters.currentchair_id = data['currentchair_id']
    parameters.staffsupport_id = data['staffsupport_id']
    parameters.appOpenDate = openDate
    parameters.appCloseDate = closeDate
  #  parameters.ProposalOpenDate = ProposalOpenDate
    parameters.ProposalAcceptanceDate = ProposalAcceptanceDate
  #  parameters.ProposalClosedDate = ProposalClosedDate
  #  parameters.AbstractnarrativesAcceptanceDate = AbstractnarrativesAcceptanceDate
    parameters.AllSubmissionsClosedDate = AllSubmissionsClosedDate
    parameters.mileageRate = data['mileageRate']
    parameters.laborRate = data['laborRate']
    parameters.stipend = data['stipend']

    parameters.save()

    flash("Successfully saved" , "success")
    return redirect(url_for('setParameters_GET', username = g.user.username))

  parameters = getCurrentParameters()
  parameters_list = Parameters.select().order_by(-Parameters.year)
  faculty = LDAPFaculty.select() # retrieves all the faculty from the data base
  return render_template ("chair/setParameters.html",
                           username = g.user.username,
                           ldap = g.user,
                           params = parameters,
                           parameters_list = parameters_list,
                           cfg = cfg,
                           allfaculty = faculty,
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
    flash("Parameters not found" , "danger")
  return redirect(redirect_url())
