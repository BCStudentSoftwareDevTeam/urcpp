from ..everything import *
from ..API.parameters import getCurrentParameters
from forms import ManageCommitteeForm
from ..API.committee import addCommitteeMembers, removeCommitteeMembers, getCommitteeMembers
from ..API.faculty import getFacultyWithAcceptedProjects
from ..API.budget import getTotalBudget


from ..pages import *

@app.route("/chair/awardLetters", methods = ["GET"])
@login_required
def awardLetters ():
  if not g.user.isCommitteeMember:
    abort(403)
  # All of our queries
  # we need the current year to get current faculty with projects
  currentCycle = getCurrentParameters()
  faculty =  getFacultyWithAcceptedProjects(currentCycle.year)
  funding = {}
  for entry in faculty:
    bID = entry.pID.budgetID
    funding[bID] = getTotalBudget(bID)
  return render_template (  "chair/awardLetters.html",
                            username = g.user.username,
                            cfg = cfg,
                            fac = faculty,
                            funding = funding,
                          )

@app.route("/chair/awardLetters/save", methods = ["POST"])
@login_required
def awardLetters_save ():
  if not g.user.isCommitteeMember:
    abort(403)
  # All of our queries
  # we need the current year to get current faculty with projects
  template = EmailTemplates.get(EmailTemplates.eID == 1)
  template.Body = request.form['body']
  template.Subject = request.form['subject']  
  template.save()
  template = EmailTemplates.get(EmailTemplates.eID == 1)
  return jsonify({"success": True})

@app.route("/chair/awardLetters/get", methods = ["GET"])
@login_required
def awardLetters_get ():
  if not g.user.isCommitteeMember:
    abort(403)
  # All of our queries
  # we need the current year to get current faculty with projects
  template = EmailTemplates.get(EmailTemplates.eID == 1)
  body = template.Body
  subject = template.Subject
  return jsonify({"body": body, "subject":subject})
  
@app.route("/chair/awardLetters/generate/<username>/<pID>", methods = ["GET"])
@login_required
def awardLetters_generate(username,pID):
  if not g.user.isCommitteeMember:
    abort(403)
  # All of our queries
  print(pID)
  project = Projects.get(Projects.pID == pID)
  # we need the current year to get current faculty with projects
  template = EmailTemplates.get(EmailTemplates.eID == 1)
  body = template.Body
  subject = template.Subject
  funding = str(getTotalBudget(project.budgetID))
  project_title = project.title
  student_count = str(project.numberStudents)
  start = str(project.startDate.strftime("%B %d, %Y"))
  end = str(project.endDate.strftime("%B %d, %Y"))
  stipend = str(project.budgetID.facultyStipend)
  
  # Replace all placeholder text
  body = body.replace("@@Funding@@",funding)
  body = body.replace("@@ProjectTitle@@",project_title)
  body = body.replace("@@Students@@",student_count)
  body = body.replace("@@Start Date@@",start)
  body = body.replace("@@End Date@@",end)
  body = body.replace("@@Stipend@@",stipend)
  
  mail_to = "mailto:%s@berea.edu?subject=%s&body=%s" % (username, subject, body)
  
  #Replace common html tags to ascii hex values
  mail_to = mail_to.replace("&nbsp;"," ")
  mail_to = mail_to.replace("&ldquo;","%22")
  mail_to = mail_to.replace("&rdquo;","%22")
  mail_to = mail_to.replace("&rsquo;","%27")
  mail_to = mail_to.replace(" ", "%20")
  mail_to = mail_to.replace("\n", "%0A")
  mail_to = mail_to.replace("<p>","")
  mail_to = mail_to.replace("</p>","%0A")
  
  return jsonify({"mail_to": mail_to})
  
  