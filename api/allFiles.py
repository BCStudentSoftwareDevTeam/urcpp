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

import os, pprint, zipfile, uuid
import shutil

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
  for fac in faculty:
    prevFilepath[fac.username.username] = {}
    for uploadType in ["narrative", "vitae", "irb"]: 
      if checkForFile(fac.username.username, uploadType) != "":
        prevFilepath[fac.username.username][uploadType]= checkForFile(fac.username.username, uploadType)

  # Does the zipping
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
                          
@app.route("/<username>/committee/allFiles", methods = ["POST"])
def allFiles_POST (username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
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


  uniqueID = uuid.uuid1() 
  
  try:
    os.stat(cfg["filepaths"]["projectFiles"]+str(parameters.year))
    print("it exits"+ os.getcwd())
  except:
    print ("making dir...")
    os.mkdir(cfg["filepaths"]["projectFiles"]+str(parameters.year))
    ##############
    # http://stackoverflow.com/questions/273192/in-python-check-if-a-directory-exists-and-create-it-if-necessary
    ##############
  os.mkdir(cfg["filepaths"]["projectFiles"]+str(parameters.year)+"/"+str(uniqueID))
  
  facultyPending = getFacultyWithPendingProjects() 

  for fac in facultyPending:
    path = cfg["filepaths"]["projectFiles"]+str(parameters.year)+"/"+str(uniqueID)+"/project"+str(fac.pID.pID)
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
    
  print "###############################" + 'attachment; filename="'+ cfg["filepaths"]["projectFiles"] + str(parameters.year)+"/"+ str(temp) + "/" + str(parameters.year)+".zip\""
  os.mkdir(cfg["filepaths"]["projectFiles"]+str(parameters.year)+"/"+str(temp))
  shutil.make_archive(cfg["filepaths"]["projectFiles"] + str(parameters.year)+"/"+ str(temp) + "/" + str(parameters.year), 'zip', cfg["filepaths"]["projectFiles"] + "/" + str(parameters.year)+"/"+str(uniqueID))            
  
  # response = make_response()
  # response.headers['Cache-Control'] = 'no-cache'
  # response.headers['Content-Type'] = 'application/zip'
  # response.headers['Content-Disposition'] = 'attachment; filename="'+ cfg["filepaths"]["projectFiles"] + str(parameters.year)+"/"+ str(temp) + "/" + str(parameters.year)+".zip\""
  # return response
  
  return send_file("../" + cfg["filepaths"]["projectFiles"] + str(parameters.year)+"/"+ str(temp) + "/" + str(parameters.year)+".zip", as_attachment=True)

  # return render_template (  "allFiles.html",
  #                   proj = proj,
  #                   username = username,
  #                   cfg = cfg,
  #                   fac = faculty,
  #                   progs = programs,
  #                   budg = budget,
  #                   files = prevFilepath,
  #                   params = parameters
  #                 )