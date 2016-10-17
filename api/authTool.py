from everything import authUser, cfg
from flask import request
from projects import getProject
from faculty import getLDAPFaculty

class AuthorizedUser:

  '''
  @param username - name of the user accessing the information
  @param prefix   - prefix of the subject being accessed
  '''

  def __init__(self):
    self.user     = getLDAPFaculty(authUser(request.environ))
    
  def get_username(self):
    '''returns the username of the person logged in'''
    return self.user.username
    
  def isAuthorized(self, username):
    return username == self.user.username
    
      
  def is_chair(self):
    return self.user.is_chair
    
  def is_committee_member(self):
    return self.user.is_committee_member
  
  #TODO move this function outside of authorized user.
  def canUpdateForm(self, username):
    proj = getProject(username)
    print proj.status
    if proj.status == cfg["projectStatus"]["incomplete"]:
      return True
    return 
  
  def __repr__(self):
    return "{0}, {1}".format(self.user.firstname, self.user.lastname)