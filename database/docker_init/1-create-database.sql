CREATE DATABASE IF NOT EXISTS `urcpp`;
CREATE USER 'urcpp_flask'@'%' IDENTIFIED BY 'DanforthLabor123!';
GRANT ALL PRIVILEGES ON *.* TO 'urcpp_flask'@'%' WITH GRANT OPTION;
USE `urcpp`;
