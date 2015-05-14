from datatype.abstract.models import AbstractDatatype
from person.models import Person


class PersonDatatype(AbstractDatatype):
    def save_csv(self):
        """
        Opens CSV-file with newhouse data and read it to database
        Newhouse model should be already configured
        """
        AbstractDatatype('person').fill_model_by_csv_data()
