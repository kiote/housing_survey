from datatype.abstract.models import AbstractDatatype
from ratiov.models import Ratiov


class RatiovDatatype(AbstractDatatype):
    def save_csv(self):
        """
        Opens CSV-file with newhouse data and read it to database
        Newhouse model should be already configured
        """
        AbstractDatatype('ratiov').fill_model_by_csv_data()
