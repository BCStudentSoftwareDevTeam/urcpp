from web import app
import os

# Run with 
# $ IP=0.0.0.0 PORT=8080 python run.py 
# or similar
app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)
