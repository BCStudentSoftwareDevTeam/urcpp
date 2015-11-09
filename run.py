from otp import app
import os

app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)
