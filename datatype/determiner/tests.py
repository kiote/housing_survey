from django.test import TestCase
from datatype.determiner.models import FileSaver
from datatype.models import Datatype


class FileTestCase(TestCase):
    fixtures = ['datatype.json', 'datatype_year.json']

    def setUp(self):
        self.generated = 'data/sample/puf2013/newhouse.gen'
        self.ad = FileSaver(2013, 'newhouse', True)
        self.ad.generate_columns()

    def test_generate_right_number_of_columns(self):
        """
        Check if we have expected count of lines
        in a file with generated data
        """
        with open(self.generated, 'rb') as generated:
            lines = generated.readlines()
            self.assertEqual(len(lines), 1022)

    def test_saves_columns(self):
        """
        Check if it saves right column count
        """
        obj = Datatype.objects.all()
        self.assertEqual(len(obj), 2152)

    def test_saves_year(self):
        """
        Check if it saves right year
        """
        obj = Datatype.objects.filter(field_name='CONTROL')
        self.assertEqual(obj[0].year_set.all()[0].year, 2013)
