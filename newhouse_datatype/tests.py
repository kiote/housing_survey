from django.test import TestCase
from newhouse_datatype.models import Field
from newhouse_datatype.models import DataTypeFactory
from newhouse_datatype.models import NewhouseDatatype

class DataTypeFactoryTest(TestCase):
    def test_return_valid_class(self):
        """Do we set datatype"""
        cases = [{'PositiveSmallIntegerField': '0'},
                 {'SmallIntegerFiled': '-2'},
                 {'PositiveIntegerField': '1000000'},
                 {'IntegerField': '-1000000'},
                 {'FloatField': '1.1'}
                ]
        for case in cases:
            factory = DataTypeFactory(case.values()[0])
            self.assertEqual(factory.__class__.__name__, case.keys()[0])

class FieldTestCase(TestCase):
    """Does it compares"""
    def test_cmp_gt(self):
        a = DataTypeFactory('0')
        b = DataTypeFactory('1000')
        self.assertTrue(b > a)

    def test_cmp_lt(self):
        a = DataTypeFactory('1110')
        b = DataTypeFactory('100')
        self.assertTrue(a > b)

    def test_cmp_eq(self):
        a = DataTypeFactory('0')
        b = DataTypeFactory('100')
        self.assertTrue(b == a)

class NewhouseDatatypeTest(TestCase):
    def setUp(self):
        NewhouseDatatype.file_path = 'data/sample/puf2013/newhouse.csv'

    def test_data_type_by_name(self):
        self.assertEquals(NewhouseDatatype().data_type_by_name('PositiveSmallIntegerField').__class__\
                          .__name__, 'PositiveSmallIntegerField'
                         )
