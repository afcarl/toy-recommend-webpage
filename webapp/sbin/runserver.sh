#!/bin/bash

export __CURRENT_DIR=`basename $0`
pushd "$__CURRENT_DIR"

export __PYTHON='python3'
export __IP_ADDRESS='192.168.111.228'
export __PORT='8000' 
$__PYTHON manage.py runserver "${__IP_ADDRESS}:${__PORT}"
