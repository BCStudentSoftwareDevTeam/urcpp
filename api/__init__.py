from everything import *

@app.route('/s/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

# Import the POST endpoints, which are queries
import api.create

# Import the PUT endpoints, where are where data comes in
import api.update

# Import the GET endpoints
import api.read

# Import the delete
import api.delete
