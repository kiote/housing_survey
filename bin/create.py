#!/usr/bin/env python

"""
 This script will generate files with Python-syntax to generate models.

 Manual steps are commented, but they are required

 To run this you should first run in command line:

    export PYTHONPATH="/webapps/housing_survey/:$PYTHONPATH"

  And then just run it with python bin/create.py
"""
import initializers.framework
import initializers.data as di

from datatype.determiner.models import DatabaseSaver
from datatype.determiner.models import FileSaver

for year in di.YEARS:
    for base_name in di.FILES:
        print "%d: %s" % (year, base_name)
        try:
            DatabaseSaver(year, base_name).write_types()
            FileSaver(year, base_name).generate_columns()
        except IOError:
            print "No file %s.csv for year %d, skipping..." % (base_name, year)

# copy columns to the model file
# run makemigrations
# run migrate
# run load_data.py
