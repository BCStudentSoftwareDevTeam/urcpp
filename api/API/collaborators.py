from api.everything import *

def getAllCollaborators():
  collabQ = (Collaborators.select())
  if collabQ.exists():
    return collabQ.execute()
  else:
    return None

def getCollaborators (username):
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