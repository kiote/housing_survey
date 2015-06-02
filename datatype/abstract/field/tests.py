from django.test import TestCase

from datatype.abstract.field.types import DataTypeFactory


class DataTypeFactoryTest(TestCase):
    def test_return_valid_class(self):
        """Do we set datatype"""
        cases = [{'expect': 'PositiveSmallIntegerField', 'value': '0'},
                 {'expect': 'SmallIntegerField',         'value': '-2'},
                 {'expect': 'PositiveIntegerField',      'value': '1000000'},
                 {'expect': 'IntegerField',              'value': '-1000000'},
                 {'expect': 'DecimalField',              'value': '1.1'}
                 ]
        for case in cases:
            factory = DataTypeFactory(case['value']).produce()
            self.assertEqual(factory, case['expect'])

    def test_return_valid_class_for_prev(self):
        """Do we set datatype if there is previous datatype"""
        cases = [{'expect': 'SmallIntegerField', 'prev': 'PositiveSmallIntegerField', 'value': '-1'},
                 {'expect': 'IntegerField', 'prev': 'PositiveIntegerField', 'value': '-1'},
                 ]

        for case in cases:
            factory = DataTypeFactory(case['value'], case['prev']).produce()
            self.assertEqual(factory, case['expect'])
