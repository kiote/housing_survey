"""
constants to locate remote files
"""
import urllib2

AHS_ADDRESS = 'http://www2.census.gov/'

Y2013 = {'file_name': urllib2.quote('AHS 2013 National PUF v1.1 CSV.zip'),
         'path': 'programs-surveys/ahs/2013/'}

Y2013_FULL_PATH = AHS_ADDRESS + Y2013['path'] + Y2013['file_name']

Y2011 = {'file_name': urllib2.quote('AHS 2011 National and Metropolitan PUF v1.4 CSV.zip'),
         'path': 'programs-surveys/ahs/2011/'}

Y2011_FULL_PATH = AHS_ADDRESS + Y2011['path'] + Y2011['file_name']