import sys
import os

activate_this= '/home/heggens/urcpp-flask/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

print ("PATH: " + os.getcwd())

sys.path.insert(0, "/home/heggens/urcpp-flask")
os.chdir("/home/heggens/urcpp-flask/api")

print ("PATH: " + os.getcwd())

sys.stderr = sys.stdout

from api import app as application

