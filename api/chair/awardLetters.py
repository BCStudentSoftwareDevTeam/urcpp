from ..everything import *
from ..API.parameters import getCurrentParameters
from forms import ManageCommitteeForm
from ..API.committee import addCommitteeMembers, removeCommitteeMembers, getCommitteeMembers
from ..API.faculty import getFacultyWithAcceptedProjects
from ..API.budget import getTotalBudget
from ..API.files import create_message


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
  template, created = EmailTemplates.get_or_create(eID = 1)
  template.Body = request.form['body']
  template.Subject = request.form['subject']  
  template.save()
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
  
@app.route("/chair/awardLetters/send/<username>/<pID>", methods = ["GET"])
@login_required
def awardLetters_generate(username,pID):
  if not g.user.isCommitteeMember:
    abort(403)
  # All of our queries
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
  email_address = "%s@berea.edu" % (username)
  try:
    acceptance_email = create_message(subject, email_address , body)
    mail.send(acceptance_email)
  except Exception as e:
      return {"mail_to": "Failed to send email to: %s" % (email_address)}

  return jsonify({"mail_to":"Email sent to: %s"  % (email_address) })
