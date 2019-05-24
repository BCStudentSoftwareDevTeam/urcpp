from ..everything import *
import json

def getCommitteeMembers():
  """Gets all of the committee members of the system
  
    Returns:
      LDAPFaculty Select Query: The committee members
  """
  return (LDAPFaculty.select()
                    .where(LDAPFaculty.isCommitteeMember == True))
                    
                    
def removeCommitteeMembers(commiteeList):
  """removes the committee members from a list
     
    Args:
      committeList (list): the list of desired committee members
  
    Returns:
      int: The number of rows changed
  """
      
  removeQuery = (LDAPFaculty.update(isCommitteeMember = False)
                        .where(LDAPFaculty.isCommitteeMember == True) # currentCommittee Members
                        .where(~(LDAPFaculty.fID << commiteeList))) # not in the list passed through
                        
  return removeQuery.execute()
  
  
def addCommitteeMembers(desiredCommitteeList):
  """Adds committee members from a list
    
    Args:
      desiredCommitteeList (list): the list of desired committee members
  
    Returns:
      int: the number of rows changed
  """
  
  makeCommitteeMembers = (LDAPFaculty.update(isCommitteeMember = True)
                                      .where(LDAPFaculty.fID << desiredCommitteeList))
                                      
  return makeCommitteeMembers.execute()
