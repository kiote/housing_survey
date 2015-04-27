from datatype.abstract.models import AbstractDatatype
from rmov.models import Rmov


class RmovDatatype(AbstractDatatype):
    def save_csv(self):
        """
        Opens CSV-file with newhouse data and read it to database
        Newhouse model should be already configured
        """
        AbstractDatatype('rmov').fill_model_by_csv_data(Rmov)
