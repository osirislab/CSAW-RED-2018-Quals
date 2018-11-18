FROM mattrayner/lamp:latest-1604

RUN apt-get update && apt-get install -y chromium-browser

COPY ./html /var/www/html/
RUN chmod -R a-w /app
RUN rm -rf /var/www/phpmyadmin
RUN rm -rf /var/www/phpMyAdmin*

COPY ./flag2.txt /var/www/
RUN chmod a-w /var/www/flag2.txt

COPY ./flag3.txt /
RUN chmod a-w /flag3.txt

COPY ./init_db.sh /
COPY ./ola.sql /
RUN chmod +x /init_db.sh

RUN sed -i '$i/init_db.sh' /create_mysql_users.sh
