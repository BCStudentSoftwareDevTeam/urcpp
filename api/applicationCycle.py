from everything import *
from datetime import datetime

def getCurrentCycle():
  now = datetime.now()
  cycle = (ApplicationCycle.select()
            .where(ApplicationCycle.startDate <= now.strftime('%Y-%m-%d') <= ApplicationCycle.endDate.year)
          )
  app.logger.info("Looking for current year with query:\n\n" + cycle + "\n\n")
  if cycle.exists():
    return cycle.get()
  else:
    return None
