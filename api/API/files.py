import shutil
from parameters import getCurrentParameters
from ..everything import *

#Flask mail imports
from flask_mail import Mail




def removeFiles(username):
  """ This function removes the folder that belong to a user. 
      It should be used when the project is withdrawn
      
      Args:
        username (str): The username of the faculty whose folder should be deleted
  
  """
  currentParameter = getCurrentParameters()
  folder_path = os.path.join(base_path, cfg["filepaths"]["projectFiles"], str(currentParameter.year), username)
  shutil.rmtree(folder_path)
  

def send_email(username_email, app=None):
  '''
  Parameters: app - Flask instance
  '''
  mail = Mail(app)  #mail using configuration values of the application
  msg = Message("Hello",
                  sender="from@example.com",
                  recipients=[username_email])  #create a message instance
  mail.send(msg) #send the message
  

  