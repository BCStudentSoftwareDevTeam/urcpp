## Important things to know before developing locally or in C9

  - You will notice a bunch of sqlite related code, but we are no longer using sqlite
  - You will need to have mysql and python mysql-db
 
# c9 Installation Guide #

1. Create a work space in c9 with the python template and the github ssh url.
2. run `git pull` to ensure latest changes are pulled.
3. run `source setup.sh` to execute setup script.
4. run `phpmyadmin-ctl install` to run the phpmyadmin client.
5. navigate to the phpmyadmin interface
6. create a database named `urcpp_flask_v2`
7. add a user named `urcpp-flask` with read and write permissions on the db
8. comment out lines 20-27 in `__init__.py`
9. run `python recreate_static`
10. run `python recreate_dynamic`
11. comment lines 20-27 back in
12. run `python api.py`
