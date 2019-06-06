from everything import *
import os

print("Contributors page is loaded")
@app.route("/contributors", methods = ["GET"])
def contributors():
    print("Here's my print sttaement")
    print("Current directory: " + os.getcwd())
    return render_template("/api/templates/contributors.html")