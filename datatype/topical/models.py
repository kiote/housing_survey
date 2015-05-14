from datatype.abstract.models import AbstractDatatype
from topical.models import Topical


class TopicalDatatype(AbstractDatatype):
    def save_csv(self):
        """
        Opens CSV-file with newhouse data and read it to database
        Newhouse model should be already configured
        """
        AbstractDatatype('topical').fill_model_by_csv_data()
