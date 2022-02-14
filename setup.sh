#! /bin/bash

# Source this.
# Setup virtualenv
#mkdir -p data

if [ -d venv ]
then
  echo "Deactivating and removing old virtualenv"
  deactivate 2>&1 /dev/null
  rm -rf venv
fi

# Check for correct python version
VERSION=`python2 -V | awk '{print $2}'`
if [ "${VERSION:0:1}" -ne "2" ] || [ "${VERSION:2:1}" -ne "7" ]; then
	     echo "You must use Python 2.7. You are using $VERSION"
	     return 1
else
	echo -e "You are using Python $VERSION"
fi

virtualenv --python=python2.7 venv
. venv/bin/activate

pip install -r requirements.txt

# TODO create a db script that can use the docker init builder
# Check out tools/erase_mysql_db_and_use_real_data.sh

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

