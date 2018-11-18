#!/bin/bash

mysql -uroot -e "CREATE USER 'ola'@'%' IDENTIFIED BY 'ola'"
mysql -uroot -e "CREATE DATABASE ola"
mysql -uroot -e "GRANT SELECT ON ola.* TO 'ola'@'%'"

mysql -u root ola < ola.sql

mysql -uroot -e "GRANT INSERT ON ola.user TO 'ola'@'%'"
mysql -uroot -e "GRANT INSERT ON ola.enrollment TO 'ola'@'%'"
mysql -uroot -e "GRANT INSERT ON ola.message TO 'ola'@'%'"
