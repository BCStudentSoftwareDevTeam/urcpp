# TODO: we need to either prune this page or add functions for different parameter years
from ..everything import *

def getCurrentParameters():
   
  paramsQ = (Parameters.select().where(Parameters.isCurrentParameter))
   
  app.logger.info("Looking for parameters with query:\n\n" + paramsQ + "\n\n")
   
  if paramsQ.exists():
    return paramsQ.get()
  else:
    return None
    
def getParameters(parameters_id):
  parameters = (Parameters.select()
                    .where(Parameters.pID == parameters_id))
  if parameters.exists():
    return parameters.get()
  else:
    return None

def getParametersByYear(year):
  parameters = (Parameters.select()
                    .where(Parameters.year == year))
  if parameters.exists():
    return parameters.get()
  else:
    return None
  
@app.route("/set/current_parameters/<int:parameters_id>", methods=["GET"])
@login_required
def set_current_parameters(parameters_id):
  if not current_user.isChair:
    abort(403)
  current_parameters = getCurrentParameters()
  current_parameters.isCurrentParameter = False
  current_parameters.save()
  
  new_current_parameters = getParameters(parameters_id)
  new_current_parameters.isCurrentParameter = True
  new_current_parameters.save()
  
  return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
  
  