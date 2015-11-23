from everything import *

# @app.route ("/s/<path:path>", methods = ["GET"])
# def templates (path):
#   return send_from_directory (path)

@app.route ("/t/<path:path>", methods = ["GET"])
def templates (path):
  return render_template ( path, 
                           username = os.getenv('USER'),
                           cfg = cfg
                        )

@app.route("/", methods = ["GET"])
def main ():
   return render_template ("urcpp.html", 
                           username = os.getenv('USER')
                           )
