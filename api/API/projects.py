from ..everything import *
import os
from parameters import getCurrentParameters


def getProjectByID(projectID):
  """ This function gets all the project information assocaiting with the projectID
  
      Args:
        projectID: the unique project ID
  
      Returns: 
        The project information by using a specific project ID
  """
  projQ = (Projects.select() # progQ is set to all the project information where pID and projectID are the same
                  .where(Projects.pID == projectID)
          )
  if projQ.exists():
    return projQ.get() # returns all the project information: pID, title, budgetID, duration, startDate, endDate, year_id, hasCommunityPartner, isServiceToCommunity, humanSubjects, numberStudents, status, and createdDate
  else:
    return None # else return None


def getProjectByYear(username, year):
    """ This function gets all the project information associating with the username and specific year
  
      Args:
        username: the person who is currently accessing the app
        year: a specific year
  
      Returns:
        proj: The project information by using a specific year and username
    """
  # gets the project belonging to this user during a specific year
  projQ = (Projects.select()
    .join (URCPPFaculty, on = (URCPPFaculty.pID == Projects.pID))
    .where (URCPPFaculty.username == username)
    .where (Projects.year == year)
    .where (Projects.status != cfg['projectStatus']['Withdrawn'])
  )
  
  if projQ.exists():
    proj = projQ.get()
    return proj # if projQ exists, return all the project info: pID, title, budgetID, duration, startDate, endDate, year_id, hasCommunityPartner, isServiceToCommunity, humanSubjects, numberStudents, status, and createdDate
  else:
    return None # else return None
    
    
def getProject (username):
  """ This function gets all the project information associating with the username and current year
  
      Args:
        username: the person who is currently accessing the app
  
      Returns:
        The project information for the username and current year
  """
  #get project for this user in the current cycle
  currentCycle = getCurrentParameters() # see parameters.py, checks to see what is the current year by finding the isCurrentParameters that has a 1
  if currentCycle is not None: # if currentCycle exists
	year = currentCycle.year # year is equal to the current year
  else:
	year = None # else, year is not a thing. Time is irrelevant
  return getProjectByYear(username, year) # returns all the project info: pID, title, budgetID, duration, startDate, endDate, year_id, hasCommunityPartner, isServiceToCommunity, humanSubjects, numberStudents, status, and createdDate
  
  
def getAllCurrentProjectsByYear(year):
  """ This function gets all of the projects in the current year
  
      Args:
        year: a specific year
  
      Returns:
        The project information for a specific year
  """
  allProjQ = (Projects.select()).where(Projects.year == year) # allProjQ is equal to all the projects in a current year
  
  if allProjQ.exists():
    return allProjQ # returns all projects info for the year: pID, title, budgetID, duration, startDate, endDate, year_id, hasCommunityPartner, isServiceToCommunity, humanSubjects, numberStudents, status, and createdDate
  else:
    return None # else returns None


def getAllCurrentProjects():
  """ This function gets all projects from the current year
  
      Args:
        None
  
      Returns:
        The project information for the current year
  """
  currentCycle = getCurrentParameters() # see parameters.py, checks to see what is the current year by finding the isCurrentParameters that has a 1
  if currentCycle is not None: 
	year = currentCycle.year # if currentCycle exists, set year equal to the current year
  
  return getAllCurrentProjectsByYear(year) # use previous function to return all project info for the current year: pID, title, budgetID, duration, startDate, endDate, year_id, hasCommunityPartner, isServiceToCommunity, humanSubjects, numberStudents, status, and createdDate


@app.route("/urcpp/v1/history/<username>", methods = ["GET"]) # reroutes to /urcpp/v1/history/<username - History doesn't exist anymore??????
def getProjectsByUsername(username):
  """ This function gets all of the projects associated with the username
  
      Args:
        username: the person who is currently accessing the app
  
      Returns: 
        hisoryDict: a dictionary with two keys, primaryFaculty and collaborated
        
  """
  #TODO: factor the project lists out to their own functions
  projects = (Projects.select()
              .join(URCPPFaculty, on = (URCPPFaculty.pID == Projects.pID)) # organizes each project with its faculty member
              .where(URCPPFaculty.username == username) # pulls only specific faculty member by username
              .order_by(-Projects.year)) # orders projects by descending year AKA present - 1998
  
  # if project exists, create an empty list and add to it
  if projects.exists():
    project_list = [] 
    for project in projects:
      project_list.append(m2d(project)) # m2d: model_2_dic, see everything.py, appears to change database to dictionary
  else:
    project_list = [] # else, create empty list
  
  # creates a dictionary called historyDict with a key of primaryFaculty and value of project_list
  historyDict = {} 
  historyDict['primaryFaculty'] = project_list 
  
  collaborated_projects = (Projects.select()
                           .join(Collaborators, on = (Collaborators.pID == Projects.pID)) # organizes each project with its collaborators
                           .where(Collaborators.username == username) # pulls only specific collaborators by username
                           )
  
  # if collaborated_projects exists, create an empty list and add to it
  if collaborated_projects.exists():
    collaborated_projects_list = []
    for collaborated_project in collaborated_projects:
      collaborated_projects_list.append(m2d(collaborated_project)) # appends projects associated with collaborator to the list, m2d: model_2_dic, see everything.py, appears to change database to dictionary
  else:
    collaborated_projects_list = [] # else, create empty list
  
  # dictionary created above now has another key of collaborated with value of collaborated_projects_list
  historyDict['collaborated'] = collaborated_projects_list
  
  return jsonify(historyDict) # returns dictionary historyDict

    
@app.route("/urcpp/v1/projects/get/<username>", methods = ["POST"]) # reroutes to /urcpp/v1/projects/get/<username>"
def projects_get (username):
  """ This function uses the username to check to see if a project can be found in the database  
  
      Args:
        username: username of the user currently logged in  
  
      Returns:
        A json response depending on the if the project can be found
  """
  # if the username is not authorized, return badUsername
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  # look up the project for this user, see getProject function above
  proj = getProject(username)

  # if project can be found, give success response
  if proj:
    response = {  "response" : "OK" }
    response["project"] = m2d(proj)
    return jsonify(response)
    
  # else it will give an error that there are no results for the project title  
  else:
    response = { "response": cfg["response"]["noResults"], 
                 "details": "No results found for project title."
                 }
    return jsonify(response) # return appropriate response based on if statement defined above


### Get Duration ###
@app.route("/urcpp/v1/projects/getPossibleDurations", methods = ["POST"]) #/reroutes to /urcpp/v1/projects/getPossibleDurations
def projects_getPossibleDurations ():
  """ This function gets the durations of the project
  
      Args:
        None
  
      Returns:
        A response based on if user is authorized or how many weeks the project went on
  """
  # if the user is not authorized, they will get a badUsername response
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  # if the user is authorized, this will return the duration of the project in weeks
  response = { "response" : "OK" }
  response["durations"] = cfg["urcpp"]["possibleDurations"]
  return jsonify(response)


### Get Narrative ###  
@app.route("/urcpp/v1/projects/getNarrative/<username>/<path>", methods = ["POST"]) # reroutes to /urcpp/v1/projects/getNarrative/<username>/<path>
def projects_getNarrative (username, path):
  """ Creates directories based on the username and the path where narrative is located
  
      Args:
        username: username of the user who is currently logged in
        path: path based on current user's narrative location
  
      Returns:
         A response based on if user is authorized or creates a directory path for the user based on the current year
  """
  # if the user is not authorized, they will get a badUsername response
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  applicationCycle = getCurrentParameters() # see parameters.py, checks to see what is the current year by finding the isCurrentParameters that has a 1
  
  # creates new path to a new directory for the user using the config.yaml, creates folders using the username and the current cycle year
  dirPath = cfg["filepaths"]["directory"]    
  dirPath = dirPath.replace("%%username%%", username)
  dirPath = dirPath.replace("%%applicationCycle%%", applicationCycle.year)

  knownFiles = os.listdir(dirPath) # returns a list containing the names of the entries in the directory given by dirPath

  # checks to see if the path exists; if so, it will give a success response, if not, it will give a noResults response
  for filenames in knownFiles: # 
    if path in filenames:
      response = {"response": "OK",
      "uploadType": filenames}
      #print "Path exists"
      return jsonify(response)
  response = { "response": cfg["response"]["noResults"],
            "details": "No results found for project file." }
  return jsonify(response) 
