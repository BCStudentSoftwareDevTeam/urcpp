# Working with URCPP

## Important things to know before developing

  - Uses Python 2.7
  - There is still sqlite code in here, but we are using mysql

## Quick Installation Guide with Docker

1. Ensure that you have the proper binaries installed by running `which docker docker-compose` and verifying the output (there should be a path for both). New student VMs should already be ready. If you do not have them, install them.
	* `sudo apt-get install docker.io`
	* Use the Linux instructions from https://docs.docker.com/compose/install/
	* Your user should be in the docker group or you will need sudo privileges.
2. Clone this repository.
3. In your new repo directory, use docker-compose to start your application.
	* `docker-compose up`
	
4. If this is successful, access your application at your server + the port
	* If on your computer: http://localhost:8080
	* If on your student VM, use that IP: e.g., http://172.31.3.69:8080
5. The application data will persist in your docker/data/db/ directory. To re-initialize it, use the appropriate script in tools/.
6. To understand more about using Docker and docker-compose, read http://172.31.2.178/en/docker.

## Manual Installation Guide

### Necessary packages and configuration
1. Ensure you have the necessary packages to run this application.
	* `apt install git mysql-server python2.7 python-pip virtualenv`
2. You must be using Python 2.7
	* If you are unsure how to fix this, read http://172.31.2.178/en/python-versions
3. Ensure you have access to the git repo using ssh keys
	* Try and clone this repository. If it doesn't work, do the next step
	* Paste your public key into bitbucket
	* If you are unsure how to get your key, read http://172.31.2.178/en/ssh
4. Clone this repo.

### Database Setup
1. Ensure MySQL is running, with the proper root password set
	* test with `mysql -u root --password="root"` 
	* if you can't connect and you do not have sudo privileges, someone will have to set this up for you
	* `sudo systemctl start mysql`
	* `echo "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root'; flush privileges;" | sudo mysql -u root --password=root`
2. Create the user and database
	* This will erase any existing data!
	* There will be ignorable errors if this is the initial setup.
	* Run `./erase_mysql_db_and_use_real_data.sh` from the tools directory.
3. Edit the application configuration for your db host.
  * In `api/config.yaml`, change your database host from "db" to your mysql host (e.g., "localhost")

### Application Setup
1. Initialize the application: `./setup.sh`
2. Activate your virtual environment: `source venv/bin/activate`
3. Run the application: `python api.py`
4. If this is successful, access your application at your server + the port
	* If on your computer: http://localhost:8080
	* If on your student VM, use that IP: e.g., http://172.31.3.69:8080
5. The application data will persist in mysql database. To re-initialize it, use the appropriate script in tools/.

## Customization and Troubleshooting

### Database Config

### Common Errors
  * If you run into this error `bind: address already in use`, run the following command:
   `sudo systemctl stop mysql`



### OLD BITS 
4. run `phpmyadmin-ctl install` to run the phpmyadmin client.
5. navigate to the phpmyadmin interface

