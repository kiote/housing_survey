import os
import csv
import warnings
import sys
import downloader.local

from django.db import connection
from datatype.models import Datatype
from datatype.field.models import default_value_by_name

class Datasaver:
    """
    The base class to save CSV-files to database
    """
    def __init__(self, year=2013, base_name='', sample=False):
        if base_name == '':
            raise 'Base name should be provided'
        self.file_path = downloader.local.data_path(year) + base_name + '.csv'
        self.base_name = base_name
        self.sample = sample
        self.year = year
        if sample:
            self.file_path = 'data/sample/puf2013/' + base_name + '.csv'

    def _which_year(self):
        if self.year == 2013:
            return ['1', '0']
        elif self.year == 2011:
            return ['0', '1']

    def _get_file_and_chunks(self):
        """
        We could have chunked files, so here we trying to get "main" file and chunks
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
        """
        Iterating through data files and return iterator (row)
        """
        files = self._get_file_and_chunks()

        for mfile in files:
            print '---> Processing file %s' % mfile
            with open(mfile, 'rb') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',', skipinitialspace=True)

                for row in reader:
                    yield row

    def _get_row_names(self):
        """
        get rows list from service table, to prepare insert-query
        """
        return [row.field_name for row in Datatype.objects.filter(table_name=self.base_name)]

    def _get_row_types(self):
        return [datatype.field_type for datatype in Datatype.objects.filter(table_name=self.base_name)]

    def _get_values_list(self, row):
        """
        get values list, to prepare insert-query
        first for all values set defaults
        then, if row has explict values,
        change defaults to current values
        """
        types = self._get_row_types()
        row_names = self._get_row_names()

        defaults = [default_value_by_name(dtype) for dtype in types]

        i = 0
        for row_name in row_names:
            row_name = row_name.lower()
            try:
                defaults[i] = row[row_name][1:-1] if row[row_name][0] == "'" else row[row_name]
            except KeyError:
                # means we need default value here
                pass
            i += 1

        return defaults

    def fill_model_by_csv_data(self):
        """
        Opens CSV-file and read it to database
        Use raw-insert to database (not creating any models) to make the insert-precess faster
        1. For given table we need to have fields-list (select from service table)
        2. This list also have fields types
        3. We need a list with defaults for types
        4. for each field we set default value
        5. if value found in a "row", then set this value instead of default
        6. create insert statement
        """
        for row in self._data_iterator():
            rows_list = self._get_row_names() + ['field_in_2013', 'field_in_2011', 'export_year']
            insert = "INSERT IGNORE INTO ahs_{table_name} ({rows}) VALUES ".format(table_name=self.base_name,
                                                                                   rows=', '.join(rows_list))
            row_values = self._get_values_list(row) + self._which_year() + [str(self.year)]
            values = "(%s)" % ', '.join(row_values)
            sys.stdout.write('.')
            with connection.cursor() as c:
                with warnings.catch_warnings():
                    warnings.filterwarnings('error')
                    try:
                        c.execute(insert + values)
                    except Exception as e:
                        print e
                        print "Error with:" + insert + values

    def check(self):
        """
        Count lines in csv-files and in corresponding tables
        """
        print "---> Testing count of %s(%d)" % (self.base_name, self.year)
        count_query = "SELECT COUNT(*) from ahs_{table_name} where export_year={year};".format(table_name=self.base_name,
                                                                                               year=self.year)
        try:
            count_file = int(os.popen("wc -l %s" % self.file_path).read().split(" ")[0]) - 1  # 1 for header
        except ValueError:
            count_file = 0
        with connection.cursor() as c:
            c.execute(count_query)
            count_db = int(c.fetchone()[0])

        if count_db == count_file:
            print "---> OK"
        else:
            print "---> ERROR (%d in db and %d in file)" % (count_db, count_file)

