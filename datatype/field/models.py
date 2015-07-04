"""
This module provides main work on defining field's datatype.

To define datatype it does:
1) assume by default datatype = PositiveSmallInteger
    ("smallest" of possible datatypes);
2) if we have some value, which is beyond the limits of current datatype,
    then we make current datatype
    to equals "next" datatype, the order for next is:
    PositiveSmallInteger -> SmallInteger -> PositiveInteger
        -> Integer -> Decimal

Main class here is DataTypeFactory which trying to "produce" right type
    based on the value.
Value is just one of the column values.
"""
from decimal import *


def data_type_by_name(name):
    while name.find('.') != -1:
        name = name[name.find('.')+1:]
    klass = globals()[name]
    return klass

def default_value_by_name(name):
    klass = globals()[name]
    return str(klass.default())


class Field:
    val_min = 0
    val_max = 0
    name = ''

    def __init__(self, value):
        self.value = value

    def _is_positive(self):
        return self.name[0:8] == 'Positive'

    def next(self):
        raise NotImplementedError("Must be implemented!")

    def in_range(self):
        return self.val_min <= self.value <= self.val_max

    def is_decimal(self):
        return not(Decimal(self.value) % 1 == 0)


class PositiveSmallIntegerField(Field):
    name = 'PositiveSmallIntegerField'
    val_min = 0
    val_max = 255

    def next(self):
        if self.is_decimal():
            return DecimalField(self.value)

        if not(self.in_range()):
            return SmallIntegerField(self.value).next()

        return PositiveSmallIntegerField(self.value)

    @staticmethod
    def default():
        return 0


class SmallIntegerField(Field):
    name = 'SmallIntegerField'
    val_min = -255
    val_max = 255

    def next(self):
        if self.is_decimal():
            return DecimalField(self.value)

        if not(self.in_range()):
            return PositiveIntegerField(self.value).next()

        return SmallIntegerField(self.value)

    @staticmethod
    def default():
        return -255


class PositiveIntegerField(Field):
    name = 'PositiveIntegerField'
    val_min = 0
    val_max = 10000000

    def next(self):
        if not(self.in_range()):
            return IntegerField(self.value).next()

        return PositiveIntegerField(self.value)

    @staticmethod
    def default():
        return 0


class IntegerField(Field):
    val_min = -2000000000
    val_max = 2000000000
    name = 'IntegerField'

    def next(self):
        if not(self.in_range()):
            return BigIntegerField(self.value).next()

        return IntegerField(self.value)

    @staticmethod
    def default():
        return -255

class BigIntegerField(Field):
    val_min = -900000000000000000
    val_max = 9000000000000000000
    name = 'BigIntegerField'

    def next(self):
        return BigIntegerField(self.value)

    @staticmethod
    def default():
        return -255

class DecimalField(Field):
    name = 'DecimalField'

    def next(self):
        return DecimalField(self.value)

    @staticmethod
    def default():
        return -255


class DataTypeFactory:
    def __init__(self, value, prev_type=''):
        self.value = self._clear_value(value)
        self.prev_type = prev_type

    def produce(self):
        if not self.prev_type:
            self.prev_type = 'PositiveSmallIntegerField' \
                if self.value >= 0 else 'SmallIntegerField'

        data_type = data_type_by_name(self.prev_type)
        return data_type(self.value).next().name

    def _clear_value(self, value):
        """Remove quotes and make int/decimal value"""
        if value[0] == "'":
            value = value[1:-1]

        try:
            value = int(value)
        except ValueError:
            try:
                value = Decimal(value)
            except InvalidOperation:
                value = self._char_to_int(value)
        return value

    def _char_to_int(self, value):
        """
        If value contains on of the "B" or "" (blank) then it set to -6 or -9

        Here we assume that whatever strange we would have,
        it will be turned to -9
        """
        if value == 'B' or value == 'b':
            value = -6
        else:
            value = -9
