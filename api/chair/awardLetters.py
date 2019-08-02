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


  if faculty is not None:
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
  print("Starting emailer")
  if not g.user.isCommitteeMember:
    abort(403)
  # All of our queries

  project = Projects.get(Projects.pID == pID)
  currentCycle = getCurrentParameters() #This is for the parameter values needed in email

  # we need the current year to get current faculty with projects
  template = EmailTemplates.get(EmailTemplates.eID == 1)
  body = template.Body
  subject = template.Subject
  funding = str(getTotalBudget(project.budgetID))
  project_title = project.title
  start = str(project.startDate.strftime("%B %d, %Y"))
  end = str(project.endDate.strftime("%B %d, %Y"))
  stipend = str(project.budgetID.facultyStipend)
  faculty = URCPPFaculty.get(project.pID == URCPPFaculty.pID)
  year = str(project.startDate.strftime("%Y"))
  student = str(project.numberStudents)
  funding = str(getTotalBudget(project.budgetID)-project.budgetID.facultyStipend)
  staff_support = str(currentCycle.staffsupport_id.firstname)+" "+str(currentCycle.staffsupport_id.lastname)
  irb_chair = str(currentCycle.IRBchair_id.firstname)+" "+str(currentCycle.IRBchair_id.lastname)
  current_chair =  str(currentCycle.currentchair_id.firstname)+" "+str(currentCycle.currentchair_id.lastname)
  abstract_date = str(currentCycle.AbstractnarrativesAcceptanceDate)
  print("Still getting email ready")
  # print("Staaaaaaaaaaaaaaa",staff_support)
  # Replace all placeholder text
  body = body.replace("@@Students@@", student)
  body = body.replace("@@Year@@", year)
  body = body.replace("@@Today's Date@@", str(datetime.datetime.now().strftime("%m/%d/%y")))
  body = body.replace("@@Faculty@@",faculty.username.firstname+ " " +faculty.username.lastname)
  body = body.replace("@@Funding@@",funding)
  body = body.replace("@@ProjectTitle@@",project_title)
  body = body.replace("@@Start Date@@",start)
  body = body.replace("@@End Date@@",end)
  body = body.replace("@@Stipend@@",stipend)
  body = body.replace("@@Staff Support@@",staff_support)
  body = body.replace("@@IRB Chair@@",irb_chair)
  body = body.replace("@@Current Chair@@",current_chair)
  body = body.replace("@@Abstract Due Date@@",abstract_date)
  email_address = "%s@berea.edu" % (str(faculty.username.username))
  try:

    acceptance_email = create_message(subject, email_address, body)
    print('Acc email: ', acceptance_email.html)
    mail.send(acceptance_email)
    print("Sent the email")
  except Exception as e:
      print("Emailer failed", e)
      return jsonify({"mail_to": "Failed to send email with error: %s" % (e)})

  return jsonify({"mail_to":"Email sent to: %s"  % (email_address) })

@app.route("/chair/awardLetters/get/<pID>", methods = ["GET"])
@login_required
def accept_letters_get(pID):
  if not g.user.isCommitteeMember:
    abort(403)
  # All of our queries

  project = Projects.get(Projects.pID == pID)
  currentCycle = getCurrentParameters() #This is for the parameter values needed in email
  # we need the current year to get current faculty with projects
  template = EmailTemplates.get(EmailTemplates.eID == 1)
  body = template.Body
  subject = template.Subject
  funding = str(getTotalBudget(project.budgetID)-project.budgetID.facultyStipend)
  project_title = project.title
  student_count = str(project.numberStudents)
  start = str(project.startDate.strftime("%B %d, %Y"))
  end = str(project.endDate.strftime("%B %d, %Y"))
  stipend = str(project.budgetID.facultyStipend)
  faculty = URCPPFaculty.get(project.pID == URCPPFaculty.pID)
  year = str(project.startDate.strftime("%Y"))
  student = str(project.numberStudents)
  staff_support = str(currentCycle.staffsupport_id.firstname)+" "+str(currentCycle.staffsupport_id.lastname)
  irb_chair = str(currentCycle.IRBchair_id.firstname)+" "+str(currentCycle.IRBchair_id.lastname)
  current_chair =  str(currentCycle.currentchair_id.firstname)+" "+str(currentCycle.currentchair_id.lastname)
  abstract_date = str(currentCycle.AbstractnarrativesAcceptanceDate)

  # Replace all placeholder text
  body = body.replace("@@Students@@", student)
  body = body.replace("@@Year@@", year)
  body = body.replace("@@Date@@", str(datetime.datetime.now().strftime("%m/%d/%y")))
  body = body.replace("@@Faculty@@",faculty.username.firstname+ " " +faculty.username.lastname)
  body = body.replace("@@Funding@@",funding)
  body = body.replace("@@ProjectTitle@@",project_title)
  body = body.replace("@@Start Date@@",start)
  body = body.replace("@@End Date@@",end)
  body = body.replace("@@Stipend@@",stipend)
  body = body.replace("@@Staff Support@@",staff_support)
  body = body.replace("@@IRB Chair@@",irb_chair)
  body = body.replace("@@Current Chair@@",current_chair)
  body = body.replace("@@Abstract Due Date@@",abstract_date)

  return jsonify({"body": body, "subject":subject})
