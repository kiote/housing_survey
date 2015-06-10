from django.test import TestCase
from datatype.determiner.models import AbstractDatatype
from datatype.models import Datatype


class AbstractDatatypeTestCase(TestCase):
    def setUp(self):
        self.generated = 'data/sample/puf2013/newhouse.gen'
        self.ad = AbstractDatatype(2013, 'newhouse', True)
        self.ad.generate_columns()

    def test_generate_right_number_of_columns(self):
        """
        Check if we have expected count of lines
        in a file with generated data
        """
        with open(self.generated, 'rb') as generated:
            lines = generated.readlines()
            self.assertEqual(len(lines), 758)

    def test_generate_right_column(self):
        """
        Check if we've generated first line with right text
        """
        with open(self.generated, 'rb') as generated:
            line = generated.readline()
            self.assertEqual(line, "cellar = models.PositiveSmallIntegerField(db_column='CELLAR', null=True)\n")

    def test_saves_columns(self):
        """
        Check if it saves right column count
        """
        obj = Datatype.objects.all()
        self.assertEqual(len(obj), 758)

    def test_saves_year(self):
        """
        Check if it saves right year
        """
        obj = Datatype.objects.filter(field_name='CONTROL')
        self.assertEqual(obj[0].export_year_2013, True)
