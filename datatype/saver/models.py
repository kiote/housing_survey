"""Main module to save data to database."""
import os
import csv
import warnings
import sys
import downloader.local

from django.db import connection
from datatype.models import Datatype
from datatype.field.models import default_value_by_name


class Datasaver:

    """The base class to save CSV-files to database."""

    def __init__(self, year=2013, base_name='', sample=False):
        """Some pre-initialization."""
        if base_name == '':
            raise 'Base name should be provided'
        self.file_path = downloader.local.data_path(year) + base_name + '.csv'
        self.base_name = base_name
        self.sample = sample
        self.year = year
        if sample:
            self.file_path = 'data/sample/puf2013/' + base_name + '.csv'

    def _get_file_and_chunks(self):
        """
        Work with chunked files.

        If files are too big we have them chunked.
        Here we trying to get chunks. If there are no chunks, we get main file.
        """
        chunks = []

        for i in range(20):
            chunk = self.file_path + '-segment-a' + chr(ord('a') + i)
            if os.path.exists(chunk):
                chunks.append(chunk)
            else:
                break

        if not len(chunks):
            chunks = [self.file_path]

        return chunks

    def _data_iterator(self):
        """Iterating through data files and return iterator (row)."""
        files = self._get_file_and_chunks()

        for mfile in files:
            print '---> Processing file %s' % mfile
            with open(mfile, 'rb') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',',
                                        skipinitialspace=True)

                for row in reader:
                    yield row

    def _get_row_names(self):
        """Get rows list from service table, to prepare insert-query."""
        return [row.field_name for row in
                Datatype.objects.filter(table_name=self.base_name)]

    def _get_row_types(self):
        return [datatype.field_type for datatype in
                Datatype.objects.filter(table_name=self.base_name)]

    def _unquoted_value(self, value):
        return value[1:-1] if value[0] == "'" else value

    def _get_assigned(self, row):
        """
        For given row readed from file gives dictionary.

        This dictionary contains row values and default values.
        Return dictionary initialized either
        with default values for given datatype
        or with values readed from file.
        """
        types = self._get_row_types()
        row_names = self._get_row_names()

        defaults = [default_value_by_name(dtype) for dtype in types]

        for i, row_name in enumerate(row_names):
            try:
                defaults[i] = self._unquoted_value(row[row_name])
            except KeyError:
                # maybe we have wrong-cased keys?
                try:
                    defaults[i] = self._unquoted_value(row[row_name.lower()])
                except KeyError:
                    # no chance, use default
                    pass

        key_values = dict(zip(row_names, defaults))
        # sorten list of fields for debug
        # key_values = {'CONTROL': key_values['CONTROL']}
        # print key_values
        return key_values

    def fill_model_by_csv_data(self):
        """
        Open CSV-file and read it to database.

        Use raw-insert to database (not creating any models)
        to make the insert-precess faster.
        """
        for row in self._data_iterator():
            key_values = self._get_assigned(row)
            rows_list = ["`%s`" % key for key in key_values.keys()] + ['`export_year`']
            insert = "INSERT IGNORE INTO ahs_{table_name} ({rows}) VALUES "
            insert = insert.format(table_name=self.base_name,
                                   rows=', '.join(rows_list))
            rows_value = key_values.values() + [str(self.year)]
            values = "(%s)" % ', '.join(rows_value)

            # debug result dict to be inserted
            # print dict(zip(rows_list, rows_value))['NEWC']
            with connection.cursor() as c:
                with warnings.catch_warnings():
                    warnings.filterwarnings('error')
                    try:
                        c.execute(insert + values)
                        sys.stdout.write('.')
                    except Exception as e:
                        print e
                        # print "Error with:" + insert + values

    def check(self):
        """Count lines in csv-files and in corresponding tables."""
        print "---> Testing count of %s(%d)" % (self.base_name, self.year)
        count_query = ("SELECT COUNT(*) from ahs_{table_name} "
                       "where export_year={year};")
        count_query = count_query.format(table_name=self.base_name,
                                         year=self.year)
        try:
            count_file = os.popen("wc -l %s" % self.file_path).read()
            count_file = int(count_file.split(" ")[0]) - 1  # 1 for header
        except ValueError:
            count_file = 0
        with connection.cursor() as c:
            c.execute(count_query)
            count_db = int(c.fetchone()[0])

        if count_db == count_file:
            print "---> OK"
        else:
            print "---> ERROR (%d in db and %d in file)" % (count_db,
                                                            count_file)
