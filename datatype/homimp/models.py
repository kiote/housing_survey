from datatype.abstract.models import AbstractDatatype
from homimp.models import Homimp


class HomimpDatatype(AbstractDatatype):
    def save_csv(self):
        """
        Opens CSV-file with newhouse data and read it to database
        Newhouse model should be already configured
        """
        AbstractDatatype('homimp').fill_model_by_csv_data(Homimp)