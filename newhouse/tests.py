from django.test import TestCase
from newhouse.models import Newhouse
from decimal import *

import csv

class NewhouseTestCase(TestCase):
    def setUp(self):
        Newhouse.file_path = 'data/sample/puf2013/newhouse.csv'
        Newhouse().read_data_file()
        self.newhouse = Newhouse.objects.get(control='100003130103')

    def test_set_valid_control_value(self):
        """Are we really save the data?"""
        
        self.assertEqual(self.newhouse.control, 100003130103)

    def test_set_valid_field_values(self):
        """
        Are we save the data correctly?
        Assume we have only one entry in the file for testing
        """
        with open(Newhouse.file_path, 'rb') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', skipinitialspace=True)
            for row in reader:
                for rowname in row.keys():
                    attr = getattr(self.newhouse, rowname.lower())
                    value = row[rowname]
                    if row[rowname][0] == "'":
                        value = row[rowname][1:-1]

                    try:
                        attr = int(attr)
                        value = int(value)
                        self.assertEqual(attr, value)
                    except ValueError:
                        attr = Decimal(attr)
                        value = Decimal(value)

                    
