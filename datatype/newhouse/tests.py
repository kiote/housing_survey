from django.test import TestCase

from datatype.newhouse.models import NewhouseDatatype


class NewhouseDatatypeTest(TestCase):
    def setUp(self):
        NewhouseDatatype.file_path = 'data/sample/puf2013/newhouse.csv'

    def test_data_type_by_name(self):
        name = NewhouseDatatype().data_type_by_name('PositiveSmallIntegerField')
        self.assertEquals(str(name), 'PositiveSmallIntegerField')
