**Requirements**
- Python2.7
- linux, unix, mac, windows(with attachments), Ubuntu
- virtualenv
- mysql and python mysql-db

**Setup**
1. In your working environment, clone the URCPP Repo:
- `https://github.com/BCStudentSoftwareDevTeam/urcpp` as of 02/10/2022
3. Pull the most recent changes
4. In the file `setup.sh` add lineRun `source setup.sh`
5. Go to your Phpmyadmin interface and log in with your credentials
- Located here: `http://0.0.0.0/phpmyadmin/`
- Make sure to replace 0.0.0.0 with your server's IP address
6. Create a new database named `urcpp_flask_v2`
- If a database of that name already exists, drop it and create it again
7. Create a user named `urcpp-flask` with password `DanforthLabor123!`
8. Grant all permissions on the database `urcpp_flask_v2` to `urcpp-flask`
9. Create a file named `secret_key` in the `api` folder
- `secret_key` MUST contain some alphanumeric characters. Anything will work including `AnythignWillWork`
10. Comment out lines 20-27 in `api/__init__.py`
11. Run `python recreate_static.py`
12. Run `python recreate_dynamic.py`
13. Comment lines 20-27 in `api/__init__.py` back in
14. Run `python api.py`
