from decimal import *

def data_type_by_name(name):
    klass = globals()[name]
    return klass


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


class PositiveIntegerField(Field):
    name = 'PositiveIntegerField'
    val_min = 0
    val_max = 10000000

    def next(self):
        if not(self.in_range()):
            return IntegerField(self.value).next()

        return PositiveIntegerField(self.value)


class IntegerField(Field):
    name = 'IntegerField'

    def next(self):
        return IntegerField(self.value)


class DecimalField(Field):
    name = 'DecimalField'

    def next(self):
        return DecimalField(self.value)


class DataTypeFactory:
    def __init__(self, value, prev_type=''):
        self.value = value
        self.prev_type = prev_type
        self._clear_value()

    def produce(self):
        if not self.prev_type:
            self.prev_type = 'PositiveSmallIntegerField' if self.value >= 0 else 'SmallIntegerField'

        data_type = data_type_by_name(self.prev_type)
        return data_type(self.value).next().__class__.name

    def _clear_value(self):
        if self.value[0] == "'":
            self.value = self.value[1:-1]

        try:
            self.value = int(self.value)
        except ValueError:
            self.value = Decimal(self.value)
