from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from parameters import getParameters

def getBudget (username):
   budgQ = (Budget.select()
      .join (URCPPFaculty, on = (URCPPFaculty.pID == Projects.pID))
      .join (Projects, on = (Projects.budgetID == Budget.bID))
      .where (URCPPFaculty.username == username)
      )
   
   app.logger.info("Looking for budget with query:\n\n" + budgQ + "\n\n")
   
   if budgQ.exists():
      return budgQ.get()
   else:
      return None

def getAllBudgets ():
   budgQ = (Budget.select())
   
   app.logger.info("Looking for all budgets with query:\n\n" + budgQ + "\n\n")
   
   if budgQ.exists():
      return budgQ.execute()
   else:
      return None

@app.route("/<username>/budget", methods = ["GET"])
def budget_GET (username):
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
  
  budg.facultyStipend       = data["facultyStipend"]
  budg.facultyStipendDesc   = data["facultyStipendDesc"]
  budg.miles                = data["miles"]
  budg.milesDesc            = data["milesDesc"]
  budg.otherTravel          = data["otherTravel"]
  budg.otherTravelDesc      = data["otherTravelDesc"]
  budg.equipment            = data["equipment"]
  budg.equipmentDesc        = data["equipmentDesc"]
  budg.materials            = data["materials"]
  budg.materialsDesc        = data["materialsDesc"]
  budg.other                = data["other"]
  budg.otherDesc            = data["otherDesc"]
  budg.save()
  
  print "Done saving budget data to db"
  return redirect(username + '/done')