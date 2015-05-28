from datatype.abstract.models import AbstractDatatype


class RatiovDatatype(AbstractDatatype):
    def save_csv(self):
        """
        Opens CSV-file with newhouse data and read it to database
        Newhouse model should be already configured
        """
        AbstractDatatype('ratiov', self.sample).fill_model_by_csv_data()
