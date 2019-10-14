#! /bin/bash

# Source this.
# Setup virtualenv
#mkdir -p data

if [ ! -d venv ]
then
  virtualenv venv
fi

. venv/bin/activate

pip install -r requirements.txt

# TODO create a db script that can use the docker init builder

# Set up config files
FILE=${PWD}/api/secret_key
if [ ! -f "$FILE" ]; then
	echo "Generating secret key"
	head /dev/urandom | tr -dc A-Za-z0-9 | head -c 14 > $FILE
fi

# Make sure api/settings.py is present
FILE=${PWD}/api/settings.py
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

