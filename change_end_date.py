from api.models import *
import datetime

projects  = Projects.select()

for project in projects:
    

    change = datetime.timedelta(days=7*project.duration)

    endDate = project.startDate + change
    
    project.endDate = endDate
    
    project.save()