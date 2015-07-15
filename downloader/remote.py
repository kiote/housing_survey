"""constants to locate remote files"""
import urllib2

AHS_ADDRESS = 'http://www2.census.gov/'

def year_attributes(year):
    file_name = 'National PUF v1.1 CSV.zip'
    if year == 2011:
        file_name = 'National and Metropolitan PUF v1.4 CSV.zip'
    elif year == 2007 or year == 2005 or year == 2003:
        file_name = 'National PUF V1.1 CSV.zip'

    quoted_file_name = urllib2.quote('AHS ' + str(year) + ' ' + file_name)
    remote_path = 'programs-surveys/ahs/' + str(year) + '/'
    concatenated = AHS_ADDRESS + remote_path + quoted_file_name
    return {'full_path': concatenated, 'file_name': quoted_file_name}
