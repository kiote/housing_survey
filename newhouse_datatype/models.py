import csv
from decimal import *

class Field:
    types = ['PositiveSmallIntegerField',
             'SmallIntegerField',
             'PositiveIntegerField',
             'IntegerField',
             'DecimalField'
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

    def _is_positive(self, string):
        return string[0:8] == 'Positive'    


class PositiveSmallIntegerField(Field):
    pass

class SmallIntegerField(Field):
    pass

class PositiveIntegerField(Field):
    pass

class IntegerField(Field):
    pass

class DecimalField(Field):
    pass

class DataTypeFactory:
    def __init__(self, value, prev_type = 'PositiveSmallIntegerField'):
        self.__class__ = NewhouseDatatype().data_type_by_name(prev_type).__class__

        if value[0] == "'":
            value = value[1:-1]

        if not value:
            return None

        try:
            value = int(value)
        except ValueError:
            value = Decimal(value)
            self.__class__ = DecimalField
            return None

        if abs(value) > Field.type_dictionary['PositiveSmallIntegerField']['max']: # not small
            if value < 0: # not positive
                self.__class__ = IntegerField
            elif self._is_positive(prev_type): # not small, positive and was positive before
                self.__class__ = PositiveIntegerField
            else: # not small, positive and wasn't positive before
                self.__class__ = IntegerField
        else: # small
            if (value < 0) and (prev_type == 'PositiveSmallIntegerField'): # not positive and was small before
                self.__class__ = SmallIntegerField
            elif (value < 0): # not positive and wasn't small before
                self.__class__ = IntegerField

        # if we still think it's positive when it's negative
        if (value < 0) and self._is_positive(prev_type) and self._is_positive(self.__class__.__name__):
            new_type = self.__class__.__name__[8:]
            self.__class__ = NewhouseDatatype().data_type_by_name(new_type)


class NewhouseDatatype:
    # read from
    file_path = 'data/non-git/puf2013/newhouse.csv'
    
    # write to
    data_type_path = 'data/columns/newhouse.csv'

    def read_data_file(self):
        """Opens CSV-file with newhouse data and set the columns datatypes"""
        headers_with_types = {}

        with open(self.file_path, 'rb') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', skipinitialspace=True)
            
            for row in reader:
                for column in row.keys():
                    headers_with_types.setdefault(column, 'PositiveSmallIntegerField')
                    prev_type = self.data_type_by_name(headers_with_types[column])
                    new_data_type = DataTypeFactory(row[column], str(prev_type.__class__.__name__))
                    
                    # if new datatype is bigger than previous
                    # for example, Integer > SmallInteger
                    # Then we set column type to new data type
                    if new_data_type > prev_type:
                        headers_with_types[column] = new_data_type.__class__.__name__
                    
        return headers_with_types

    def write_types(self):
        rows_to_write = self.read_data_file()
        with open(self.data_type_path, 'wb') as typefile:
            writer = csv.writer(typefile, delimiter = ',')
            for k, v in rows_to_write.iteritems():
                params = 'null = True'
                if v == 'DecimalField':
                    params = 'max_digits = 20, decimal_places = 10, null = True'

                writer.writerow([k, v, params])


    def data_type_by_name(self, name):
        values = [PositiveSmallIntegerField,
                  SmallIntegerField,
                  PositiveIntegerField,
                  IntegerField,
                  DecimalField
                 ]

        options = dict(zip(Field.types, values))

        return options[name]()
