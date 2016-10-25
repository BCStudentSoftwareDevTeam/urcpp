from api.everything import *
from api.faculty import getFaculty, getLDAPFaculty
from api.projects import getProject
from api.programs import getAllPrograms
from api.parameters import getParameters
from api.applicationCycle import getCurrentCycle
import math

def getBudget (username):
   proj = getProject(username);
   if proj:
     budgQ = (Budget.select()
          .where (Budget.bID == proj.budgetID)
          )
     app.logger.info("Looking for budget with query:\n\n" + budgQ + "\n\n")
   
     if budgQ.exists():
        return budgQ.get()
     else:
        return None
   else:
      return None

def getAllBudgets ():
  
  year = getCurrentCycle()
  
  budgQ = (Budget.select()
            .join(Projects)
            .where(Projects.year == year))
  
  app.logger.info("Looking for all budgets with query:\n\n" + budgQ + "\n\n")
  
  if budgQ.exists():
    return budgQ.execute()
  else:
    return None

@app.route("/budget", methods = ["GET"])
@login_required
def budget_GET ():
  
  # All of our queries
  proj = getProject(g.user.username)
  programs = getAllPrograms()
  budget = getBudget(g.user.username)
  parameters = getParameters()
  
  if not proj.status == cfg["projectStatus"]["incomplete"]:
    flash("application has been submited")
    redirect(url_for("main"))

  return render_template (  "budget.html",
                            proj = proj,
                            username = g.user.username,
                            cfg = cfg,
                            budg = budget,
                            params = parameters
                          )

             
@app.route("/budget", methods = ["POST"])
@login_required 
def budget_POST ():
  
  # Data is an immutable dictionary
  data = request.form
  
  budg = getBudget(g.user.username)
  
  # we should not be able to create a budget without attaching it to a project
  # TODO: remove and replace with log and error message
  if budg is None:
    budg = Budget()
    budg.save()
  
  # what are we doing to this poor data? There must be a better way to format
  budg.facultyStipend       = int(round(float(data["facultyStipend"])))
  budg.facultyStipendDesc   = data["facultyStipendDesc"]
  budg.miles                = int(round(float(data["miles"])))
  budg.milesDesc            = data["milesDesc"]
  budg.otherTravel          = int(round(float(data["otherTravel"])))
  budg.otherTravelDesc      = data["otherTravelDesc"]
  budg.equipment            = int(round(float(data["equipment"])))
  budg.equipmentDesc        = data["equipmentDesc"]
  budg.materials            = int(round(float(data["materials"])))
  budg.materialsDesc        = data["materialsDesc"]
  budg.other                = int(round(float(data["other"])))
  budg.otherDesc            = data["otherDesc"]
  budg.save()
  
  return redirect(url_for("done_GET"))
