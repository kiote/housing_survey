import urllib2
import os
import errno
import zipfile

"""
Downloads remote CSV-files from census.gov and uncompress them
"""
class Downloader:
    def __init__(self, remote_attrs, local_attrs, full_path):
        self.remote_attrs = remote_attrs
        self.local_attrs = local_attrs
        self.full_path = full_path

    def _get_file_params(self):
        files = []
        files.append({'remote': self.remote_attrs['full_path'],
                      'zip_file': self.local_attrs['path'] + self.remote_attrs['file_name'],
                      'local_path': self.local_attrs['csv_path']})
        return files

    def download(self):
        """Download and unpack zip archive."""
        self._makedirs()

        for file_info in self._get_file_params():
            print '---> Checking %s to exist locally' % file_info['zip_file']
            # do nothing if file exists already
            if os.path.isfile(file_info['zip_file']):
                continue

            self._dowload_remote(file_info)
            self._extract_archive(file_info)

            self._rename_files()
            self._chunk_files()

    @staticmethod
    def _dowload_remote(file_info):
        print '---> Downloading %s' % file_info['remote']
        response = urllib2.urlopen(file_info['remote'])
        result = response.read()
        with open(file_info['zip_file'], 'wb') as result_file:
            result_file.write(result)

    @staticmethod
    def _extract_archive(file_info):
        print '---> Extracting archive %s' % file_info['zip_file']
        with zipfile.ZipFile(file_info['zip_file']) as zf:
            zf.extractall(file_info['local_path'])

    def _makedirs(self):
        """
        Create directories for data files.

        If this directories does not exist yet
        """
        mdir = self.local_attrs['csv_path']

        try:
            os.makedirs(mdir)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(mdir):
                pass
            else:
                raise

    def _file_iterator(self):
        mdir = self.local_attrs['csv_path']
        for mfile in os.listdir(self.full_path + '/' + mdir):
            os.chdir(self.full_path + '/' + mdir)
            yield mfile

    def _rename_files(self):
        """
        AHS give us CSV-files with different name for different years.

        for example newhouse.csv in 2011 named tnewhouse.csv
        So we just make names to follow the same pattern here
        """
        for mfile in self._file_iterator():
                print '---> Renaming %s to %s' % (mfile, mfile.lower())
                os.rename(mfile, mfile.lower())
                if mfile.startswith("t") and mfile != 'topical.csv':
                    print '---> Renaming %s to %s' % (mfile, mfile[1:].lower())
                    os.rename(mfile, mfile[1:].lower())

    def _chunk_files(self):
        """Chunk big files."""
        for mfile in self._file_iterator():
            if os.path.getsize(mfile) > 300000000:
                print '---> Chunking big file %s' % mfile
                os.system('split -l 30000 %s %s-segment-' % (mfile, mfile))
