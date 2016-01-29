from everything import *
from faculty import getFaculty, getLDAPFaculty, getFacultyWithProjects, getFacultyWithPendingProjects
from projects import getAllProjects
from programs import getAllPrograms
from budget import getAllBudgets
from upload import checkForFile
from parameters import getParameters
from collaborators import getCollaborators
from flask import send_file

from pages import *

import os, pprint, zipfile, uuid, time
import shutil

# remove all folders that are not user folders and are older than one minute


@app.route("/<username>/committee/allFiles", methods = ["GET"])

def allFiles_GET (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  # All of our queries
  faculty = getFacultyWithProjects()
  proj = getAllProjects()
  programs = getAllPrograms()
  budget = getAllBudgets()
  parameters = getParameters()
  prevFilepath = {}
  
  yearDir = cfg["filepaths"]["projectFiles"]+str(parameters.year)
  projectDir = cfg["filepaths"]["projectFiles"]
  
  for fac in faculty:
    prevFilepath[fac.username.username] = {}
    for uploadType in ["narrative", "vitae", "irb"]: 
      if checkForFile(fac.username.username, uploadType) != "":
        prevFilepath[fac.username.username][uploadType]= checkForFile(fac.username.username, uploadType)

  # Does the zipping
  shutil.make_archive(yearDir, 'zip', yearDir)
    
  allFolders = os.walk(yearDir).next()[1]
  allFac = [fac.username.username for fac in faculty]
  
  print allFolders
  print allFac

  for folder in allFolders:
    fullPath =  yearDir + "/" + str(folder)
    if (folder not in allFac) and (os.stat(fullPath).st_mtime < time.time() - 60*30):
      shutil.rmtree(fullPath)
    

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
                          
@app.route("/<username>/committee/allFiles", methods = ["POST"])
def allFiles_POST (username):
  if username != authUser(request.environ):
    return { "response": projectDir}
  # All of our queries
  faculty = getFacultyWithProjects()
  proj = getAllProjects()
  programs = getAllPrograms()
  budget = getAllBudgets()
  parameters = getParameters()
  prevFilepath = {}
  
  yearDir = cfg["filepaths"]["projectFiles"]+str(parameters.year)
  pfojectDir = cfg["filepaths"]["projectFiles"]
  
  for fac in faculty:
    prevFilepath[fac.username.username] = {}
    for uploadType in ["narrative", "vitae", "irb"]: 
      if checkForFile(fac.username.username, uploadType) != "":
        prevFilepath[fac.username.username][uploadType]= checkForFile(fac.username.username, uploadType)


  uniqueID = uuid.uuid1() 
  
  try:
    os.stat(yearDir)
  except:
    os.mkdir(yearDir)
    ##############
    # http://stackoverflow.com/questions/273192/in-python-check-if-a-directory-exists-and-create-it-if-necessary
    ##############
  os.mkdir(yearDir+"/"+str(uniqueID))
  
  facultyPending = getFacultyWithPendingProjects() 

  for fac in facultyPending:
    path = yearDir + "/"+str(uniqueID)+"/project"+str(fac.pID.pID)
    os.mkdir(path)
    for uploadType in ["narrative", "vitae", "irb"]:
            
      if checkForFile(fac.username.username, uploadType) != "":
        filename = checkForFile(fac.username.username, uploadType).split("/").pop()
        shutil.copyfile("api/"+str(checkForFile(fac.username.username, uploadType)), path+ "/" + filename)
      if uploadType == "vitae":
        collaborator = getCollaborators(fac.username)
        if collaborator is not None:
          for c in collaborator:
            print "collaborator is " + c.username.username
            if checkForFile(c.username.username, uploadType) != "":
              filename = checkForFile(c.username.username, uploadType).split("/").pop()
              shutil.copyfile("api/"+str(checkForFile(c.username.username, uploadType)), path+ "/" + filename)
  
  temp = uuid.uuid1()
    
  os.mkdir(yearDir+"/"+str(temp))
  shutil.make_archive(yearDir+"/"+ str(temp) + "/" + str(parameters.year), 'zip', yearDir +"/"+str(uniqueID))            
  
  return send_file("../" + yearDir +"/"+ str(temp) + "/" + str(parameters.year)+".zip", as_attachment=True)