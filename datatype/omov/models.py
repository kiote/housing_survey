from datatype.abstract.models import AbstractDatatype
from omov.models import Omov


class OmovDatatype(AbstractDatatype):
    def save_csv(self):
        """
        Opens CSV-file with newhouse data and read it to database
        Newhouse model should be already configured
        """
        AbstractDatatype('omov').fill_model_by_csv_data(Omov)
