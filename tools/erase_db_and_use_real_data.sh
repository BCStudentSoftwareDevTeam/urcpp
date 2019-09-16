#! /bin/bash

# Remove the existing database and
# start from a production backup
####################################

DATA_FILE=prod-data.sql
source rewrite_db.sh
