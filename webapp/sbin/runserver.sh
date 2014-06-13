#!/bin/bash

export __CURRENT_DIR=`basename $0`
pushd "$__CURRENT_DIR"

export __IP_ADDRESS='192.168.111.228'
export __PORT='8000' 
python manage.py runserver "${__IP_ADDRESS}:${__PORT}"
