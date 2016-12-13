from api.everything import *
from faculty import get_faculty_by_bnumbers
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
  """ gets all of the collaborator for a user
      
      Args:
        username (str): the user to whom the project belongs
      
      Returns:
        Collaborators Select Query: the collaborators aiding the project
  """
  collabQ = (Collaborators.select()
    .join (URCPPFaculty, on = (URCPPFaculty.pID == Collaborators.pID))
    .where (URCPPFaculty.username == username)
    )

  if collabQ.exists():
    collaborators = []
    collabs = collabQ.select()
    for collab in collabs:
      collaborators.append( collab )
    return collaborators
  else:
    return None

def getCollaboratorsById (pID):
  """ gets collaborator based on an project id 
      
      Args: 
        pID (int): the project that the collaborators are contributing to
      
      Returns:
        list, None: the list of collaborators or None 
  """
  collabQ = (Collaborators.select()
    .where (Collaborators.pID == pID)
    )

  if collabQ.exists():
    collaborators = []
    collabs = collabQ.select()
    for collab in collabs:
      collaborators.append( collab )
    return collaborators
  else:
    return None

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
    
def delete_non_collaborators(collaborator_bnumbers, project_id):
  """ deletes the current collaborators that are not in the list provided
      
      Args:
        collaborators (list): the list of collaborators that are current_user
        project_id (int): the id of the project that the collaborators belong to
        
      Returns:
        int: the number of rows affected
  """
  current_collaborators = get_faculty_by_bnumbers(collaborator_bnumbers)
  
  return (Collaborators.delete()
                       .where(Collaborators.pID == project_id)
                       .where(
                              ~(Collaborators.username << current_collaborators)
                              )
          ).execute()