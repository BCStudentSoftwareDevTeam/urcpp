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
pip install sqlite-web
pip install pyotp
pip install qrcode
pip install pyyaml

# For QR Codes
pip install Pillow
pip install git+git://github.com/ojii/pymaging.git#egg=pymaging
pip install git+git://github.com/ojii/pymaging-png.git#egg=pymaging-png

# Database setup
python recreate.py

# To deactivate the venv, use
#
# $ deactivate
#
# as a command on the command line.
# To set up the venv again, then type
#
# $ source setup.sh
