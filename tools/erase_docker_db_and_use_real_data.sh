#! /bin/bash

# Remove the existing database and
# start from a production backup
####################################

DATA_FILE=prod-data.sql
TARGET=docker
source rewrite_db.sh
