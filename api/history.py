from everything import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from collaborators import getCollaborators
from budget import getBudget

from pages import validPageTemplate


@app.route("/<username>/history", methods = ["GET"])
def history_GET (username):
  # All of our queries
  faculty = getFaculty(username)
  ldapFaculty = getLDAPFaculty(username)
  proj = getProject(username)
  programs = getAllPrograms()
  # Who knew... the collaborators all go through
  # as LDAPFaculty objects...
  collaborators = getCollaborators(username)
  budget = getBudget(username)
  
  
  return render_template (  "history.html",
                            proj = proj,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            ldap = ldapFaculty,
                            progs = programs,
                            collabs = collaborators
                          )
                          
@app.route("/<username>/history", methods = ["POST"])
def history_POST (username):
  # Form data looks like...
  
  # name={{fid}}-{{when}}
  # where the when items are from the config for history.
  
  
  
  # FIXME (minor)
  # I haven't been having luck with redirecting automatically
  # from the POST pages... if someone can focus on that, 
  # it would be good. I just might be tired.
  # nextPage = cfg["flow"]["people"]
  
  return redirect (  "/{0}/upload/vitae".format(username) )
