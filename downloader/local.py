"""
constants to locate local files
"""
import os

FULL_PATH = os.path.abspath(os.path.dirname(__name__))

PREFIX = 'data/non-git/puf'
SUFFIX = 'csv_files/'

Y2013_PATH = PREFIX + '2013/'
Y2013_CSV_PATH = Y2013_PATH + SUFFIX

Y2011_PATH = PREFIX + '2011/'
Y2011_CSV_PATH = Y2011_PATH + SUFFIX

def data_path(year):
    return "%s%d/%s" % (PREFIX, year, SUFFIX)
