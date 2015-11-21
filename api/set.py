from everything import *
from projects import getProject

@app.route("/urcpp/v1/set/start/<username>", methods = ["POST"])
def set_start(username):
  if username != os.getenv("USER"):
    return { "response": cfg["response"]["badUsername"] }

  # Grab the .body() from the aja() POST
  data = request.get_json()

  # This is what our post from this page looks like
  # {duration: "8", program: "1", startDate: "May 1", title: "URCPP Software Also"}
  
  proj = getProject(username)
  if proj is None:
    proj = Project()
  
  proj.title = data["title"]
  proj.save()  
  
  response = { "response" : "OK" }
  return jsonify(response)
