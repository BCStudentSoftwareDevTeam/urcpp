import datetime
from everything import *
from faculty import getFaculty, getFacultyByYear, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from budget import getBudget
from parameters import getParameters
from applicationCycle import getCurrentCycle
from pages import *

@app.route("/<username>/create", methods = ["GET"])
def create_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }

  # All of our queries
  faculty = getFaculty(username)
  ldapFaculty = getLDAPFaculty(username)
  proj = getProject(username)
  progs = getAllPrograms()
  parameters = getParameters()
  
  return render_template (  "create.html",
                            proj = proj,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            ldap = ldapFaculty,
                            progs = progs,
                            params = parameters
                          )

@app.route("/<username>/create", methods = ["POST"])
def create_POST (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }

  # Grab the .body() from the aja() POST
  data = request.form
  print "Post data is: " + str(data)
  # This is what our post from this page looks like
  # {duration: "8", program: "1", startDate: "May 1", title: "URCPP Software Also"}
  
  # First, update the project title
  proj = getProject(username)
  budg = getBudget(username)
  year = getCurrentCycle().year
  if proj is None:
    proj = Projects()
  
  if budg is None:
    budg = Budget()
    budg.save()
  
  proj.title      = data["title"]
  #  print "Date is: " + data["startDate"]
  proj.startDate  = datetime.datetime.strptime(data["startDate"], '%m-%d-%Y')
  proj.endDate    = datetime.datetime.strptime(data["endDate"], '%m-%d-%Y')
  proj.duration   = int(data["duration"])
  proj.budgetID   = budg.bID
  proj.year       = year
  # print (data["isServiceToCommunity"] if data["isServiceToCommunity"] is not None else False)
  # print (data["hasCommunityPartner"] if data["hasCommunityPartner"] is not None else False)
  proj.isServiceToCommunity = data["isServiceToCommunity"] if "isServiceToCommunity" in data is not None else False 
  proj.hasCommunityPartner = data["hasCommunityPartner"] if "hasCommunityPartner" in data is not None else False
  proj.save()  
  
  # Next, update the faculty's program
  fac = getFacultyByYear(username, year)
  # If they don't exist yet, create one.
  if fac is None:
    fac               = URCPPFaculty()
    fac.username      = username
    fac.corresponding = True
  
  fac.pID       = proj.pID
  fac.programID = int(data["program"])
  fac.save()

  return redirect(username + '/people')
