from everything import *

@app.route('/{0}/start'.format(cfg['tag']), methods = ['GET'])
def start ():
  username = session['username']
  if (username != os.getenv('USERNAME')):    
    redirect (url_for ("init"))

  
  return render_template('start.html',
                          username = session['username'],
                          tag  = cfg['tag'],
                          next = "storecommunicating"
                          )

@app.route('/{0}/addadditionalfaculty'.format(cfg['tag']), methods = ['GET'])
def addadditionalfaculty ():
  username = session['username']
  if (username != os.getenv('USERNAME')):    
    redirect (url_for ("init"))
  
  return render_template('addadditionalfaculty.html',
                          username = session['username'],
                          tag  = cfg['tag'],
                          next = "storeadditionalfaculty"
                          )
  
