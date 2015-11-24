from everything import *

import os

def validPageTemplate (page):
  return page in os.listdir(cfg["filepaths"]["pageTemplates"])


# def genericPageGet (username, page):
#   if validPageTemplate (page + ".html"):
#     # All of our queries
#     faculty = getFaculty(username)
#     ldapFaculty = getLDAPFaculty(username)
#     proj = getProject(username)
#     programs = getAllPrograms()
#     # Who knew... the collaborators all go through
#     # as LDAPFaculty objects...
#     collaborators = getCollaborators(username)
#     budget = getBudget(username)
    
    
#     return render_template (  page + ".html",
#                               proj = proj,
#                               username = username,
#                               cfg = cfg,
#                               fac = faculty,
#                               ldap = ldapFaculty,
#                               progs = programs,
#                               collabs = collaborators,
#                               budg = budget,
#                             )
#   else:
#     return "Page not found. 404 or something."

# @app.route("/urcpp/<username>/<page>", methods = ["GET"])
# def generic_page_get (username, page):
#   return _generic_page_get (username, page)
