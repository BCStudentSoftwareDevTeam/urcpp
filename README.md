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
7. add a user named `urcpp-flask` with password `DanforthLabor123!` and check `grant all permissions on database urcpp_flask_v2`
   - See instructions [here](https://docs.google.com/document/d/1K2Ex8xsa65SwvCG3UdZ9bL-hLey9rTguOA9kfbENtwY/edit?usp=sharing) for more aid
8. comment out lines 20-27 in `api/__init__.py`
9. create a file `api/secret_key` with alphanumeric characters in the file
9. run `python recreate_static`
10. run `python recreate_dynamic`
11. comment lines 20-27 back in
12. run `python api.py`
13. if application does not load, comment out lines 80-83 in 'urcpp-flask/api/everything.py'
14. to initialize mysql, run 'mysql-ctl install' and answer 'Y'
