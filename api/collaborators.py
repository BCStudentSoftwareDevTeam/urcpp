from everything import *

def getCollaborators (username):
  collabQ = (Collaborators.select()
    .join (URCPPFaculty, on = (URCPPFaculty.pID == Collaborators.pID))
    .where (URCPPFaculty.username == username)
    )

  if collabQ.exists():
    collaborators = []
    collabs = collabQ.select()
    for collab in collabs:
      collaborators.append( collab.username )
    return collaborators
  else:
    return None

@app.route ("/urcpp/v1/collaborators/get/<username>", methods = ["POST"])
def collaborators_get (username):
  if username != os.getenv("USER"):
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