# Remove the existing database and
# start from a given backup
####################################

if [ -z "$DATA_FILE" ]; then
	echo "You must provide a db dump .sql in \$DATA_FILE.";
	exit 1
fi

DATA_LINK=2_db-data.sql

printf "Removing existing database volume..."
sudo rm -r ../docker/data/db/*
echo "Done"

printf "Switching to database/$DATA_FILE..."
cd ../database/docker_init
rm $DATA_LINK
ln -s ../$DATA_FILE $DATA_LINK

printf "Done.\n\nStop your docker containers. The next 'docker-compose up' will load the new database.\n"
