from everything import *
import os
from makeExcel import makeBudgetExcel, makeLaborExcel
from flask import send_file

@app.route("/<username>/document/<filename>",
            defaults={'applicationYear' : cfg['urcpp']['applicationCycle'] }
        , methods = ['GET'])
@app.route("/<username>/document/<filename>/<applicationYear>", methods = ['GET'])
def documentDownload(username, filename, applicationYear):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  fileNameComponents = filename.split('-')
  folder, fileType = fileNameComponents
  relPath = '{0}{1}/{2}/{3}'.format(cfg["filepaths"]["downloadFiles"],
                            applicationYear, folder, filename)
  
  here = os.path.dirname(__file__)
  fullPath = os.path.join(here, relPath)
  
  
  return send_file (fullPath, as_attachment=True)
   

@app.route("/<username>/download/<fileName>/", methods = ["GET"])
def generic_file_download (username, fileName):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  fileNameComponents = fileName.split('-')
  fileNameComponents.pop(0)
  applicationYear, folder = fileNameComponents
  ext = cfg["downloads"]["downloadFileExtension"]
  relPath = cfg["filepaths"]["downloadFiles"] + applicationYear + "/" + folder + "/" + fileName + ext
  
  here = os.path.dirname(__file__)
  fullPath = os.path.join(here, relPath)
  
  if folder == cfg["downloads"]["downloadFileTypes"]["allLabor"]:
    makeLaborExcel()
  elif folder == cfg["downloads"]["downloadFileTypes"]["allBudgets"]:
    makeBudgetExcel()
  
  return send_file (fullPath, as_attachment=True)
  
