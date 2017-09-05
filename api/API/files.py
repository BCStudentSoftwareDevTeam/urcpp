import shutil
from parameters import getCurrentParameters
from ..everything import *
#Flask mail imports
from flask_mail import Mail, Message




def removeFiles(username):
  """ This function removes the folder that belong to a user. 
      It should be used when the project is withdrawn
      
      Args:
        username (str): The username of the faculty whose folder should be deleted
  
  """
  currentParameter = getCurrentParameters()
  folder_path = os.path.join(base_path, cfg["filepaths"]["projectFiles"], str(currentParameter.year), username)
  shutil.rmtree(folder_path)
  

def send_email(user_email, app=None):
  '''this function sends email to the user email
  specify port, mail-server, username, password in settings.py
  '''
  mail=Mail(app)
  msg=Message("Hello",
    sender="from@example.com",
    recipients=[user_email] 
  )
  msg.body="this is a messsage body"
  mail.send(msg)
  
@app.route("/email")
def email():
  '''this route is for testing purposes'''
  my_email="heggens@berea.edu"
  send_email(my_email, app)
  return "Message is sent."
  

  