from api.everything import *
from faculty import *


def getAllCollaborators():
  """ gets all of the collaborators from the collaborators table
  
      Returns:
        Collaborator Select Query: all of the collaborators
  """
  collabQ = (Collaborators.select())
  if collabQ.exists():
    return collabQ.execute()
  else:
    return None

def getCollaborators (username):
  """ gets all of the collaborators for a user
      
      Args:
        username (str): the user to whom the project belongs
      
      Returns:
        Collaborators Select Query: the collaborators aiding the project
  """
  collaborators = (Collaborators.select()
    .join (URCPPFaculty, on = (URCPPFaculty.pID == Collaborators.pID))
    .where (URCPPFaculty.username == username)
    .join(Projects, on =(Projects.pID == Collaborators.pID))
    .where (Projects.status != "Withdrawn")
    )

  if collaborators.exists():
    return collaborators
  else:
    return None

def getCollaboratorsByProjectId (pID):
  """ gets collaborator based on an project id 
      
      Args: 
        pID (int): the project that the collaborators are contributing to
      
      Returns:
        list, None: the list of collaborators or None 
  """
  collaborators = (Collaborators.select()
    .where (Collaborators.pID == pID)
    )

  if collaborators.exists():
    return collaborators
  else:
    return None


# used in AwardLetters
@app.route ("/urcpp/v1/collaborators/get/<username>", methods = ["POST"])
def collaborators_get (username):
  """ gets the collaborators of a user
      
      Args:
        username (str): the username of whom the project belongs
      
      Returns:
        JSON: a dictionary version of the models or noResults
  """

  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }

  collabs = getCollaborators(username)
  
  if collabs:
    response = {  "response" : "OK" }
    response["collaborators"] = map(m2d, collabs)
    return jsonify(response)
  else:
    response = { "response": cfg["response"]["noResults"],
                 "details": "No collaborators found for username {0}.".format(username)
                 }
    return jsonify(response)  
    
def get_collaborator(project_id, username):
  """ gets a collaborator 
      
      Args:
        username (str): the username of the collaborators_get
        project_id (int): the id of the project 
        
      Returns:
        Collaborators: the collaborator"""
  collaborator = (Collaborators.select()
                        .where(Collaborators.username==username)
                        .where(Collaborators.pID==project_id))
                        
  if collaborator.exists():
    return collaborator.get() # FIXME: expects only one collaborator, will break with 2+
  else:
    return None
  
def delete_all_collaborators(project_id):
  """ deletes all of the currect collaborators 
      
      Args:
        project_id (int): the id of the project that the collaborators belong to
        
      Returns:
        int: the number of rows affected
  """
  return(Collaborators.delete()
                    .where(Collaborators.pID == project_id)).execute()
                    
        
def delete_non_collaborators(project_id, *collaborators):
  """ deletes the current collaborators that are not in the list provided
      
      Args:
        project_id (int): the id of the project that the collaborators belong to
        collaborator_bnumbers (splat): the collaborators that are current collaborators
        
      Returns:
        int: the number of rows affected
  """
  current_collaborators = get_faculty_by_bnumbers(collaborators)
  
  return (Collaborators.delete()
                      .where(Collaborators.pID == project_id)
                      .where(
                              ~(Collaborators.username << current_collaborators)
                              )
          ).execute()
        
        
def add_collaborators(project_id, *collaborator_usernames):
  """ add the collaborators from collaborator bnumbers
  
      Args:
        project_id (int): the id of the project that the collabors belong to
        collaborator_bnumbers (splat): the collaborators that will be the current collaborators
  """
  
  faculty = getLDAPFaculty(collaborator_usernames)
  
  for professor in faculty:
    if get_collaborator(project_id, professor.username) is None:
      Collaborators(pID = project_id, username = professor.username).save()
