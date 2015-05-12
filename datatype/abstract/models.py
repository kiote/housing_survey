import csv
import warnings
from field.models import *


class AbstractDatatype:
    def __init__(self, base_name='', sample=False):
        self.file_path = 'data/non-git/puf2013/metro/' + base_name + '.csv'
        self.columns_generated_file_path = 'data/columns/generated/' + base_name + '.gen'
        self.data_type_path = 'data/columns/' + base_name + '.csv'
        self.base_name = base_name
        self.sample = sample
        if sample:
            self.file_path = 'data/sample/puf2013/' + base_name + '.csv'
            self.columns_generated_file_path = 'data/sample/puf2013/' + base_name + '.gen'
            self.data_type_path = 'data/sample/puf2013/' + base_name + 'with_types.csv'

    def _generate_types(self):
        """Opens CSV-file with newhouse data and set the columns datatypes"""
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
        """Prepare CSV-file with column names and types"""
        rows_to_write = self._generate_types()
        with open(self.data_type_path, 'wb') as typefile:
            writer = csv.writer(typefile, delimiter=',')
            for k, v in rows_to_write.iteritems():
                params = 'null=True'
                if v == 'DecimalField':
                    params = 'max_digits=20, decimal_places=10, null=True'

                writer.writerow([k, v, params])

    def generate_columns(self):
        """
        Read prepared CSV-file with column names and data types and then generate
        Python-like statements, based on this data
        """
        self._write_types()
        with open(self.data_type_path, 'rb') as csvcolumns:
            reader = csv.reader(csvcolumns, delimiter=',')
            f = open(self.columns_generated_file_path, 'w')
            for row in reader:
                more_params = row[2] if row[2] == "" else ', ' + row[2]

                prepared_string = "%s = models.%s(db_column='%s'%s)\n" % \
                    (row[0].lower(), row[1], row[0], more_params)
                f.write(prepared_string)
            f.close()

    def fill_model_by_csv_data(self, model):
        """
        Opens CSV-file with newhouse data and read it to database
        Newhouse model should be already configured
        """
        for mtype in ['metro', 'national']:
            self.file_path = 'data/non-git/puf2013/' + mtype + '/' + self.base_name + '.csv'
            if self.sample:
                self.file_path = 'data/sample/puf2013/' + self.base_name + '.csv'
            with open(self.file_path, 'rb') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',', skipinitialspace=True)

                for row in reader:
                    obj = model(control=int(row['CONTROL'][1:-1]))
                    for column in row.keys():
                        value = row[column]

                        if value[0] == "'":
                            value = value[1:-1]

                        setattr(obj, column.lower(), value)

                    with warnings.catch_warnings():
                        warnings.filterwarnings('error')
                        obj.save()
