import urllib2
import os, errno
import zipfile


class Downloader:
    address = 'http://www2.census.gov/'
    ahs_2013_path = 'data/non-git/puf2013/'

    ahs_2013_metro_name = 'AHS_2013_Metropolitan_PUF_v1.0_CSV.zip'
    ahs_2013_metro_path = ahs_2013_path + 'metro/'
    ahs_2013_national_name = 'AHS 2013 National PUF v1.1 CSV.zip'
    ahs_2013_national_path = ahs_2013_path + 'national/'

    files = [{'remote': address + 'programs-surveys/ahs/2013/' + ahs_2013_metro_name,
              'zip_file': ahs_2013_path + ahs_2013_metro_name,
              'local_path': ahs_2013_metro_path},
             {'remote': address + 'programs-surveys/ahs/2013/' + ahs_2013_national_name,
              'zip_file': ahs_2013_path + ahs_2013_national_name,
              'local_path': ahs_2013_national_path}]

    def download(self):
        self.makedirs()

        for file_info in self.files:
            if not os.path.isfile(file_info['zip_file']):
                response = urllib2.urlopen(file_info['remote'])
                result = response.read()
                with open(file_info['zip_file'], 'wb') as result_file:
                    result_file.write(result)
            with zipfile.ZipFile(file_info['zip_file']) as zf:
                zf.extractall(file_info['local_path'])

    def makedirs(self):
        for mdir in [self.ahs_2013_metro_path, self.ahs_2013_national_path]:
            try:
                os.makedirs(mdir)
            except OSError as exc:
                if exc.errno == errno.EEXIST and os.path.isdir(mdir):
                    pass
                else:
                    raise