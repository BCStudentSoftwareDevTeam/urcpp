from flask import Flask

app = Flask(__name__)

# The init and router: / and the /{tag}/{username}/{next} routes
import web.main
import web.static

# Individual Pages
import web.pages
import web.store

# JSON Endpoints
import web.endpoints
