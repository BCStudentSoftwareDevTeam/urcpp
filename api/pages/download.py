from api.flask_imports import *

from ..everything import cfg
from api.models import *
import os
from ..API.makeExcel import makeBudgetExcel, makeLaborExcel
from flask import send_file, abort
from flask_login import login_required, current_user
from ..API.parameters import getCurrentParameters

from api.pages import pages

@pages.route("/document/<username>/<fileType>"
        ,methods = ['GET'])
# Trying out temporal stuff
def document(username,fileType):
    return redirect(url_for("documentDownload",
                            username=username,
                            fileType=fileType,
                            applicationYear=getCurrentParameters().year))

@pages.route("/document/<username>/<fileType>/<applicationYear>", methods = ['GET'])
@login_required
def documentDownload(username, fileType, applicationYear):
  if (not current_user.isCommitteeMember) and current_user.username != username:
    abort(403)

  relPath = '{0}{1}/{2}/{3}'.format(cfg["filepaths"]["downloadFiles"],
                            applicationYear, username, fileType)

  fullPath = os.path.join(base_path, relPath)


  return send_file (fullPath, as_attachment=True)


@pages.route("/<username>/download/<fileName>/", methods = ["GET"])
def generic_file_download (username, fileName):
  if username != authUser(request.environ):
    return { "response": cfg["response"]["badUsername"] }

  fileNameComponents = fileName.split('-')
  fileNameComponents.pop(0)
  applicationYear, folder = fileNameComponents
  ext = cfg["downloads"]["downloadFileExtension"]
  relPath = cfg["filepaths"]["downloadFiles"] + applicationYear + "/" + folder + "/" + fileName + ext

  fullPath = os.path.join(base_path, relPath)

  if folder == cfg["downloads"]["downloadFileTypes"]["allLabor"]:
    makeLaborExcel()
  elif folder == cfg["downloads"]["downloadFileTypes"]["allBudgets"]:
    makeBudgetExcel()

  return send_file (fullPath, as_attachment=True)
