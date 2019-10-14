#! /bin/bash

# Remove the existing database and
# start using an empty one
####################################

DATA_FILE=dummy-data.sql
TARGET=docker
source rewrite_db.sh
