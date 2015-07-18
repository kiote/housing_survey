"""constants to locate remote files"""
import urllib2

AHS_ADDRESS = 'http://www2.census.gov/'

def year_attributes(year):
    if year == 2011:
        file_name = 'National and Metropolitan PUF v1.4 CSV.zip'
    elif year in [2007, 2005, 2003, 1999]:
        file_name = 'National PUF V1.1 CSV.zip'
    else #the only difference is downcased "v" here
        file_name = 'National PUF v1.1 CSV.zip'

    quoted_file_name = urllib2.quote('AHS ' + str(year) + ' ' + file_name)
    remote_path = 'programs-surveys/ahs/' + str(year) + '/'
    full_remote_path = AHS_ADDRESS + remote_path + quoted_file_name
    return {'full_path': full_remote_path, 'file_name': quoted_file_name}
