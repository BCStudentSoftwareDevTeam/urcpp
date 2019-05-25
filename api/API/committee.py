from ..everything import *
import json

def getCommitteeMembers():
  """Gets all of the committee members of the system
  
    Returns:
      LDAPFaculty Select Query: The committee members
  """
  return (LDAPFaculty.select(LDAPFaculty.username)
                    .where(LDAPFaculty.isCommitteeMember == True)
                    )
                   
                    
def removeCommitteeMembers(commiteeList):
  """removes the committee members from a list
     
    Args:
      committeList (list): the list of desired committee members
  
    Returns:
      int: The number of rows changed
  """
      
  makeCommitteeMembers = (LDAPFaculty.update(isCommitteeMember = False)
                                      .where(LDAPFaculty.fID << commiteeList))
                        
  return makeCommitteeMembers.execute()
  
  
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
