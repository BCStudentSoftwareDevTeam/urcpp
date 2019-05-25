import shutil
from parameters import getCurrentParameters
from ..everything import *
#Flask mail imports
from flask_mail import Message





def removeFiles(username):
  """ This function removes the folder that belong to a user. 
      It should be used when the project is withdrawn
      
      Args:
        username (str): The username of the faculty whose folder should be deleted
  
  """
  currentParameter = getCurrentParameters()
  folder_path = os.path.join(base_path, cfg["filepaths"]["projectFiles"], str(currentParameter.year), username)
  shutil.rmtree(folder_path)

  



def create_message(subject, recipients, body):
  '''
  Parameters: 
    username_email(s) - Emails of the recipients
    body - The body of the email
  '''
  msg = Message(subject,
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[recipients])  #create a message instance
  msg.html = body
  return msg
