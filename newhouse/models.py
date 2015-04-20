from django.db import models
import csv

class Newhouse(models.Model):
    control = models.BigIntegerField(db_column = 'CONTROL', unique = True, primary_key = True)
    # Average heating/cooling degree days
    degree = models.PositiveSmallIntegerField(db_column = 'DEGREE', null = True)
    # Central city / suburban status
    metro3 = models.PositiveSmallIntegerField(db_column = 'METRO3', null = True)

    file_path = 'data/non-git/puf2013/newhouse.csv'
    columns_file_path = 'data/columns/newhouse-smalldata.csv'
    columns_generated_file_path = 'data/columns/generated/newhouse.gen'

    def readfile(self):
        with open(self.file_path, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
            next(reader, None)  # skip the headers
            for row in reader:
                nh = Newhouse(control = int(row[0][1:-1]))
                nh.degree = row[1][1:-1]
                nh.metro3 = row[2][1:-1]
                nh.save()

                print row[2]

    def generate_columns(self):
        with open(self.columns_file_path, 'rb') as csvcolumns:
            reader = csv.reader(csvcolumns, delimiter = ',')
            f = open(self.columns_generated_file_path, 'w')
            for row in reader:
                more_params = row[2]
                if more_params != "":
                    more_params = ', ' + more_params

                prepared_string = "%s = models.%s(db_column = '%s'%s)\n" % \
                    (row[0].lower(), row[1], row[0], more_params)
                f.write(prepared_string)
            f.close()
