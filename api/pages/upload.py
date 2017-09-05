from api.everything import *
import os, re, errno
from ..API.projects import getProject
from ..API.parameters import getCurrentParameters

def checkForFile(username, uploadType, year):
  #we need to know where we are at for file lookup issues
  allowedExtensions = cfg["filepaths"]["allowedFileExtensions"].keys();
  for ext in allowedExtensions:
    fileDirectory = 'static/files'
    prevFilepath = '{0}{1}/{2}/{3}-{4}.{5}'.format(cfg['filepaths']['projectFiles'],
                                    year,
                                    username, username,
                                    uploadType, ext)
    prevFilepathAbs = os.path.join(base_path, prevFilepath)
    if not (os.path.exists(prevFilepathAbs)):
      prevFilepath =''
    else:
        app.logger.error(prevFilepath)
        pathComponents = prevFilepath.split('/')
        prevFilepath = pathComponents[-1] 
        break
  return prevFilepath


# This looks like file upload, but it isn't.
# This renders a "generic" upload page, where the upload type
# is one of three types. The page configures itself based
# on the type of upload being requested.

@app.route("/upload/<uploadType>", methods = ["GET"])
@login_required
def generic_file_upload (uploadType):
  # we need the current cycle to upload only the current file
  applicationCycle = getCurrentParameters()
  if uploadType in cfg["filepaths"]["allowedFileNames"]:
    # All of our queries
    
    proj = getProject(g.user.username)

    prevFilepath = checkForFile(g.user.username, uploadType, applicationCycle.year)
    prev = prevFilepath
    #prevFilepath = prev.split("/").pop()
    return render_template (  "pages/upload.html",
                              proj = proj,
                              # we are passing both the username and user object
                              username = g.user.username,
                              cfg = cfg,
                              ldap = g.user,
                              uploadType = uploadType,
                              fullpath = prev,
                              prevFilepath = prevFilepath,
                            )
  else:
    return "File upload type not recognized."


def removeLeadingDot (line):
  line = re.sub('[.]', '', line)
  return line

@app.route('/upload/removefile/<uploadType>/<username>', methods=['POST'])
def remove_file(username, uploadType):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  else:
    rawpath = cfg["filepaths"]["directory"]
    cycle   = getCurrentParameters()
    rawpath = rawpath.replace("%%applicationCycle%%", str(cycle.year))
    path    = rawpath.replace("%%username%%", username)
    path    = os.path.join(base_path, path)
    previous_file = checkForFile(username, uploadType, cycle.year)

    if previous_file:
      app.logger.info("{0} removing {1}.".format(username, path))
      os.remove(os.path.join(path, previous_file))
      return "File Deleted"
  return "Error, File Not Deleted"
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
    cycle   = getCurrentParameters()
    rawpath = rawpath.replace("%%applicationCycle%%", str(cycle.year))
    path    = rawpath.replace("%%username%%", username)
    path    = os.path.join(base_path, path)
    app.logger.info("{0} saving {1} to {2}.".format(username, filename, path))
    try:
      os.makedirs(path)
    except OSError as exc: # Python >2.5
      if exc.errno == errno.EEXIST and os.path.isdir(path):
          pass
      else: raise
    
    # delete the previous file 
    # needed in case of extension change
    previous_file = checkForFile(username, whichfile, cycle.year)
    if previous_file:
      os.remove(os.path.join(path, previous_file))
    
    file.save(os.path.join(path, filename))

    return jsonify( { "response" : "OK" } )
  return jsonify( { "response" : "BAD" } )
