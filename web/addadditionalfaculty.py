from everything import *

#################################################################
# STEP 3: addfaculty()
# POST
#   Store the data. Redirect to the GET.
# GET
#   Allow the user to enter more faculty.
@app.route('/{0}/<username>/addadditionalfaculty'.format(cfg['tag']), methods = ['GET', 'POST'])
def addadditionalfaculty (username):
  app.logger.info("Made it to storeadditionalfaculty().")
  
  if (session['username'] != os.getenv('USERNAME')):    
    redirect (url_for ("init"))

  if request.method == 'POST':
    pass

  else:
    app.logger.error("storeadditionalfaculty: GET")
    return render_template('addadditionalfaculty.html',
                            username = username,
                            tag  = cfg['tag'],
                            next = "addadditionalfaculty"
                            )
