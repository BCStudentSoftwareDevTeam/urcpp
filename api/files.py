from everything import *
import os, re

def removeLeadingDot (line):
  line = re.sub('[.]', '', line)
  return line

@app.route('/urcpp/v1/file/upload/<whichfile>/<username>', methods=['POST'])
def upload_file(whichfile, username):
  
  app.logger.info("{0} attempting to upload file.".format(username))
  
  file = request.files['file']
  allowedExtensions = cfg["filepaths"]["allowedFileExtensions"].keys()
  
  if file and (whichfile in cfg["filepaths"]["allowedFileNames"]):
    basename, file_extension = os.path.splitext(file.filename)
    ext = removeLeadingDot(file_extension)
    
    app.logger.info("File extension: {0}".format(file_extension))
    
    if ext in allowedExtensions:
      filename = "{0}-vitae.{1}".format(username, ext)
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
      
    file.save(os.path.join(path, filename))
    
    return jsonify( { "response" : "OK" } )
  return jsonify( { "response" : "BAD" } )
  # return redirect(url_for('uploaded_file', filename=filename))