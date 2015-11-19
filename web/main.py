# Our standard import soup
from everything import *

# Import our route helpers
from pages import *
from store import *

# We have to set up and break down the DB on every request.
@app.before_request
def before_request():
  g.db = theDB
  g.db.connect()

@app.after_request
def after_request(response):
  g.db.close()
  return response

######################################################
# ROUTES
######################################################
# init    : /
# static  : /s/{{path}}
# router  : /{{tag}}/{{username}}/{{next}}

@app.route("/")
def init ():
  
  if (not session.has_key('username') or (session['username'] != os.getenv('USERNAME'))):    
    session['username'] = os.getenv('USERNAME')
  # Redirect everyone
  return redirect('/{0}/start'.format(cfg['tag']))

