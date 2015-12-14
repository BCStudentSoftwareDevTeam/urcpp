from everything import *
from faculty import getFaculty, getLDAPFaculty, getFacultyWithProjects
from projects import getAllProjects
from programs import getAllPrograms
from budget import getAllBudgets
from upload import checkForFile
from parameters import getParameters

from pages import *

import os, pprint, zipfile
import shutil


def zipdir(path, ziph):
    # ziph is zipfile handle
    zipf = zipfile.ZipFile('Python.zip', 'w')
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            
            
@app.route("/<username>/committee/allFiles", methods = ["GET"])
def allFiles_GET (username):
  # All of our queries
  faculty = getFacultyWithProjects()
  proj = getAllProjects()
  programs = getAllPrograms()
  budget = getAllBudgets()
  parameters = getParameters()
  prevFilepath = {}
  for fac in faculty:
    prevFilepath[fac.username.username] = {}
    for uploadType in ["narrative", "vitae", "irb"]: 
      if checkForFile(fac.username.username, uploadType) != "":
        prevFilepath[fac.username.username][uploadType]= checkForFile(fac.username.username, uploadType)

  # # do zipping  
  # zipf = zipfile.ZipFile("api/static/files/" + str(parameters.year) + "/" + str(parameters.year) + ".zip", 'w')
  # zipdir('static/files/' + str(parameters.year), zipf)
  # zipf.close()
  
  shutil.make_archive("api/static/files/" + str(parameters.year), 'zip', 'api/static/files/' + str(parameters.year))
  
  return render_template (  "allFiles.html",
                            proj = proj,
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            progs = programs,
                            budg = budget,
                            files = prevFilepath,
                            params = parameters
                          )
