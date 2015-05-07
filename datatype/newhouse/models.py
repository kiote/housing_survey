from datatype.abstract.models import AbstractDatatype
from newhouse.models import Newhouse
from datatype.codebook.models import Codebook
import csv


class NewhouseDatatype(AbstractDatatype):
    def save_csv(self):
        """
        Opens CSV-file with newhouse data and read it to database
        Newhouse model should be already configured
        """
        AbstractDatatype('newhouse', self.sample).fill_model_by_csv_data(Newhouse)


class Documenter:
    file_path = 'data/columns/newhouse.csv'

    def __init__(self):
        c = Codebook()
        with open('data/columns/documentor/newhouse.csv', 'wb') as csvfile:
            docwriter = csv.writer(csvfile)

            with open(self.file_path, 'rb') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)

                for row in reader:
                    docwriter.writerow([row[0], c.get_info(row[0])])
