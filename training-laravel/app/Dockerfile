FROM ubuntu:18.04

# ----- set up utils
RUN apt-get update && \
    apt-get install -y \
      sudo \
      curl \
      vim \
      expect \
      nginx || \
    apt-get install -y --fix-missing \
      sudo \
      curl \
      vim \
      expect \
      nginx

# ----- set up php
RUN expect -c " \
      set timeout 1000; \
      spawn apt-get -y install php; \
      expect \"Geographic area:\"; \
      send \"6\"; \
      expect \"Time zone:\"; \
      send \"78\"; \
      expect eof; \
    "

RUN apt-get install -y \
      php-common \
      php-fpm \
      php-json \
      php-mbstring \
      php-mysql \
      php-xml \
      php-zip || \
    apt-get install -y --fix-missing \
      php-common \
      php-fpm \
      php-json \
      php-mbstring \
      php-mysql \
      php-xml \
      php-zip

# ----- set up composer
RUN curl https://getcomposer.org/installer | \
    php -- --install-dir=/usr/local/bin --filename=composer

# ----- set up global
RUN composer global require "laravel/installer"
ENV PATH $PATH:/root/.composer/vendor/bin

# ----- add user
RUN useradd -d /home/sdarw -m -s /bin/bash sdarw
RUN echo sdarw:sdarw | chpasswd
RUN echo 'sdarw ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers