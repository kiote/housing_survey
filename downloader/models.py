import urllib2
import os, errno
import zipfile


class Downloader:
    address = 'http://www2.census.gov/'
    ahs_2013_name = 'AHS_2013_Metropolitan_PUF_v1.0_CSV.zip'
    ahs_2013_path = 'data/non-git/puf2013/'
    files = {'file': {'remote': address + 'programs-surveys/ahs/2013/' + ahs_2013_name,
                      'zip_file': ahs_2013_path + ahs_2013_name,
                      'local_path': ahs_2013_path}}

    def __init__(self):
        self.files = self.files

    def download(self):
        try:
            os.makedirs(self.ahs_2013_path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(self.ahs_2013_path):
                pass
            else:
                raise
        for file_info in self.files.itervalues():
            if not os.path.isfile(file_info['zip_file']):
                response = urllib2.urlopen(file_info['remote'])
                result = response.read()
                with open(file_info['zip_file'], 'wb') as result_file:
                    result_file.write(result)
            with zipfile.ZipFile(file_info['zip_file']) as zf:
                zf.extractall(file_info['local_path'])