from django.db import models
import csv

class Newhouse(models.Model):
    control = models.BigIntegerField(db_column = 'CONTROL', unique = True, primary_key = True)

    degree = models.PositiveSmallIntegerField(db_column = 'DEGREE', null = True)
    metro3 = models.PositiveSmallIntegerField(db_column = 'METRO3', null = True)
    region = models.PositiveSmallIntegerField(db_column = 'REGION', null = True)
    smsa = models.PositiveSmallIntegerField(db_column = 'SMSA', null = True)
    lmed = models.PositiveIntegerField(db_column = 'LMED', null = True)
    lmeda = models.PositiveIntegerField(db_column = 'LMEDA', null = True)
    lmedb = models.PositiveIntegerField(db_column = 'LMEDB', null = True)
    fmr = models.PositiveIntegerField(db_column = 'FMR', null = True)
    fmra = models.PositiveIntegerField(db_column = 'FMRA', null = True)
    fmrb = models.PositiveIntegerField(db_column = 'FMRB', null = True)
    l30 = models.PositiveIntegerField(db_column = 'L30', null = True)
    l50 = models.PositiveIntegerField(db_column = 'L50', null = True)
    l80 = models.PositiveIntegerField(db_column = 'L80', null = True)
    l30a = models.PositiveIntegerField(db_column = 'L30A', null = True)
    l50a = models.PositiveIntegerField(db_column = 'L50A', null = True)
    l80a = models.PositiveIntegerField(db_column = 'L80A', null = True)
    l30b = models.PositiveIntegerField(db_column = 'L30B', null = True)
    l50b = models.PositiveIntegerField(db_column = 'L50B', null = True)
    l80b = models.PositiveIntegerField(db_column = 'L80B', null = True)
    ipov = models.PositiveIntegerField(db_column = 'IPOV', null = True)
    histry = models.PositiveSmallIntegerField(db_column = 'HISTRY', null = True)
    cmsa = models.CharField(db_column = 'CMSA', max_length=2, null = True)
    division = models.CharField(db_column = 'DIVISION', max_length=2, null = True)
    dish = models.CharField(db_column = 'DISH', max_length=2, null = True)
    wash = models.CharField(db_column = 'WASH', max_length=2, null = True)
    dry = models.CharField(db_column = 'DRY', max_length=2, null = True)
    buyg = models.CharField(db_column = 'BUYG', max_length=2, null = True)
    buye = models.CharField(db_column = 'BUYE', max_length=2, null = True)
    nunit2 = models.CharField(db_column = 'NUNIT2', max_length=2, null = True)
    burner = models.CharField(db_column = 'BURNER', max_length=2, null = True)
    amtg = models.PositiveIntegerField(db_column = 'AMTG', null = True)
    gaspip = models.CharField(db_column = 'GASPIP', max_length=2, null = True)
    usegas = models.CharField(db_column = 'USEGAS', max_length=2, null = True)
    amte = models.PositiveIntegerField(db_column = 'AMTE', null = True)
    uselect = models.CharField(db_column = 'USELECT', max_length=2, null = True)
    hfuel = models.CharField(db_column = 'HFUEL', max_length=2, null = True)
    wfuel = models.CharField(db_column = 'WFUEL', max_length=2, null = True)
    cook = models.CharField(db_column = 'COOK', max_length=2, null = True)
    oven = models.CharField(db_column = 'OVEN', max_length=2, null = True)
    refr = models.CharField(db_column = 'REFR', max_length=2, null = True)
    baths = models.CharField(db_column = 'BATHS', max_length=2, null = True)
    bedrms = models.CharField(db_column = 'BEDRMS', max_length=2, null = True)
    dens = models.CharField(db_column = 'DENS', max_length=2, null = True)
    dining = models.CharField(db_column = 'DINING', max_length=2, null = True)
    famrm = models.CharField(db_column = 'FAMRM', max_length=2, null = True)
    halfb = models.CharField(db_column = 'HALFB', max_length=2, null = True)
    kitch = models.CharField(db_column = 'KITCH', max_length=2, null = True)
    living = models.CharField(db_column = 'LIVING', max_length=2, null = True)
    othfn = models.CharField(db_column = 'OTHFN', max_length=2, null = True)
    recrm = models.CharField(db_column = 'RECRM', max_length=2, null = True)

    file_path = 'data/non-git/puf2013/newhouse.csv'
    columns_file_path = 'data/columns/newhouse-smalldata.csv'
    columns_generated_file_path = 'data/columns/generated/newhouse.gen'

    def read_data_file(self):
        """Opens CSV-file with newhouse data and read it to database"""
        with open(self.file_path, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
            next(reader, None)  # skip the headers
            for row in reader:
                nh = Newhouse(control = int(row[0][1:-1]))
                for i, name in enumerate(self.get_row_names()):
                    value = row[i+1][1:-1] if row[i+1][0] == "'" else row[i+1]
                    setattr(nh, name, value)
                nh.save()

    def get_row_names(self):
        """
        Returns the list of names for rows in newhouse,
        this list are used to save the data into the database,
        so we don't need to have each row name in saving-to-database code
        """
        with open(self.columns_file_path, 'rb') as csvcolumns:
            reader = csv.reader(csvcolumns, delimiter = ',')
            names = [row[0].lower() for row in reader]
        return names

    def generate_columns(self):
        """
        Read prepared CSV-file with column names and data types and generate
        Python-like sataments, based on this data
        """
        with open(self.columns_file_path, 'rb') as csvcolumns:
            reader = csv.reader(csvcolumns, delimiter = ',')
            f = open(self.columns_generated_file_path, 'w')
            for row in reader:
                more_params = row[2] if more_params == "" else ', ' + more_params

                prepared_string = "%s = models.%s(db_column = '%s'%s)\n" % \
                    (row[0].lower(), row[1], row[0], more_params)
                f.write(prepared_string)
            f.close()
