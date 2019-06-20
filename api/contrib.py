from everything import *


@app.route("/contributor", methods = ["GET"])
def contributors():
    return render_template("contrib.html", cfg = cfg)