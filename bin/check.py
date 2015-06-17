"""
 This script will check the data saved to MySQL against datafile.
 It simply counts number of rows for every table and compares
 it with line numbers of corresponding files.

 To run this you should first run in command line:

    export PYTHONPATH="/webapps/housing_survey/:$PYTHONPATH"

  And then just run it with python bin/check.py
"""
import django_init

from datatype.saver.models import Datasaver

files = ['homimp', 'mortg', 'newhouse', 'omov', 'owner', 'person', 'ratiov', 'repwgt', 'rmov', 'topical']
years = [2013, 2011]

for year in years:
    for base_name in files:
        print "%d: %s" % (year, base_name)
        try:
            Datasaver(year, base_name).check()
        except IOError:
            print "No file %s.csv for year %d, skipping..." % (base_name, year)
