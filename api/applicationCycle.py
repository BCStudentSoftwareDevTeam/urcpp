from everything import *
import datetime

def getCurrentCycle():
  now = datetime.datetime.now()
  cycle = (ApplicationCycle.select()
            .where(ApplicationCycle.year == now.year)
          )
  app.logger.info("Looking for budget with query:\n\n" + cycle + "\n\n")
  if cycle.exists():
    return cycle.get()
  else:
    return None
