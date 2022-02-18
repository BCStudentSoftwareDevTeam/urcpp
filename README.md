## Requirements
- Python2.7
- linux, unix, mac, windows(with attachments), Ubuntu
- virtualenv
- mysql and python mysql-db

## Setup
1. In your working environment, clone the URCPP Repo:
`https://github.com/BCStudentSoftwareDevTeam/urcpp` as of 02/10/2022
3. Pull the most recent changes
4. In the file `setup.sh` add lineRun `source setup.sh`
### Create database with Phpmyadmin
(Skip to step 9 if you want to setup using MYSQL Workbench and Terminal)
5. Go to your Phpmyadmin interface and log in with your credentials
Located here: `http://0.0.0.0/phpmyadmin/`
Make sure to replace 0.0.0.0 with your server's IP address
6. Create a new database named `urcpp_flask_v2`
If a database of that name already exists, drop it and create it again
7. Create a user named `urcpp-flask` with password `DanforthLabor123!`
8. Grant all permissions on the database `urcpp_flask_v2` to `urcpp-flask`
Continue to step 13.
### Create database with MySQL Workbench and Terminal
(Skip this if you have set up with Phpmyadmin)
9. In your terminal use the command `mysql -u root -p`. You will be prompted to enter your password
10. To create the database: `CREATE DATABASE urcpp_flask_v2;` (Make sure you include the ;)
11. To create a user named `urcpp-flask` with password `DanforthLabor123!`: `CREATE USER 'urcpp-flask'@localhost IDENTIFIED BY 'DanforthLabor123!'; `
11. To Grant all permissions on the database `urcpp_flask_v2` to `urcpp-flask`: ` GRANT ALL PRIVILEGES ON `urcpp_flask_v2` . * TO 'urcpp-flask'@localhost; `
12. To make sure permissions take effect: ` flush privileges; `

13. Create a file named `secret_key` in the `api` folder
`secret_key` MUST contain some alphanumeric characters. Anything will work including `AnythignWillWork`
14. Comment out lines 20-27 in `api/__init__.py`
15. Run `python recreate_static.py`
16. Run `python recreate_dynamic.py`
17. Comment lines 20-27 in `api/__init__.py` back in
18. Run `python api.py`
