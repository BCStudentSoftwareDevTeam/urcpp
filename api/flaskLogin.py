from everything import *
from API.faculty import getLDAPFaculty
from redirectback import redirect_url


@app.route('/login', methods=['GET'])
def login():
        # get the user from shibboleth
        print "Started the login process"
        system_user = authUser(request.environ)
        print "Logging in as", system_user
	

	envK = "eppn"  # AD data from Shibboleth

  	if (envK not in request.environ):        
            request.environ['sn'] = "Testuser"
            request.environ['givenName'] = "Test"
	
        # look for user in our database
        user, created = LDAPFaculty.get_or_create(
                            username = system_user,
                            defaults = {
                                'lastname': request.environ['sn'],
                                'firstname': request.environ['givenName'],
                                'bnumber': "B00000000",
                            });
        if created:
            print "User created for", system_user

        login_user(user)

        return redirect(redirect_url())
            

@app.route('/logout')
def logout():
    logout_user()
    return redirect('https://login.berea.edu/idp/profile/Logout')
