from ..everything import *
from ..API.projects import getProject
from ..API.parameters import getCurrentParameters

from ..API.budget import getBudget

@app.route("/budget", methods = ["GET"])
@login_required
def budget_GET ():
  
  # All of our queries
  proj = getProject(g.user.username)
  budget = getBudget(g.user.username)
  parameters = getCurrentParameters()
  
  if proj.status == cfg["projectStatus"]["Pending"]:
    flash("Application has already been submited.")
    return redirect(url_for("main_with_username", username = g.user.username))
    
  return render_template (  "pages/budget.html",
                            proj = proj,
                            username = g.user.username,
                            cfg = cfg,
                            budg = budget,
                            params = parameters
                          )

             
@app.route("/budget", methods = ["POST"])
@login_required 
def budget_POST ():
  print("Inside budget")
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
  
  print("Budget saved successfully")
  return redirect(url_for("done_GET"))
