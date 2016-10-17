# TODO: we need to either prune this page or add functions for different parameter years
from everything import *

def getParameters():
   
   paramsQ = (Parameters.select())
   
   app.logger.info("Looking for parameters with query:\n\n" + paramsQ + "\n\n")
   
   if paramsQ.exists():
      return paramsQ.get()
   else:
      return None
