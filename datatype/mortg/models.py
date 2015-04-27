from datatype.abstract.models import AbstractDatatype
from mortg.models import Mortg


class MortgDatatype(AbstractDatatype):
    def save_csv(self):
        """
        Opens CSV-file with newhouse data and read it to database
        Newhouse model should be already configured
        """
        AbstractDatatype('mortg').fill_model_by_csv_data(Mortg)
