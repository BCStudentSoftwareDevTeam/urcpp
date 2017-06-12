## Important things to know before developing locally or in C9

  - You will notice a bunch of sqlite related code, but we are no longer using sqlite
  - You will need to have mysql and python mysql-db
  - Start your mysql server and add a database with following username and password
    - Database Name: urcpp_flask
    - User Name: urcspp-flask
    - User Password: DanforthLabor123!

  - Alternatively, the following MySQL queries can be used:
    - CREATE DATABASE urcpp_flask;
    - CREATE USER 'urcpp-flask'@'%' IDENTIFIED BY 'DanforthLabor123!';
    - GRANT ALL ON urcpp_flask.* TO 'urcpp-flask'@'localhost' IDENTIFIED BY 'DanforthLabor123!';
  - Then run recreate_static.py followed by recreate_dynamic.py
  - Now you can run setup.sh to setup and serve this application.