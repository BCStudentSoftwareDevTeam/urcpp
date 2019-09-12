# Source this.
# Setup virtualenv
mkdir -p data

if [ ! -d venv ]
then
  virtualenv venv
fi

. venv/bin/activate

pip install Flask
pip install peewee
pip install pyyaml
# For security, for LDAP
pip install pyopenssl ndg-httpsclient pyasn1
pip install ldap3
# For docs
pip install mkdocs
pip install gunicorn
pip install tornado

# additional python library
pip install XlsxWriter

#for login
pip install Flask-Login
pip install PyMySQL
# For QR Codes
pip install flask-wtf
pip install wtf-peewee
#flask-mail library
pip install Flask-Mail
#pip install sqlite-web
#pip install pyotp
#pip install qrcode
#pip install Pillow
#pip install git+git://github.com/ojii/pymaging.git#egg=pymaging
#pip install git+git://github.com/ojii/pymaging-png.git#egg=pymaging-png

# Database setup
# python recreate_dynamic.py

# Set up config files

FILE=${PWD}api/secret_key
if [ ! -f "$FILE" ]; then
	echo "Generating secret key"
	head /dev/urandom | tr -dc A-Za-z0-9 | head -c 14 > $FILE
fi

# Make sure api/settings.py is present
FILE=${PWD}api/settings.py
if test -f "$FILE"; then
	echo "$FILE exists"
else 
   touch $FILE
   echo "$FILE created"
fi
echo "Remember to edit your mail settings in $FILE"

# To deactivate the venv, use
#
# $ deactivate
#
# as a command on the command line.
# To set up the venv again, then type
#
# $ source setup.sh

