from datatype.abstract.models import AbstractDatatype
from repwgt.models import Repwgt


class RepwgtDatatype(AbstractDatatype):
    def save_csv(self):
        """
        Opens CSV-file with newhouse data and read it to database
        Newhouse model should be already configured
        """
        AbstractDatatype('repwgt').fill_model_by_csv_data(Repwgt)
