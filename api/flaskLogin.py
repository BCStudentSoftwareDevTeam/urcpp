from everything import *
from API.faculty import getLDAPFaculty
from redirectback import redirect_url


@app.route('/login', methods=['GET'])
def login():
        # get the user from shibboleth
        system_user = authUser(request.environ)
	print(system_user)        
        # look for user in our database
        user = getLDAPFaculty(system_user)
        if user is None:
            abort(403)
        else:
            login_user(user)
        return redirect(redirect_url())
            

@app.route('/logout')
def logout():
    logout_user()
    return redirect('https://login.berea.edu/idp/profile/Logout')
            
