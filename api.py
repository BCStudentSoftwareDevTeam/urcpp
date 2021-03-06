#!/usr/bin/env python
import os
from api import app
from api.config import load_config


# The path is relative to the top of the project.
cfg = load_config('api/config.yaml')
#skt = load_config('api/secret_config.yaml')

# Run with
# $ IP=0.0.0.0 PORT=8080 python run.py
# or similar
if os.getenv('IP'):
  IP = os.getenv('IP')
else:
  IP = '0.0.0.0'

if os.getenv('PORT'):
  PORT = int(os.getenv('PORT'))
  PORT = 8080
else:
  PORT = 8080

print ("Running at http://{0}:{1}/".format(IP, PORT))

#app.secret_key = skt['secret_key']
app.tag = cfg['tag']

if __name__ == "__main__":
  app.run(host = IP, port = PORT,  threaded = True)
