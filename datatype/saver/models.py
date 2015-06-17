import os
import csv
import warnings
import downloader.local

from django.db import connection


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
            return 1, 0
        elif self.year == 2011:
            return 0, 1

    def _get_file_and_chunks(self):
        """
        We could have chunked files, so here we trying to get "main" file and chunks
        """
        chunks = [self.file_path]

        for i in range(20):
            chunk = self.file_path + '-segment-a' + chr(ord('a') + i)
            if os.path.exists(chunk):
                chunks.append(chunk)
            else:
                break

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

    def fill_model_by_csv_data(self):
        """
        Opens CSV-file and read it to database
        Use raw-insert to database (not creating any models) to make the insert-precess faster
        """
        printed = False
        count = 0

        for row in self._data_iterator():
            count += 1
            # print "inserting %d row" % count
            rows_with_year = ', '.join(row.keys()) + ', field_in_2013, field_in_2011, export_year'
            insert = "INSERT IGNORE INTO ahs_{table_name} ({rows}) VALUES ".format(table_name=self.base_name,
                                                                                   rows=rows_with_year)
            row_values = ', '.join([v[1:-1] if v[0] == "'" else v for v in row.values()])
            values_tuple = self._which_year() + (self.year,)
            row_values += ", %d, %d, %d" % values_tuple
            values = "(%s)" % row_values
            if not printed:
                print "Sample: " + insert + values
                printed = True
            with connection.cursor() as c:
                with warnings.catch_warnings():
                    warnings.filterwarnings('error')
                    try:
                        c.execute(insert + values)
                    except:
                        pass
                        #print "Error with:" + insert + values

    def check(self):
        """
        Count lines in csv-files and in corresponding tables
        """
        print "---> Testing %s" % self.base_name
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

