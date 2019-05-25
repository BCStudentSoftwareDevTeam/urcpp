activate_this= '/var/www/html/urcpp-flask/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/html/urcpp-flask/")
from api import app as application

