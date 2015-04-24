from decimal import *


def data_type_by_name(name):
    klass = globals()[name]
    return klass


class Field(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return type(self).__name__

    def _is_positive(self):
        return str(self)[0:8] == 'Positive'

    def next(self):
        raise NotImplementedError("Must be implemented!")


class PositiveSmallIntegerField(Field):
    val_range = range(0, 255)

    def next(self):
        if not(self.value in self.val_range):
            return SmallIntegerField(self.value).next()
        return PositiveSmallIntegerField(self.value)


class SmallIntegerField(Field):
    val_range = range(-255, 255)

    def next(self):
        if not(self.value in self.val_range):
            return PositiveIntegerField(self.value).next()
        return SmallIntegerField(self.value)


class PositiveIntegerField(Field):
    val_range = range(0, 10000000)

    def next(self):
        if not(self.value in self.val_range):
            return IntegerField(self.value).next()
        return PositiveIntegerField(self.value)


class IntegerField(Field):
    val_range = range(-10000000, 10000000)

    def next(self):
        if not(self.value in self.val_range):
            return DecimalField(self.value).next()
        return IntegerField(self.value)


class DecimalField(Field):
    def next(self):
        return DecimalField(self.value)


class DataTypeFactory:
    def __init__(self, value, prev_type=''):
        self.value = value
        self.prev_type = prev_type
        self._clear_value()

        if not self.prev_type:
            self.prev_type = 'PositiveSmallIntegerField' if self.value > 0 else 'SmallIntegerField'

        self.__class__ = data_type_by_name(self.prev_type)(self.value).next().__class__

    def _clear_value(self):
        if self.value[0] == "'":
            self.value = self.value[1:-1]

        try:
            self.value = int(self.value)
        except ValueError:
            self.value = Decimal(self.value)
