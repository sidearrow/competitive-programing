FROM php:7.2-fpm

WORKDIR /tmp

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y \
        git \
        zlib1g-dev

RUN docker-php-ext-install pdo_mysql zip

RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer && \
    export PATH=$PATH:/root/.composer/vendor/bin

WORKDIR /var/www

RUN rm -r html