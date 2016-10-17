from everything import *
from faculty import getLDAPFaculty


@app.route('/login', methods=['GET'])
def login():
        # get the user from shibboleth
        system_user = authUser(request.environ)
        
        # look for user in our database
        user = getLDAPFaculty(system_user)
        if user is None:
            abort(403)
        else:
            login_user(user)
            print user.username
        return "something"
            

@app.route('/logout')
def logout():
    logout_user()
    return redirect('http://login.berea.edu/idp/profile/Logout')
            