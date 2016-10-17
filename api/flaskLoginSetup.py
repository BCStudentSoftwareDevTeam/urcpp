import flask_login as flask_login
from everything import *

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def user_loader(username):
    return User.get(User.username=username)