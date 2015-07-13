"""
constants to locate local files
"""
import os

FULL_PATH = os.path.abspath(os.path.dirname(__name__))

PREFIX = 'data/non-git/puf'
SUFFIX = 'csv_files/'

def year_attributes(year):
    return {'path': PREFIX + str(year) + '/',
            'csv_path': PREFIX + str(year) + '/' + SUFFIX}

def data_path(year):
    return "%s%d/%s" % (PREFIX, year, SUFFIX)
