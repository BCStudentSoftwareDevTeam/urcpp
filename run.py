from web import app
import os
from web.config import load_config

# The path is relative to the top of the project.
cfg = load_config('web/config.yaml')
skt = load_config('web/secret_config.yaml')

# Run with
# $ IP=0.0.0.0 PORT=8080 python run.py
# or similar
if os.getenv('IP'):
  IP = os.getenv('IP')
else:
  IP = '0.0.0.0'

if os.getenv('PORT'):
  PORT = int(os.getenv('PORT'))
else:
  PORT = 9090

print ("Running at http://{0}:{1}/".format(IP, PORT))

app.secret_key = skt['secret_key']
app.tag = cfg['tag']

app.run(host = IP, port = PORT, debug = True)

