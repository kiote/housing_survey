![](https://api.travis-ci.org/kiote/housing_survey.svg)

## Intro

This project imports data from American Housing Survey (AHS) to MySQL database.

# Installation

## Requirements

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
mysql -uahs -p123456
```

##

# Development Info

In case you are going to run through all import data process manually:

# Import data

Since github can't store big files, you should run downloader (under vagrant shell):
 
 ```
 cd /webapps/housing_survey
 source bin/activate
 cd housing-survey
 python manage.py shell < bin/import.py
 ```

# Project Structure

This project has default django-project structure, with several extra folders (see below).

### Data Files (/data)

There are several files, which helps this app to work:

#### File with columns and datatypes (/data/columns)

Contains auto-generated files for each table, this files should not be manually edited.

```
data/columns/newhouse.csv
```

This file describes all columns and corresponding datatypes for those columns to generate Newhouse model.

```
data/columns/generated/newhouse.gen
```

generated (data fields with python-like syntax).
This generated data then being copied and pasted to Newhouse model.

#### Initial data files (/data/initial)

Contains seed data for django-app, which creates admin user.
Default login to admin interface is ```admin``` with password ```pass```

#### Non-git files (/data/non-git)

Original data files, see [Import data](https://github.com/kiote/housing_survey#import-data) section

#### Sample files (/data/sample)

```
data/sample/puf2013/newhouse.csv
```

contains small part of original AHS data, for unit-tests.
