from everything import *
from datetime import datetime

def getCurrentCycle():
  now = datetime.now()
  cycle = (Parameters.select()
            .where(Parameters.appOpenDate <= now.strftime('%Y-%m-%d') <= Parameters.appCloseDate.year)
          )
  app.logger.info("Looking for current year with query:\n\n" + cycle + "\n\n")
  if cycle.exists():
    return cycle.get()
  else:
    return None
