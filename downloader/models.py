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
              'local_path': local.Y2013_CSV_PATH},
             {'remote': remote.Y2011_FULL_PATH,
              'zip_file': local.Y2011_PATH + remote.Y2011['file_name'],
              'local_path': local.Y2011_CSV_PATH}]

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

        self._rename_files()

    @staticmethod
    def _makedirs():
        """
        Creates directories for data files, if this directories did not exist yet
        """
        for mdir in [local.Y2013_CSV_PATH, local.Y2011_CSV_PATH]:
            try:
                os.makedirs(mdir)
            except OSError as exc:
                if exc.errno == errno.EEXIST and os.path.isdir(mdir):
                    pass
                else:
                    raise

    @staticmethod
    def _rename_files():
        """
        AHS give us CSV-files with different name for different years,
        for example newhouse.csv in 2011 named tnewhouse.csv

        So we just make names to follow the same pattern here
        """
        for mdir in [local.Y2013_CSV_PATH, local.Y2011_CSV_PATH]:
            # lowercase all file names inside this dir and removes "t" in the beginning of the name
            for mfile in os.listdir(local.FULL_PATH + '/' + mdir):
                os.chdir(local.FULL_PATH + '/' + mdir)
                os.rename(mfile, mfile.lower())
                if mfile.startswith("t"):
                    os.rename(mfile, mfile[1:])
