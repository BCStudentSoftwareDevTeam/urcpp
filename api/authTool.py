from everything import *
from projects import getProject

class AuthorizedUser:

  '''
  @param username - name of the user accessing the information
  @param prefix   - prefix of the subject being accessed
  '''

  def __init__(self):
    self.username = authUser(request.environ)
      
  def isAuthorized(self, username):
    return self.username == username
  
  def canUpdateForm(self, username):
    proj = getProject(username)
    print proj.status
    if proj.status == cfg["projectStatus"]["incomplete"]:
      return True
    return False