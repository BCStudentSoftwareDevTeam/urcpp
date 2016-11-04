# from everything import *
# from faculty import getFaculty, getLDAPFaculty
# from projects import getProject
# from programs import getAllPrograms
# from collaborators import getCollaborators
# from pages.budget import getBudget
# from pages import *
# from applicationCycle import getCurrentCycle
# from datetime import datetime

# @app.route("/dashboard", methods = ["GET"])
# def dashboard():
#   username = authUser(request.environ)
#   # print(pprint.pformat (request.environ, depth = 5))
#   print username  
#   ldap = getLDAPFaculty(username)
#   project = getProject(username)
#   currentCycle = getCurrentCycle()
#   today = datetime.now()

#   return render_template ("dashboard.html", 
#                           username = username,
#                           ldap = ldap,
#                           proj = project,
#                           cfg = cfg,
#                           currentCycle = currentCycle,
#                           today = today
#                           )