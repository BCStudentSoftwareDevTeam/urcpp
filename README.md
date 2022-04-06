## Requirements
- Python2.7
- linux, unix, mac, windows(with attachments), Ubuntu
- virtualenv
- mysql and python mysql-db

## Setup
1. In your working environment, clone the URCPP Repo:
- `https://github.com/BCStudentSoftwareDevTeam/urcpp` as of 02/10/2022
3. Pull the most recent changes
4. Run `source setup.sh`

## Create database with Phpmyadmin

5. Go to your Phpmyadmin interface and log in with your credentials
- Located here: `http://0.0.0.0/phpmyadmin/`
Make sure to replace 0.0.0.0 with your server's IP address
6. Create a new database named `urcpp_flask`
- If a database of that name already exists, drop it and create it again
7. Create a user named `urcpp_flask` with password `DanforthLabor123!`
8. Grant all permissions on the database `urcpp_flask` to `urcpp_flask`
Continue to step 14.

## Create database using MYSQL commands

9. In your terminal use the command `mysql -u root -p`. You will be prompted to enter your password
10. Create the database: ` CREATE DATABASE urcpp_flask; `
11. Create a user with given password:  ` CREATE USER 'urcpp_flask'@localhost IDENTIFIED BY 'DanforthLabor123!'; `
12. Grant all permissions: ` GRANT ALL PRIVILEGES ON 'urcpp_flask' . * TO 'urcpp_flask'@localhost; `
13. Make sure permissions take effect: ` flush privileges; `

## Continue from here again
14. Run `python api.py`
