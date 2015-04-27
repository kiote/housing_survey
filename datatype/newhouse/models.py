from datatype.abstract.models import AbstractDatatype
from newhouse.models import Newhouse


class NewhouseDatatype(AbstractDatatype):
    def save_csv(self):
        """
        Opens CSV-file with newhouse data and read it to database
        Newhouse model should be already configured
        """
        AbstractDatatype('newhouse').fill_model_by_csv_data(Newhouse)
