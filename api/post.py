from everything import *

# https://github.com/micha/resty
# Also, Postman in Chrome
# Also, http://blog.luisrei.com/articles/flaskrest.html
# Also, https://github.com/jpillora/jquery.rest

@app.route ("/urcpp/1/gfd/<username>", methods = ["POST"])
def getfacultydetails (username):
  # force is for ignoring headers
  # data = request.get_json (force = True)
  data = request.form
  app.logger.info ("POST gfd: {0} {1}".format(username, data))

  response = {  "result" : "OK" }
  for k in data:
    response[k] = data[k]
  return jsonify (response)
