import shutil
from parameters import getCurrentParameters
from ..everything import *

def removeFiles(username):
  """ This function removes the folder that belong to a user. 
      It should be used when the project is withdrawn
      
      Args:
        username (str): The username of the faculty whose folder should be deleted
  
  """
  currentParameter = getCurrentParameters()
  folder_path = os.path.join(base_path, cfg["filepaths"]["projectFiles"], str(currentParameter.year), username)
  shutil.rmtree(folder_path)
  