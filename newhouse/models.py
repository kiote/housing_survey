from django.db import models
import csv

class Newhouse(models.Model):
    control = models.BigIntegerField(db_column = 'CONTROL', unique = True, primary_key = True)
    degree = models.PositiveSmallIntegerField(db_column = 'DEGREE', null = True)
    metro3 = models.PositiveSmallIntegerField(db_column = 'METRO3', null = True)
    region = models.PositiveSmallIntegerField(db_column = 'REGION', null = True)
    smsa = models.CharField(db_column = 'SMSA', max_length=4, null = True)
    lmed = models.PositiveIntegerField(db_column = 'LMED', null = True)
    lmeda = models.PositiveIntegerField(db_column = 'LMEDA', null = True)
    lmedb = models.PositiveIntegerField(db_column = 'LMEDB', null = True)
    fmr = models.PositiveIntegerField(db_column = 'FMR', null = True)
    fmra = models.PositiveIntegerField(db_column = 'FMRA', null = True)
    fmrb = models.PositiveIntegerField(db_column = 'FMRB', null = True)
    l30 = models.PositiveIntegerField(db_column = 'L30', null = True)
    l50 = models.PositiveIntegerField(db_column = 'L50', null = True)
    l80 = models.PositiveIntegerField(db_column = 'L80', null = True)
    l30a = models.PositiveIntegerField(db_column = 'L30A', null = True)
    l50a = models.PositiveIntegerField(db_column = 'L50A', null = True)
    l80a = models.PositiveIntegerField(db_column = 'L80A', null = True)
    l30b = models.PositiveIntegerField(db_column = 'L30B', null = True)
    l50b = models.PositiveIntegerField(db_column = 'L50B', null = True)
    l80b = models.PositiveIntegerField(db_column = 'L80B', null = True)
    ipov = models.PositiveIntegerField(db_column = 'IPOV', null = True)
    histry = models.PositiveSmallIntegerField(db_column = 'HISTRY', null = True)
    cmsa = models.CharField(db_column = 'CMSA', max_length=2, null = True)

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
