#!/usr/bin/env bash

## Environment Variables
# docker
export DOCKER_HOST=localhost

## apt
APT_GET_INSTALL='apt-get install -y --force-yes'
apt-get update -y
#apt-get upgrade -y
# apache
$APT_GET_INSTALL apache2 
# mysql
debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password password root'
debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password_again password root'
$APT_GET_INSTALL mysql-server
## sqlite
$APT_GET_INSTALL sqlite sqlite3
## redis
$APT_GET_INSTALL redis-server
# git
$APT_GET_INSTALL git
# python3
$APT_GET_INSTALL python3 python3-dev python3-numpy python3-scipy python3-nose
#python-numpy python-scipy python-django python-mysqldb python-nose python-matplotlib python-pip python-sklearn
# pip update
$APT_GET_INSTALL curl libfreetype6 libfreetype6-dev libatlas-dev libatlas-base-dev build-essential
curl -kL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python3
__PIP_PACKAGES="
pip pip-tools versiontools Django==1.6.5 freetype2
matplotlib scikit-learn==0.14.1
pymysql django-mysql-pymysql redis django-redis
"
for __PACKAGE in $__PIP_PACKAGES
  do
    #pip install -U "$__PACKAGE"
    pip install "$__PACKAGE"
  done
# misc
$APT_GET_INSTALL screen bash-completion

## apt
#apt-get upgrade -y

## Restart service(s)
service mysql restart
