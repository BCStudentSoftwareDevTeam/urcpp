from ..everything import *
from ..API.faculty import  getFacultyWithProjects, getFacultyByYear
from ..API.parameters import getCurrentParameters
from ..API.files import removeFiles
from ..API.files import create_message

@app.route("/email/accepted", methods = ["GET"])
@login_required
def emailProjects_GET ():
  if not g.user.isChair:
    abort(403)
  # All of our queries
  # we need the current year to get current faculty with projects
  currentCycle = getCurrentParameters()

  faculty =  getFacultyWithProjects(currentCycle.year)

  return render_template (  "chair/allProjects.html",
                            username = g.user.username,
                            cfg = cfg,
                            fac = faculty,
                          )

@app.route("/email")
def email():
  '''this route is for testing purposes'''
  my_email="guillermoramos330179@gmail.com"
  msg = create_message(my_email)
  mail.send(msg)
  return "Message is sent."


@app.route("/email/<username>")
@login_required
def view_email(username):
  currentCycle = getCurrentParameters()

  faculty = getFacultyByYear(username, currentCycle.year)

  return render_template("snips/email.html",
                          person = faculty,
                          cfg = cfg)

