"""Loads data from CSV-files to database."""
import initializers.framework
import initializers.data as di

from datatype.saver.models import Datasaver

for year in di.YEARS:
    for base_name in di.FILES:
        try:
            Datasaver(year, base_name).fill_model_by_csv_data()
        except IOError:
            print 'File with name %s not found for year %d' % (base_name, year)
            pass
