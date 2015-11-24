from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from collaborators import getCollaborators
from budget import getBudget
import os

def validPageTemplate (page):
  return page in os.listdir(cfg["filepaths"]["pageTemplates"])

# This looks like file upload, but it isn't.
# This renders a "generic" upload page, where the upload type
# is one of three types. The page configures itself based 
# on the type of upload being requested.
@app.route("/urcpp/<username>/upload/<uploadType>", methods = ["GET"])
def generic_file_upload (username, uploadType):
  if uploadType in cfg["filepaths"]["allowedFileNames"]:
    # All of our queries
    faculty = getFaculty(username)
    ldapFaculty = getLDAPFaculty(username)
    proj = getProject(username)
    programs = getAllPrograms()
    collaborators = getCollaborators(username)
    budget = getBudget(username)
    
    
    return render_template (  "upload.html",
                              proj = proj,
                              username = username,
                              cfg = cfg,
                              fac = faculty,
                              ldap = ldapFaculty,
                              uploadType = uploadType
                            )
  else:
    return "File upload type not recognized."
    
  
@app.route("/urcpp/<username>/<page>", methods = ["GET"])
def generic_page_get (username, page):
  if validPageTemplate (page + ".html"):
    # All of our queries
    faculty = getFaculty(username)
    ldapFaculty = getLDAPFaculty(username)
    proj = getProject(username)
    programs = getAllPrograms()
    collaborators = getCollaborators(username)
    budget = getBudget(username)
    
    
    return render_template (  page + ".html",
                              proj = proj,
                              username = username,
                              cfg = cfg,
                              fac = faculty,
                              ldap = ldapFaculty,
                              progs = programs,
                              collabs = collaborators,
                              budg = budget
                            )
  else:
    return "Page not found. 404 or something."