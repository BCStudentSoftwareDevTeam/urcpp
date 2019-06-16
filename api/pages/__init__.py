from flask import Blueprint

pages = Blueprint('pages', __name__)

from api.pages import budget
from api.pages import create
from api.pages import done
from api.pages import download
from api.pages import history
from api.pages import irbyn
from api.pages import people
from api.pages import upload
