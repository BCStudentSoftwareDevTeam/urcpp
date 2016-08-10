from everything import *
import os
from makeExcel import makeBudgetExcel, makeLaborExcel
from flask import send_file

@app.route("/<username>/download/<fileName>/", methods = ["GET"])
def generic_file_download (username, fileName):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }
  
  fileNameComponents = fileName.split('-')
  fileNameComponents.pop(0)
  applicationYear, folder = fileNameComponents
  ext = cfg["downloads"]["downloadFileExtension"]
  
  path = cfg["filepaths"]["downloadFiles"] + applicationYear + "/" + folder + "/" + fileName + ext
  
  if folder == cfg["downloads"]["downloadFileTypes"]["allLabor"]:
    makeLaborExcel()
  elif folder == cfg["downloads"]["downloadFileTypes"]["allBudgets"]:
    makeBudgetExcel()
  
  return send_file (path, as_attachment=True)
  