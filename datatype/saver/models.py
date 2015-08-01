"""Main module to save data to database."""
import os
import csv
import warnings
import sys
import downloader.local

from django.db import connection
from datatype.models import Datatype, ParticularTable
from datatype.field.models import default_value_by_name


class Settings:

    """Store general settings that is changing with year file."""

    def __init__(self, year=2013, base_name='', sample=False):
        if base_name == '':
            raise 'Base name should be provided'

        # Short name, based on table name
        # for newhouse.csv it's newhouse
        self.base_name = base_name

        # Full path to csv file
        self.file_path = downloader.local.data_path(year) + base_name + '.csv'

        # Boolean flag, are we in a testing mode?
        self.sample = sample

        if sample:
            self.file_path = 'data/sample/puf2013/' + base_name + '.csv'

        # Year to work with
        self.year = year


class Cell:

    """Represent one particular cell of the data."""

    def __init__(self, cell):
        self.cell = cell

    def _unquoted_value(self):
        self.cell = self.cell[1:-1] if self.cell[0] == "'" else self.cell

    def _numeric_value(self):
        self.cell = '-9' if self.cell == 'B' else self.cell

    def clear(self):
        self._unquoted_value()
        self._numeric_value()
        return self.cell


class DataFile:

    """Read data from particular file."""

    def __init__(self, settings):
        self.settings = settings

    def _get_file_and_chunks(self):
        """
        Work with chunked files.

        If files are too big we have them chunked.
        Here we trying to get chunks. If there are no chunks, we get main file.
        """
        chunks = []

        for i in range(20):
            chunk = self.settings.file_path + '-segment-a' + chr(ord('a') + i)
            if os.path.exists(chunk):
                chunks.append(chunk)
            else:
                break

        if not len(chunks):
            chunks = [self.settings.file_path]

        return chunks

    def rows(self):
        """Iterating through data files and return iterator (row)."""
        files = self._get_file_and_chunks()

        for mfile in files:
            print '---> Processing file %s' % mfile
            with open(mfile, 'rb') as csvfile:
                reader = csv.DictReader((line.replace('\0', '') for line in csvfile),
                                        delimiter=',',
                                        skipinitialspace=True)

                for row in reader:
                    yield row


class Row:

    """Represent one row of a data."""

    def __init__(self, row, settings):
        self.row = row
        self.settings = settings

    def get_assigned(self):
        """
        For given row return {name: value} dictionary.

        This dictionary initialized either
        with default values for given datatype
        or with values readed from file.
        """
        table = ParticularTable(self.settings.base_name)
        types = table.get_row_types()
        row_names = table.get_row_names()

        defaults = [default_value_by_name(dtype) for dtype in types]

        for i, row_name in enumerate(row_names):
            try:
                defaults[i] = Cell(self.row[row_name]).clear()
            except KeyError:
                # maybe we have wrong-cased keys?
                try:
                    defaults[i] = Cell(self.row[row_name.lower()]).clear()
                except KeyError:
                    # no chance, use default
                    pass

        key_values = dict(zip(row_names, defaults))
        # sorten list of fields for debug
        # key_values = {'CONTROL': key_values['CONTROL']}
        # print key_values
        try:
            if key_values['JEQUIP'] == '':
                key_values['JEQUIP'] = '-9'
        except KeyError:
            pass
        return key_values


class InsertMaker:

    """Prepare INSERT statement for MySQL."""

    def __init__(self, dict, settings):
        # Dictionary contains { row_name: row_value }
        self.dict = dict

        self.settings = settings

    def prepare(self):
        rows_list = ["`%s`" % key for key in self.dict.keys()] + ['`export_year`']
        insert = "INSERT INTO ahs_{table_name} ({rows}) VALUES "
        insert = insert.format(table_name=self.settings.base_name,
                               rows=', '.join(rows_list))
        row_values = self.dict.values() + [str(self.settings.year)]
        values = "(%s)" % ', '.join(row_values)

        # debug result dict to be inserted
        # print dict(zip(rows_list, row_values))['NEWC']

        return insert + values


class Checker:

    """Check if we have the same about of data in files and in tables"""

    def __init__(self, settings):
        self.settings = settings

    def check(self):
        """Count lines in csv-files and in corresponding tables."""
        print "---> Testing count of %s(%d)" % (self.settings.base_name, self.settings.year)
        count_query = ("SELECT COUNT(*) from ahs_{table_name} "
                       "where export_year={year};")
        count_query = count_query.format(table_name=self.settings.base_name,
                                         year=self.settings.year)
        try:
            count_file = os.popen("wc -l %s" % self.settings.file_path).read()
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


class Datasaver:

    """The base class to save CSV-files to database."""

    def __init__(self, settings):
        self.settings = settings
        self.file = DataFile(settings)

    def fill_model_by_csv_data(self):
        """
        Open CSV-file and read it to database.

        Use raw-insert to database (not creating any models)
        to make the insert-precess faster.
        """
        for row in self.file.rows():
            # Make insert data ready to be placed into the query
            key_values = Row(row, self.settings).get_assigned()

            # Prepare insert with data
            insert = InsertMaker(key_values, self.settings).prepare()

            with connection.cursor() as c:
                with warnings.catch_warnings():
                    warnings.filterwarnings('error')
                    try:
                        c.execute(insert)
                        sys.stdout.write('.')
                    except Exception as e:
                        print e
                        print key_values
