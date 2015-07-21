#!/usr/bin/env python

"""
 This script will check the data saved to MySQL against datafile.

 It simply counts number of rows for every table and compares
 it with line numbers of corresponding files.

 To run this you should first run in command line:

    export PYTHONPATH="/webapps/housing_survey/:$PYTHONPATH"

  And then just run it with python bin/check.py
"""
import initializers.framework
import initializers.data as di

from datatype.saver.models import Checker, Settings

for year in di.YEARS:
    for base_name in di.FILES:
        try:
            settings = Settings(year, base_name)
            Checker(settings).check()
        except IOError:
            print "No file %s.csv for year %d, skipping..." % (base_name, year)
