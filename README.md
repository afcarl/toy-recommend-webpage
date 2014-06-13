toy-recommend-webpage
=====================

Trying to create a simple recommendation web system

## Requirement

- Vagrant

## Components

- Vagrant on VirtualBox
    - Ubuntu 12.04 precise
- Web Framework
    - Djangoh
- Machine Learning Library 
    - Scikit-Learn

## Building This Project

### Launch a Vagrant instance

`/vagrant` on the vagrant is linked to the basic path of this project.
The IP address of the lanched machine is set as `192.168.111.228`.
Please check `./vagrant/Vagrantfile`.

```
cd ./vagrant
vagrant up
```

### Launch Django Server

#### SSSH Login to The Vagrant Machine

You have to execute command on your host machine.

```
cd ./vagrant
vagrant ssh
```

#### Launch Django Server on Vagrant

You have to execute command on the vagrang machine.

```
cd /vagrant/webapp
./sbin/runserver.sh
```

#### Check Whether The Django Server is correctly executed

You need to brows on your host machine.
Please see also `./webapp/sbin/runserver.sh` which is the script to launch django server.

```
curl http://192.168.111.228:8000/
```


