import csv
from field.models import *

class NewhouseDatatype:
    # read from
    file_path = 'data/non-git/puf2013/newhouse.csv'

    # generate columns to
    columns_generated_file_path = 'data/columns/generated/newhouse.gen'
    
    # write to
    data_type_path = 'data/columns/newhouse.csv'

    def read_data_file(self):
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

    def write_types(self):
        rows_to_write = self.read_data_file()
        with open(self.data_type_path, 'wb') as typefile:
            writer = csv.writer(typefile, delimiter=',')
            for k, v in rows_to_write.iteritems():
                params = 'null= True'
                if v == 'DecimalField':
                    params = 'max_digits=20, decimal_places=10, null=True'

                writer.writerow([k, v, params])

    def generate_columns(self):
        """
        Read prepared CSV-file with column names and data types and generate
        Python-like sataments, based on this data
        """
        with open(self.data_type_path, 'rb') as csvcolumns:
            reader = csv.reader(csvcolumns, delimiter=',')
            f = open(self.columns_generated_file_path, 'w')
            for row in reader:
                more_params = row[2] if row[2] == "" else ', ' + row[2]

                prepared_string = "%s=models.%s(db_column='%s'%s)\n" % \
                    (row[0].lower(), row[1], row[0], more_params)
                f.write(prepared_string)
            f.close()
