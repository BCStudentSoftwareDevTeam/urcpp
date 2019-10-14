# Remove the existing database and
# start from a given backup
####################################

if [ ${0##*/} == "rewrite_db.sh" ]; then
	echo "Don't call this file directly, please. Use one of the other scripts.";
	exit 1
fi

if [ -z "$DATA_FILE" ]; then
	echo "You must provide a db dump .sql in \$DATA_FILE.";
	exit 1
fi

DATA_LINK=2_db-data.sql

printf "Switching to database/$DATA_FILE..."
pushd ../database/docker_init > /dev/null
rm $DATA_LINK
cp ../$DATA_FILE $DATA_LINK
popd > /dev/null
echo "Done"

# If we want to mess with the docker db
if [ "$TARGET" == "docker" ] ; then
	printf "Removing existing database volume..."
	sudo rm -r ../docker/data/db/*

	printf "Done.\n\nStop your docker containers. The next 'docker-compose up' will load the new database.\n"

# if we are using mysql locally, run the sql files directly
else
	MYSQL_CONN="--defaults-extra-file=mysql.conf"

	echo "Creating backup in tools/backup.sql. Remove if not needed."
	mysqldump $MYSQL_CONN urcpp_flask > backup.sql
	echo "DROP USER urcpp_flask; DROP DATABASE urcpp_flask;" | mysql $MYSQL_CONN
	cat ../database/docker_init/*.sql | mysql $MYSQL_CONN
fi
