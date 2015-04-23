from django.test import TestCase
from newhouse_datatype.models import Field
from newhouse_datatype.models import DataTypeFactory
from newhouse_datatype.models import NewhouseDatatype

class DataTypeFactoryTest(TestCase):
    def test_return_valid_class(self):
        """Do we set datatype"""
        cases = [{'PositiveSmallIntegerField': '0'},
                 {'SmallIntegerField': '-2'},
                 {'PositiveIntegerField': '1000000'},
                 {'IntegerField': '-1000000'},
                 {'DecimalField': '1.1'}
                ]
        for case in cases:
            factory = DataTypeFactory(case.values()[0])
            self.assertEqual(factory.__class__.__name__, case.keys()[0])

    def test_return_valid_class_for_prev(self):
        """Do we set datatype if there is previous datatype"""
        cases = [{'expect': 'SmallIntegerField', 'prev': 'PositiveSmallIntegerField', 'value': '-1'},
                 {'expect': 'IntegerField', 'prev': 'SmallIntegerField', 'value': '-1000000'},
                ]

        for case in cases:
            factory = DataTypeFactory(case['value'], case['prev'])
            self.assertEqual(factory.__class__.__name__, case['expect'])

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

    def test_data_type_class_by_name(self):
        self.assertEquals(NewhouseDatatype().data_type_class_by_name('PositiveSmallIntegerField').__class__\
                          .__name__, 'PositiveSmallIntegerField'
                         )
