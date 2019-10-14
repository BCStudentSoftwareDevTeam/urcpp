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
echo "done"

# If we want to mess with the docker db
if [ "$TARGET" == "docker" ] ; then
	printf "Removing existing database volume..."
	sudo rm -r ../docker/data/db/*

	printf "done.\n\nStop your docker containers. The next 'docker-compose up' will load the new database.\n"

# if we are using mysql locally, run the sql files directly
else
	MYSQL_CONN="--defaults-extra-file=mysql.conf"

	printf "Creating backup in tools/backup.sql..."
	mysqldump $MYSQL_CONN urcpp_flask > backup.sql
	echo "done. Remove if not needed."

	printf "Dropping existing user and database..."
	echo "DROP USER urcpp_flask; DROP DATABASE urcpp_flask;" | mysql $MYSQL_CONN
	echo "done"

	printf "Reinitializing database from database/docker_init/*.sql..."
	cat ../database/docker_init/*.sql | mysql $MYSQL_CONN
	echo "done"
fi
