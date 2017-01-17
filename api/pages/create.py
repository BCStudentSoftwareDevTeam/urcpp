import datetime
from api.everything import *
from ..API.faculty import getFaculty, getFacultyByYear
from ..API.projects import getProject
from ..API.programs import getAllPrograms
from ..API.budget import getBudget
from ..API.parameters import getCurrentParameters

@app.route("/create", methods = ["GET"])
@login_required
def create_GET ():

  # All of our queries
  faculty  = getFaculty(g.user.username)
  proj = getProject(g.user.username)
  progs = getAllPrograms()
  parameters = getCurrentParameters()
  if proj is not None:
    if proj.status == cfg["projectStatus"]["pending"]:
      redirect(url_for("main"))
  
  return render_template (  "pages/create.html",
                            fac = faculty,
                            ldap = g.user,
                            proj = proj,
                            username = g.user.username,
                            cfg = cfg,
                            progs = progs,
                            params = parameters
                          )


@app.route("/create", methods = ["POST"])
@login_required
def create_POST ():
  
  # Grab the .body() from the aja() POST
  # data is an immutable dictionary
  data = request.form
  
  # First, update the project title
  proj = getProject(g.user.username)
  budg = getBudget(g.user.username)
  year = getCurrentParameters().year
  if proj is None:
    proj = Projects()
  
  if budg is None:
    budg = Budget()
    budg.save()
  
  proj.title      = data["title"]
  proj.startDate  = datetime.datetime.strptime(data["startDate"], '%m-%d-%Y')
  proj.endDate    = datetime.datetime.strptime(data["endDate"], '%m-%d-%Y')
  proj.duration   = int(data["duration"])
  proj.budgetID   = budg.bID
  proj.year       = year
  proj.isServiceToCommunity = data["isServiceToCommunity"] if "isServiceToCommunity" in data is not None else False 
  proj.hasCommunityPartner = data["hasCommunityPartner"] if "hasCommunityPartner" in data is not None else False
  proj.save()  
  
  # Next, update the faculty's program
  fac = getFacultyByYear(g.user.username, year)
  # If they don't exist yet, create one.
  if fac is None:
    fac               = URCPPFaculty()
    fac.username      = g.user.username
    fac.corresponding = True
  
  fac.pID       = proj.pID
  fac.programID = int(data["program"])
  fac.save()

  return redirect(url_for("people_GET"))
