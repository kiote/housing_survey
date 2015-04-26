from datatype.abstract.models import AbstractDatatype
from ratiov.models import Ratiov


class RatiovDatatype(AbstractDatatype):
    def __init__(self, file_path='data/non-git/puf2013/ratiov.csv',
                 columns_generated_file_path='data/columns/generated/ratiov.gen',
                 data_type_path='data/columns/ratiov.csv'):
        AbstractDatatype.__init__(self, file_path, columns_generated_file_path, data_type_path)

    def save_csv(self):
        """
        Opens CSV-file with newhouse data and read it to database
        Newhouse model should be already configured
        """
        AbstractDatatype(self.file_path).fill_model_by_csv_data(Ratiov)
