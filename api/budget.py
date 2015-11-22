from everything import *

def getBudget (username):
   facQ = (URCPPFaculty.select()
      .where (URCPPFaculty.username == username)
      )
   
   if facQ.exists():
      fac = facQ.get()
      return fac.pID.budgetID
   else:
      return None