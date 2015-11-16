######################################################
# IMPORTS
######################################################
# Python 2/3 compat
from __future__ import print_function
import os
# We need a bunch of Flask stuff
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import g
from flask import session
# We need to import the DB object
from models import theDB

# Don't forget to import your own models!
from models import Secret, RegLinks
import uuid

######################################################
# SETUP
######################################################
# Set up the Flask app
from web import app

# We have to set up and break down the DB on every request.
@app.before_request
def before_request():
  g.db = theDB
  g.db.connect()

@app.after_request
def after_request(response):
  g.db.close()
  return response

######################################################
# ROUTES
######################################################

# STEP 1: We begin by going to the root, which bounces
# us over to the signin page.
@app.route("/")
def hello ():
  return redirect(url_for('start'))

@app.route('/s/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

# STEP 2: We have the option of signing in, or
# requesting a registration email. That email sends us a validation
# link. Only people with Berea addresses can receive that email.
@app.route('/start', methods = ['GET', 'POST'])
def start ():
  # If we're working with an authenticated web server, the environment
  # should already hold the username.
  app.logger.info("USER: %s" % os.getenv('USER'))

  if request.method == 'GET':
    return render_template('start.html', user = os.getenv('USER'))

  if request.method == 'POST':
    email  = request.form['email']
    digits = request.form['digits']
    s = Secret.get(Secret.email == email)
    secret = s.secret
    print ("secret: %s" % secret)
    tweb = pyotp.TOTP(secret)
    calculated = tweb.now()
    if tweb.verify(digits):
      print ("They match: {0}".format(digits))
    else:
      print ("They did not match: digits[{0}] calc[{1}]".format(digits, calculated))


  return redirect(url_for('signin'))

def make_qr_code (uri):
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
  )
  qr.add_data(uri)
  qr.make(fit=True)
  img = qr.make_image()
  return img

# STEP 3: When we hit the requestlink page, we either
# came here as a GET or a POST. A GET means that we should
# let people put in their email address. A post means they
# filled out the form. When the form is filled out, we grab the email
# address, generate a registration link, stuff it into the RegLinks
# table, and send them an email.
#
# We bounce back to the signin page when we're done here.
#
# FIXME: We might want timeouts on these, and for now, I'm just printing.
#
# Use: https://chrome.google.com/webstore/detail/authenticator/bhghoamapcdpbohphigoooaddinpkbai?hl=en

@app.route('/requestlink', methods = ['GET', 'POST'])
def requestlink ():
  if request.method == 'GET':
    return render_template('request.html')

  if request.method == 'POST':
    link = uuid.uuid4().get_hex()
    reg = RegLinks (email = request.form['email'], link = link)
    reg.save()

    # Send the link
    print ("Link [{0}] for {1}.".format(link, request.form['email']))

    # Just for now...
    print ("https://csc-berea-jadudm.c9.io/validate/{0}".format(link))

    return redirect(url_for('signin'))


# STEP 4: Given a validation link, we can check: did they receive the
# email? If they did, we can look them up and say "Yes! They did!"
# If they did receive an email, we can safely bounce them over to the
# registration page.
#
# We pass that validation link on to the registration page.
@app.route('/validate/<link>', methods = ['GET'])
def validate (link):
  if (request.method == 'GET'):
    found = True
    try:
      r = RegLinks.get(RegLinks.link == link)
    except RegLinks.DoesNotExist:
      found = False
    if found:
      print ("Found {0} with link {1}.".format(r.email, r.link))
      return redirect('/register/{0}/{1}'.format(r.email, r.link))
    else:
      return "Not found: %s" % link


# STEP 5: We now have a page where the user is going to scan their QR code.
# By doing so, we now have their shared secret in the DB. This means they
# can come back later with their email address and six-digit TOTP, and log
# in. There are security issues that should be explored, but it is
# better than nothing, and should be "more than secure enough" for the purposes.
@app.route('/register/<email>/<link>', methods = ['GET'])
def register (email, link):
  # If it is the initial page request

  # If someone is requesting an email.
  if request.method == 'GET':
    found = True
    try:
      r = RegLinks.get(RegLinks.link == link)
    except RegLinks.DoesNotExist:
      found = False

    if found and r.email == email:
      global APPNAME

      data = {}
      data['email'] = email
      sharedsecret = pyotp.random_base32()
      tweb = pyotp.TOTP(sharedsecret)
      key = "{0} @ {1}".format(data['email'], APPNAME)

      s = Secret (email = email, secret = sharedsecret)
      s.save()

      data['tweb-uri']  = tweb.provisioning_uri(key)
      data['qr']   = make_qr_code(data['tweb-uri'])
      data['img-fname'] = "{0}.png".format(uuid.uuid4())
      data['qr'].save("web/static/qr/{0}".format(data['img-fname']))

      return render_template('qr.html', data = data)



# start the server with the 'run()' method
#if __name__ == '__main__':
#  app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)
