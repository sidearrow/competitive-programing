FROM php:7.2-fpm

WORKDIR /tmp

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y \
        git

RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer

WORKDIR /var/www

RUN rm -r html