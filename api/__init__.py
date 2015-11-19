from everything import *
from api.models import theDB

# We have to set up and break down the DB on every request.
@app.before_request
def before_request():
  g.db = theDB
  g.db.connect()

@app.after_request
def after_request(response):
  g.db.close()
  return response

@app.route('/s/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)


# Import the POST endpoints, which are queries
import api.post

# Import the PUT endpoints, where are where data comes in
import api.put
