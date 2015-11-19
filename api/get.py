from everything import *

# https://github.com/micha/resty
# Also, Postman in Chrome
# Also, http://blog.luisrei.com/articles/flaskrest.html
# Also, https://github.com/jpillora/jquery.rest
# For testing: http://unirest.io/python.html
# Also, the unittest library.
# Also for REST: http://restkit.readthedocs.org/en/latest/

@app.route ("/urcpp/v1/get/facultydetails/<username>", methods = ["POST"])
def getFacultyDetails (username):
  # FIXME: The funny library pushes things through as... form data?
  # force is for ignoring headers
  # data = request.get_json (force = True)
  data = request.form
  app.logger.info ("POST gfd: {0} {1}".format(username, data))

  response = {  "result" : "OK" }
  for k in data:
    response[k] = data[k]

  app.logger.info ("POST gfd: {0} {1}".format(username, data))

  return jsonify (response)
