"""Loads data from CSV-files to database."""
import django_init
import data_init as di

from datatype.saver.models import Datasaver

for year in di.YEARS:
    for base_name in di.FILES:
        try:
            Datasaver(year, base_name).fill_model_by_csv_data()
        except IOError:
            print 'File with name %s not found for year %d' % (base_name, year)
            pass
