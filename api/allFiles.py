from everything import *
from faculty import getFacultyWithProjects
from upload import checkForFile
from parameters import getParameters
from flask import send_file
from applicationCycle import getCurrentCycle

from pages import *

import os, pprint, zipfile, uuid, time
import shutil

# remove all folders that are not user folders and are older than one minute


@app.route("/<username>/committee/allFiles", methods = ["GET"])

def allFiles_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  here = os.path.dirname(__file__)
  
  # we need the year to the current projects
  # TODO: remove application cycle or get parameters
  applicationCycle = getCurrentCycle()
  # All of our queries
  faculty = getFacultyWithProjects(applicationCycle.year)
  parameters = getParameters()
  prevFilepath = {}
  
  yearDir = cfg["filepaths"]["projectFiles"]+str(parameters.year)
  yearDir = os.path.join(here, yearDir)
  projectDir = cfg["filepaths"]["projectFiles"]

  projectDir = os.path.join(here, projectDir)
  if faculty:
    for fac in faculty:
      prevFilepath[fac.username.username] = {}
      for uploadType in ["narrative", "vitae", "irb"]: 
        if checkForFile(fac.username.username, uploadType, applicationCycle.year) != "":
          prevFilepath[fac.username.username][uploadType]= checkForFile(fac.username.username, uploadType, applicationCycle.year)
      allFac = [fac.username.username for fac in faculty]

  # Does the zipping
  shutil.make_archive(yearDir, 'zip', yearDir)
    
  allFolders = os.walk(yearDir).next()[1]

  
  

  for folder in allFolders:
    fullPath =  yearDir + "/" + str(folder)
    if (folder not in allFac) and (os.stat(fullPath).st_mtime < time.time() - 60*30):
      shutil.rmtree(fullPath)
    

  return render_template (  "allFiles.html",
                            username = username,
                            cfg = cfg,
                            fac = faculty,
                            files = prevFilepath,
                            params = parameters
                          )
                          
@app.route("/<username>/committee/allFiles", methods = ["POST"])
def allFiles_POST (username):
  if username != authUser(request.environ):
    return { "response": projectDir}
    
  # All of our queries
  parameters = getParameters()
  prevFilepath = {}
  
  here = os.path.dirname(__file__)
  yearDir = cfg["filepaths"]["projectFiles"]+str(parameters.year)
  yearDir = os.path.join(here, yearDir)

  
  try:
    os.stat(yearDir)
  except:
    os.mkdir(yearDir)
  allfiles = '{0}{1}'.format(yearDir, '.zip')
    
  
  return send_file(allfiles)
