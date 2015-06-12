import csv

import downloader.local
from datatype.field.models import data_type_by_name
from datatype.field.models import DataTypeFactory
from datatype.models import Datatype


class AbstractDatatype:
    """
    The base class to generate database based on CSV-files

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

    def _generate_types(self):
        """Opens original CSV-file with the data and sets columns datatypes"""
        headers_with_types = {}

        with open(self.file_path, 'rb') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',', skipinitialspace=True)
            
            for row in reader:
                for column in row.keys():
                    try:
                        prev_type = str(data_type_by_name(headers_with_types[column]))
                    except KeyError:
                        prev_type = ''

                    headers_with_types[column] = DataTypeFactory(row[column], prev_type).produce()
                    
        return headers_with_types

    def _write_types(self):
        """save data with column names and types"""
        rows_to_write = self._generate_types()
        table_name = self.base_name
        for name, value in rows_to_write.iteritems():
            params = 'null=True'
            if value == 'DecimalField':
                params = 'max_digits=20, decimal_places=10, null=True'

            obj, created = Datatype.objects.get_or_create(table_name=table_name,
                                                          field_name=name)
            setattr(obj, "export_year_%d" % self.year, 1)
            obj.extra_params = params
            if self._need_to_change_datatype(obj, value):
                obj.field_type = value

            obj.save()

    @staticmethod
    def _need_to_change_datatype(dt_object, dt_new):
        if (dt_object.field_type == '') or (data_type_by_name(dt_object.field_type) < data_type_by_name(dt_new)):
            return True
        else:
            return False

    def generate_columns(self):
        """
        Read saved to table data with column names and data types and then generate
        Python-like statements, based on this data
        """
        self._write_types()
        table_name = self.base_name
        fields = Datatype.objects.filter(table_name=table_name)
        with open(self.columns_generated_file_path, 'w') as f:
            for field in fields:
                more_params = field.extra_params if field.extra_params == "" else ', ' + field.extra_params
                prepared_string = "%s = models.%s(db_column='%s'%s)\n" % \
                    (field.field_name.lower(), field.field_type, field.field_name, more_params)
                f.write(prepared_string)

