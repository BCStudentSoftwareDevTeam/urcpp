from everything import *

def getBudget (username):
   facQ = (URCPPFaculty.select()
      .where (URCPPFaculty.username == username)
      )
   
   if facQ.exists():
      fac = facQ.get()
      if fac.pID:
        if fac.piD.budgetID
          return fac.pID.budgetID
      return None
   else:
      return None