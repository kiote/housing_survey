# 1. How To Apply New Indexes

## On host machine:
* ```cd /path/to/housing/survey/```
* ```git pull``` – get new code version
* ```vagrant ssh``` – open VM terminal

## On virtual machine:
* ```cd /webapps/housing_survey/``` – move to project's dir
* ```source bin/activate``` – activate python environment
* ```cd housing-survey``` – move to app's dir
* ```python manage.py migrate``` – run new migrations (add indexes)