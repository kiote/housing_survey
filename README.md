![](https://api.travis-ci.org/kiote/housing_survey.svg)

## Intro

This project imports data from American Housing Survey (AHS) to MySQL database.

## Import data

Since github can't store big files, you should run downloader (under vagrant shell):
 
 ```
 cd /webapps/housing_survey
 source bin/activate
 cd housing-survey
 python manage.py shell < bin/import.py
 ```

## Project Structure

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
