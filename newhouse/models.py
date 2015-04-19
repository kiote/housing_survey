from django.db import models
import csv

class Newhouse(models.Model):
    control = models.BigIntegerField(db_column = 'CONTROL', unique = True, primary_key = True)
    # Average heating/cooling degree days
    degree = models.PositiveSmallIntegerField(db_column = 'DEGREE', null = True)
    # Central city / suburban status
    metro3 = models.PositiveSmallIntegerField(db_column = 'METRO3', null = True)

    file_path = 'data/non-git/puf2013/newhouse.csv'

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
