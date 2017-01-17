from ..everything import *
from ..API.faculty import getFacultyWithProjects
from ..pages.upload import checkForFile
from ..API.parameters import getCurrentParameters
from flask import send_file

import os, pprint, zipfile, uuid, time
import shutil

# remove all folders that are not user folders and are older than one minute


@app.route("/committee/allFiles", methods = ["GET"])
@login_required
def allFiles_GET ():
  if not g.user.isCommitteeMember:
    abort(403)
  
  # we need the year to the current projects
  # TODO: remove application cycle or get parameters
  parameters = getCurrentParameters()
  # All of our queries
  faculty = getFacultyWithProjects(parameters.year)
  prevFilepath = {}
  
  yearDir = cfg["filepaths"]["projectFiles"]+str(parameters.year)
  yearDir = os.path.join(base_path ,yearDir)
  # I don't think this is needed anymore #######
  projectDir = cfg["filepaths"]["projectFiles"]

  projectDir = os.path.join(base_path, projectDir)
  ##############################################
  if faculty:
    for fac in faculty:
      prevFilepath[fac.username.username] = {}
      for uploadType in ["narrative", "vitae", "irb"]: 
        if checkForFile(fac.username.username, uploadType, parameters.year) != "":
          prevFilepath[fac.username.username][uploadType]= checkForFile(fac.username.username, uploadType, parameters.year)
      allFac = [fac.username.username for fac in faculty]

  # Does the zipping
  shutil.make_archive(yearDir, 'zip', yearDir)
    
  allFolders = os.walk(yearDir).next()[1]

  
  

  for folder in allFolders:
    fullPath =  yearDir + "/" + str(folder)
    if (folder not in allFac) and (os.stat(fullPath).st_mtime < time.time() - 60*30):
      shutil.rmtree(fullPath)
    

  return render_template (  "allFiles.html",
                            username = g.user.username,
                            cfg = cfg,
                            fac = faculty,
                            files = prevFilepath,
                            params = parameters
                          )
                          
@app.route("/committee/allFiles", methods = ["POST"])
@login_required
def allFiles_POST ():
  if not g.user.isCommitteeMember:
    abort(403)
    
  # All of our queries
  parameters = getCurrentParameters()
  prevFilepath = {}
  
  yearDir = cfg["filepaths"]["projectFiles"]+str(parameters.year)
  yearDir = os.path.join(base_path, yearDir)

  
  try:
    os.stat(yearDir)
  except:
    os.mkdir(yearDir)
  allfiles = '{0}{1}'.format(yearDir, '.zip')
    
  
  return send_file(allfiles)
