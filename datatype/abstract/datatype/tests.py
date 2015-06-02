from django.test import TestCase
from datatype.abstract.datatype.models import AbstractDatatype


class AbstractDatatypeTestCase(TestCase):
    def setUp(self):
        self.generated = 'data/sample/puf2013/newhouse.gen'
        self.ad = AbstractDatatype('newhouse', True)

    def test_generate_right_number_of_columns(self):
        """
        Check if we have expected count of lines
        in a file with generated data
        """
        self.ad.generate_columns()

        with open(self.generated, 'rb') as generated:
            lines = generated.readlines()
            self.assertEqual(len(lines), 758)

    def test_generate_right_column(self):
        """
        Check if we've generated first line with right text
        """
        self.ad.generate_columns()

        with open(self.generated, 'rb') as generated:
            line = generated.readline()
            self.assertEqual(line, "cellar = models.PositiveSmallIntegerField(db_column='CELLAR', null=True)\n")