#!/usr/bin/env bash

## Environment Variables
# docker
export DOCKER_HOST=localhost

## apt
APT_GET_INSTALL='apt-get install -y --force-yes'
apt-get update -y
apt-get upgrade -y
# apache
$APT_GET_INSTALL apache2 
# mysql
debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password password root'
debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password_again password root'
$APT_GET_INSTALL mysql-server
## sqlite
$APT_GET_INSTALL sqlite sqlite3
# git
$APT_GET_INSTALL git
# python
$APT_GET_INSTALL python python-numpy python-scipy python-django python-mysqldb python-nose python-matplotlib python-pip python-sklearn
# pip update
pip install -U pip-tools
pip-review --auto
#pip freeze --local | cut -d = -f 1  | while read i; do pip install -U $i; done
# misc
$APT_GET_INSTALL screen bash-completion

## Django
#pip install Django==1.6.5

## Restart service(s)
service mysql restart
