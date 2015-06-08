import django_init

from django.db import connection
from datatype.saver.models import Datasaver

files = ['homimp', 'mortg', 'newhouse', 'omov', 'owner', 'person', 'ratiov', 'repwgt', 'rmov', 'topical']

years = [2013, 2011]

for year in years:
    for base_name in files:
        Datasaver(year, base_name).fill_model_by_csv_data()
