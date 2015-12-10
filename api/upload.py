from everything import *
import os, re, errno
from pages import *
from faculty import getFaculty, getLDAPFaculty
from projects import getProject
from programs import getAllPrograms
from budget import getBudget
from collaborators import getCollaborators

def checkForFile(username, uploadType):
  allowedExtensions = cfg["filepaths"]["allowedFileExtensions"].keys();
  # print allowedExtensions
  for ext in allowedExtensions:
    prevFilepath = ("api/static/files/" + str(cfg["urcpp"]["applicationCycle"]) + "/" + username + "/" + username + "-" + uploadType + "." + ext)
    if not (os.path.exists(prevFilepath)):
      prevFilepath = ""
    else:
      break
  return prevFilepath.split("/").pop()


# This looks like file upload, but it isn't.
# This renders a "generic" upload page, where the upload type
# is one of three types. The page configures itself based 
# on the type of upload being requested.
@app.route("/<username>/upload/<uploadType>", methods = ["GET"])
def generic_file_upload (username, uploadType):
  if uploadType in cfg["filepaths"]["allowedFileNames"]:
    # All of our queries
    faculty = getFaculty(username)
    ldapFaculty = getLDAPFaculty(username)
    proj = getProject(username)
    programs = getAllPrograms()
    collaborators = getCollaborators(username)
    budget = getBudget(username)

    prevFilepath = checkForFile(username, uploadType)
    return render_template (  "upload.html",
                              proj = proj,
                              username = username,
                              cfg = cfg,
                              fac = faculty,
                              ldap = ldapFaculty,
                              uploadType = uploadType,
                              prevFilepath = prevFilepath,
			      lastPage = uploadType
                            )
  else:
    return "File upload type not recognized."
    

def removeLeadingDot (line):
  line = re.sub('[.]', '', line)
  return line


# Captures file upload from the dropzone and saves to server
@app.route('/v1/upload/<whichfile>/<username>', methods=['POST'])
def upload_file(whichfile, username):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
    
  app.logger.info("{0} attempting to upload file.".format(username))
  # NOTE: This is very fragile. Seems to work with docx, failed on two pdf's. 
  # Size isn't cause. 
  file = request.files['file']
  allowedExtensions = cfg["filepaths"]["allowedFileExtensions"].keys()
  
  app.logger.info("File name: {0}".format(file.filename))
  
  if file and (whichfile in cfg["filepaths"]["allowedFileNames"]):
    basename, file_extension = os.path.splitext(file.filename)
    ext = removeLeadingDot(file_extension)
    
    app.logger.info("File extension: {0}".format(file_extension))
    
    if ext in allowedExtensions:
      filename = "{0}-{1}.{2}".format(username, whichfile, ext)
    else:
      app.logger.info("Not an allowed extention!")
      return jsonify( { "response" : "BADEXTENSION" } )
    
    app.logger.info("Filename appears to be: " + filename)
    
    # Need to replace the cycle and username
    rawpath = cfg["filepaths"]["directory"]
    cycle   = cfg["urcpp"]["applicationCycle"]
    rawpath = rawpath.replace("%%applicationCycle%%", str(cycle))
    path    = rawpath.replace("%%username%%", username)
    
    app.logger.info("{0} saving {1} to {2}.".format(username, filename, path))
    
    try:
      os.makedirs("api/static/files/" + str(cfg["urcpp"]["applicationCycle"]) + "/" + username + "/")
    except OSError as exc: # Python >2.5
      if exc.errno == errno.EEXIST and os.path.isdir(path):
          pass
      else: raise
    
    file.save(os.path.join(path, filename))
    
    return jsonify( { "response" : "OK" } )
  return jsonify( { "response" : "BAD" } )