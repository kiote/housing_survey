from django.test import TestCase
from newhouse.models import Newhouse

import csv

class NewhouseTestCase(TestCase):
    def setUp(self):
        Newhouse.file_path = 'data/sample/puf2013/newhouse.csv'

    def test_set_valid_control_value(self):
        """Are we really save the data?"""
        Newhouse().read_data_file()
        data = Newhouse.objects.get(control='100003130103')
        self.assertNotEqual(data, None)

    def test_set_valid_field_values(self):
        """
        Are we save the data correctly?
        Assume we have only one entry in the file for testing
        """
        Newhouse().read_data_file()
        row_names = Newhouse().get_row_names()
        newhouse = Newhouse.objects.get(control='100003130103')

        with open(Newhouse.file_path, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
            next(reader, None)  # skip the headers
            for row in reader:
                for i, rowname in enumerate(row_names):
                    attr = getattr(newhouse, rowname)
                    value = row[i+1][1:-1] if row[i+1][0] == "'" else row[i+1]
                    self.assertEqual(str(attr), str(value))
