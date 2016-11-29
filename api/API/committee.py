from ..everything import *
import json

def getCommitteeMembers():
  """Gets all of the committee members of the system"""
  return (LDAPFaculty.select()
                    .where(LDAPFaculty.isCommitteeMember == True))
                    
                    
def removeCommitteeMembers(commiteeList):
  """removes the committee members from a list
    :param committeList - the list of desired committee members"""
  removeQuery = (LDAPFaculty.update(isCommitteeMember = False)
                        .where(LDAPFaculty.isCommitteeMember == True) # currentCommittee Members
                        .where(~(LDAPFaculty.fID << commiteeList))) # not in the list passed through
                        
  return removeQuery.execute()
  
  
def addCommitteeMembers(desiredCommitteeList):
  """Adds committee members from a list
     :param desiredCommitteeList - the list of desired committee members"""
  
  makeCommitteeMembers = (LDAPFaculty.update(isCommitteeMember = True)
                                      .where(LDAPFaculty.fID << desiredCommitteeList))
                                      
  return makeCommitteeMembers.execute()
