import csv

class Field:
    types = ['PositiveSmallIntegerField',
             'SmallIntegerFiled',
             'PositiveIntegerField',
             'IntegerField',
             'FloatField'
            ]
    values = [{'min': 0, 'max': 255},
              {'min': -255, 'max': 255},
              {'min': 0, 'max': 10000000},
              {'min': -10000000, 'max': 10000000},
              {'min': -10000000.0, 'max': 10000000.0}
             ]

    type_dictionary = dict(zip(types, values))

    def __cmp__(self, other):
        self_index = self.types.index(self.__class__.__name__)
        other_index = self.types.index(other.__class__.__name__)
        if self_index < other_index:
            return -1
        elif self_index == other_index:
            return 0
        else:
            return 1


class PositiveSmallIntegerField(Field):
    pass

class SmallIntegerFiled(Field):
    pass

class PositiveIntegerField(Field):
    pass

class IntegerField(Field):
    pass

class FloatField(Field):
    pass

class DataTypeFactory:
    def __init__(self, value):
        self.__class__ = PositiveSmallIntegerField

        if value[0] == "'":
            value = value[1:-1]

        if not value:
            return None

        try:
            value = int(value)
        except ValueError:
            value = float(value)
            self.__class__ = FloatField
            return None

        if Field.type_dictionary['PositiveSmallIntegerField']['max'] < value < Field.type_dictionary['PositiveSmallIntegerField']['min']:
            self.__class__ = SmallIntegerFiled

        if Field.type_dictionary['SmallIntegerFiled']['max'] < value < Field.type_dictionary['SmallIntegerFiled']['min']:
            self._class__ = PositiveIntegerField

        if Field.type_dictionary['PositiveIntegerField']['max'] < value < Field.type_dictionary['PositiveIntegerField']['min']:
            self.__class__ = IntegerField

class NewhouseDatatype:
    file_path = 'data/non-git/puf2013/newhouse.csv'

    def read_data_file(self):
        """Opens CSV-file with newhouse data and set the columns datatypes"""
        with open(self.file_path, 'rb') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', skipinitialspace=True)
            headers = reader.next()

            headers_with_types = {}

            # lets assume first, that all datatypes is PositiveSmallIntegerField
            for column in headers:
                headers_with_types[column] = Field.types[0]

            for row in reader:
                for column in headers:
                    new_data_type = DataTypeFactory(row[column])

                    if new_data_type > self.prev_data_type(headers_with_types[column]):
                        headers_with_types[column] = new_data_type


    def prev_data_type(self, name):
        values = [PositiveSmallIntegerField,
                  SmallIntegerFiled,
                  PositiveIntegerField,
                  IntegerField,
                  FloatField
                ]

        options = dict(zip(Field.types, values))

        return options[name]()
