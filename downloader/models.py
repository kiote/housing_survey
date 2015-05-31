import urllib2
import os, errno
import zipfile
import remote
import local

"""
Downloads remote CSV-files from census.gov and uncompress them
"""
class Downloader:
    files = [{'remote': remote.Y2013_FULL_PATH,
              'zip_file': local.Y2013_PATH + remote.Y2013['file_name'],
              'local_path': local.Y2013_NATIONAL_PATH},
             {'remote': remote.Y2011_FULL_PATH,
              'zip_file': local.Y2011_PATH + remote.Y2011['file_name'],
              'local_path': local.Y2011_NATIONAL_AND_METRO_PATH}]

    def download(self):
        self._makedirs()

        for file_info in self.files:
            if not os.path.isfile(file_info['zip_file']):
                print '---> Downloading %s' % file_info['remote']
                response = urllib2.urlopen(file_info['remote'])
                result = response.read()
                with open(file_info['zip_file'], 'wb') as result_file:
                    result_file.write(result)
            print '---> Extracting archive %s' % file_info['zip_file']
            with zipfile.ZipFile(file_info['zip_file']) as zf:
                zf.extractall(file_info['local_path'])

    @staticmethod
    def _makedirs():
        for mdir in [local.Y2013_NATIONAL_PATH, local.Y2011_NATIONAL_AND_METRO_PATH]:
            try:
                os.makedirs(mdir)
            except OSError as exc:
                if exc.errno == errno.EEXIST and os.path.isdir(mdir):
                    pass
                else:
                    raise