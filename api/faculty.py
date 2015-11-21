from everything import *
import json

def previousYearsFunded (username):
  urcppFacultyQ = (URCPPFaculty.select()
    .where (URCPPFaculty.username == username)
    .where (URCPPFaculty.corresponding == True)
  )
  
  if urcppFacultyQ.exists():
    return urcppFacultyQ.get()
  else:
    return None

@app.route ("/urcpp/v1/faculty/previousYearsFunded/<username>", methods = ["POST"])
def faculty_previousYearsFunded (username):
  if username != os.getenv("USER"):
    return { "response": cfg["response"]["badUsername"] }

  urcppFaculty = previousYearsFunded(username)
  
  if urcppFaculty:
    response = {  "response" : "OK" }
    fundedDict = json.loads(urcppFaculty.yearsFunded)
    response["urcppFaculty"] = fundedDict
    
    return jsonify(response)
  else:
    response = { "response": cfg["response"]["noResults"],
                 "details": "No results found for project."
                 }
    return jsonify(response) 