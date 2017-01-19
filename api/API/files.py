import shutil
from parameters import getCurrentParameters
from ..everything import *

def removeFiles(username):
  currentParameter = getCurrentParameters()
  print base_path
  folder_path = os.path.join(base_path, cfg["filepaths"]["projectFiles"], str(currentParameter.year), username)
  shutil.rmtree(folder_path)
  