import csv

import downloader.local
from datatype.field.models import data_type_by_name
from datatype.field.models import DataTypeFactory
from datatype.models import Datatype
from datatype.year.models import Year

class AbstractSaver:

    """
    The base class to generate database based on CSV-files.

    it makes some csv-parsing to determine datatypes for columns,
    and sets database column-type depending on CSV column values

    save determined values to table ahs_service_datatype
    """

    def __init__(self, year=2013, base_name='', sample=False):
        self.file_path = downloader.local.data_path(year) + base_name + '.csv'
        self.columns_generated_file_path = 'data/columns/generated/' + base_name + '.gen'
        self.data_type_path = 'data/columns/' + base_name + '.csv'
        self.base_name, self.sample, self.year = base_name, sample, year
        if sample:
            self.file_path = 'data/sample/puf2013/newhouse.csv'
            self.columns_generated_file_path = 'data/sample/puf2013/newhouse.gen'


class FileSaver(AbstractSaver):

    """
    Write information about fields to *.gen files.

    *.gen files has Python-like syntax and used to create models
    """

    def generate_columns(self):
        """
        Read saved to table data with column names and data types.

        And then generate Python-like statements, based on this data
        """
        table_name = self.base_name
        fields = Datatype.objects.filter(table_name=table_name)
        with open(self.columns_generated_file_path, 'w') as f:
            for field in fields:
                more_params = field.extra_params if field.extra_params == "" else ', ' + field.extra_params
                prepared_string = "%s = models.%s(db_column='%s'%s)\n" % \
                    (field.field_name.lower(), field.field_type, field.field_name, more_params)
                f.write(prepared_string)


class DatabaseSaver(AbstractSaver):

    """
    Saves information about fields to database.

    It gets csv-file and iterates over every line of it to determine
    column datatype. After determine it writes datatype to mysql-table
    named ahs_service_datatype.

    We use this table after to generate data - tables. Also this table could be
    used to determine which feild had been used in which year.
    """

    def write_types(self):
        """Save data with column names and types."""
        rows_to_write = self._generate_types()
        table_name = self.base_name
        for name, value in rows_to_write.iteritems():
            params = 'null=True'
            if value == 'DecimalField':
                params = 'max_digits=20, decimal_places=10, null=True'

            obj, created = Datatype.objects.get_or_create(table_name=table_name,
                                                          field_name=name)
            # create year
            Year.objects.get_or_create(table_field_id=obj.id, year=self.year)

            if created or self._need_to_change_datatype(obj, value):
                obj.field_type = value
                obj.extra_params = params

            obj.save()

    def _generate_types(self):
        """Open original CSV-file with the data and set columns datatypes."""
        headers_with_types = {}

        with open(self.file_path, 'rb') as csvfile:
            reader = csv.DictReader((line.replace('\0', '') for line in csvfile),
                                    delimiter=',', skipinitialspace=True)

            for row in reader:
                for column in row.keys():
                    prev_type = self._determine_prev_type(row, column, headers_with_types)
                    dtf = DataTypeFactory(row[column], prev_type)
                    headers_with_types[column] = dtf.produce()

        return headers_with_types

    @staticmethod
    def _determine_prev_type(row, column, headers_with_types):
            try:
                return str(data_type_by_name(headers_with_types[column]))
            except KeyError:
                return ''

    @staticmethod
    def _need_to_change_datatype(dt_object, dt_new):
        if (dt_object.field_type == '') or (data_type_by_name(dt_object.field_type) < data_type_by_name(dt_new)):
            return True
        else:
            return False
