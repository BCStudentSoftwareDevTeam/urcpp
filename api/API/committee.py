from ..everything import *
import json

def getCommitteeMembers():
  """Gets all of the committee members of the system
    Args: 
      None
      
    Returns:
      LDAPFaculty Select Query: gets all committee 
  """
  
  # selects all committee members from the database
  return (LDAPFaculty.select(LDAPFaculty.username)
                    .where(LDAPFaculty.isCommitteeMember == True)
                    )
                   
                    
def removeCommitteeMembers(commiteeList):
  """removes the committee members from a list
     
    Args:
      committeList (list): the list of desired committee members that will be removed
  
    Returns:
      int: The number of rows changed in the database
  """
  
  # selects faculty members from the database and sets isCommitteeMember to false which will remove names provided in the list from the database    
  makeCommitteeMembers = (LDAPFaculty.update(isCommitteeMember = False)
                                      .where(LDAPFaculty.fID << commiteeList))
                        
  # executes the above query
  return makeCommitteeMembers.execute()
  
  
def addCommitteeMembers(desiredCommitteeList):
  """Adds committee members from a list to the database
    
    Args:
      desiredCommitteeList (list): the list of desired committee members to be added
  
    Returns:
      int: the number of rows changed within the database
  """
  
  #select faculty members from the database  and sets isCommitteeMember to true which will add members from list to the database
  makeCommitteeMembers = (LDAPFaculty.update(isCommitteeMember = True)
                                      .where(LDAPFaculty.fID << desiredCommitteeList))
                                      
  # executes the above query
  return makeCommitteeMembers.execute()
