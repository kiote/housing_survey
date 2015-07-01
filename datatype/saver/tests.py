from decimal import *
import csv

from django.test import TestCase
from datatype.saver.models import Datasaver
from newhouse.models import Newhouse


class AbstractDatasaverTestCase(TestCase):
    fixtures = ['datatype']

    def setUp(self):
        Datasaver(2013, 'newhouse', True).fill_model_by_csv_data()
        self.newhouse = Newhouse.objects.get(control='100003130103')

    def test_set_valid_control_value(self):
        """Are we really save the data?"""

        self.assertEqual(self.newhouse.control, 100003130103)

    def test_set_valid_field_values(self):
        """
        Are we save the data correctly?
        Assume we have only one entry in the file for testing
        """
        with open(Datasaver(2013, 'newhouse', True).file_path, 'rb') as csvfile:
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
                        #self.assertEqual(attr, value)
