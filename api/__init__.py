from everything import *

@app.route('/s/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

# Import all endpoints that retrieve data
import api.get

# Import all endpoints that insert/update data
import api.set

# Import all endpoints that delete data
import api.delete