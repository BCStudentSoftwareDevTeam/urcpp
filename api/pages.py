from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms

import os

def validPageTemplate (page):
  return page in os.listdir(cfg["filepaths"]["pageTemplates"])

@app.route("/urcpp/<username>/<page>", methods = ["GET"])
def create (username, page):
  if validPageTemplate (page + ".html"):
    fac = getFaculty(username)
    ldap = getLDAPFaculty(username)
    proj = getProject(username)
    progs = getAllPrograms()
    
    return render_template (  page + ".html",
                              proj = proj,
                              username = username,
                              cfg = cfg,
                              fac = fac,
                              ldap = ldap,
                              progs = progs
                            )
                              