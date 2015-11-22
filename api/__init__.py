from everything import *

@app.route('/s/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

# Routes used everywhere, like static and templates
import api.globalroutes

# Our getters
import api.projects
import api.faculty
import api.programs
import api.collaborators

# Our setters, so pages can submit data
import api.set
