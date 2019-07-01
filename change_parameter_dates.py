from api.models import *
import datetime

params  = Parameters.select()

for p in params:
    
    print(p.year)
    change = datetime.datetime.now()
    change = change.replace(year=p.year, month=1, day=1)
    p.ProposalOpenDate = change
    change = change.replace(year=p.year, month=2, day=1)
    p.ProposalClosedDate = change
    change = change.replace(year=p.year, month=3, day=1)
    p.ProposalAcceptanceDate = change
    change = change.replace(year=p.year, month=4, day=1)
    p.AbstractnarrativesAcceptanceDate = change
    change = change.replace(year=p.year, month=5, day=1)
    p.AllSubmissionsClosedDate = change

    p.IRBchair_id = 'broomfields'
    p.currentchair_id = 'broomfields'
    p.staffsupport_id = 'broomfields'



    p.save() 
