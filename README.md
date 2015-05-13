![](https://api.travis-ci.org/kiote/housing_survey.svg)

## Intro

This project imports data from American Housing Survey (AHS) to MySQL database.

# Installation

## Requirements

- Git
- Python - should be in your system already
- [Ansible](http://docs.ansible.com/intro_installation.html)
- [Vagrant](http://www.vagrantup.com/downloads.html)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## Init script

First of all please create project's working dir (any name you wish). For example:

```
mkdir ahsdata
```

Then, change your current dir to just created:

```
cd ahsdata
```

Finally, run 

```
(curl -s https://raw.githubusercontent.com/kiote/housing_survey/master/bin/init_machine) | python
```

this script will download all environment and will try to run VM. This could take some time, 
since this script is trying to download packaged VM, which is about 1Gb.

After it finished you should be able to ssh into VM:

```
cd ansible-django-stack
vagrant ssh
```

Now you can do whatever you want with mysql:

```
mysql -uahs -p12345
```
