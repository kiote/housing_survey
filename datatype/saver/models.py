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

    def fill_model_by_csv_data(self):
        """
        Opens CSV-file and read it to database
        Use raw-insert to database (not creating any models) to make the insert-precess faster
        """
        if self.sample:
            self.file_path = 'data/sample/puf2013/' + self.base_name + '.csv'

        with open(self.file_path, 'rb') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', skipinitialspace=True)
            printed = False

            for row in reader:
                rows_with_year = ', '.join(row.keys()) + ', export_year_2013, export_year_2011'
                insert = "INSERT IGNORE INTO ahs_{table_name} ({rows}) VALUES ".format(table_name=self.base_name,
                                                                                       rows=rows_with_year)
                row_values = ', '.join([v[1:-1] if v[0] == "'" else v for v in row.values()])
                row_values += ", %d, %d" % self._which_year()
                values = "(%s)" % row_values
                if not printed:
                    print "Trying: " + insert + values
                    printed = True
                with connection.cursor() as c:
                    with warnings.catch_warnings():
                        warnings.filterwarnings('error')
                        # try:
                        c.execute(insert + values)
                        # except:
                        #     print "Error with:" + insert + values
