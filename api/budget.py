from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from parameters import getParameters
from applicationCycle import getCurrentCycle
import math

def getBudget (username):
   proj = getProject(username);
   if proj:
     budgQ = (Budget.select()
          .where (Budget.bID == projQ.budgetID)
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
  
@app.route("/<username>/budget", methods = ["GET"])
def budget_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  # All of our queries
  faculty = getFaculty(username)
  ldapFaculty = getLDAPFaculty(username)
  proj = getProject(username)
  programs = getAllPrograms()
  budget = getBudget(username)
  parameters = getParameters()

  return render_template (  "budget.html",
                            proj = proj,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            ldap = ldapFaculty,
                            progs = programs,
                            budg = budget,
                            params = parameters
                          )
                          
@app.route("/<username>/budget", methods = ["POST"])
def budget_POST (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  data = request.form
  # Data looks like:
  # [('equipment', u'40'), ('milesDesc', u'And go farther, not further'), 
  # ('materials', u'50'), ('facultyStipendDesc', u'Faculty get rich'), 
  # ('materialsDesc', u'To build more stuff'), ('otherTravelDesc', 
  # u'In planes and trains and automobiles'), ('miles', u'20'), 
  # ('otherDesc', u'And other stuff'), ('facultyStipend', u'10'), 
  # ('otherTravel', u'30111'), ('total', u'30291'), ('other', u'60'), 
  # ('equipmentDesc', u'With stuff')]
  # print data
  
  print "Data loaded"
  budg = getBudget(username)
  
  if budg is None:
    budg = Budget()
    budg.save()
  
  print "Saving budget data to db"
  print int(round(float(data["facultyStipend"])))
  budg.facultyStipend       = int(round(float(data["facultyStipend"])))
  print budg.facultyStipend
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
  
  print "Done saving budget data to db"
  return redirect(username + '/done')
