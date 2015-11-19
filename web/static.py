# Our standard import soup
from everything import *

@app.route('/s/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

