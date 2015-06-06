from django.db import connection

files = ['homimp', 'mortg', 'newhouse', 'omov', 'owner', 'person', 'ratiov', 'repwgt', 'rmov', 'topical']
truncate = "; ".join(["TRUNCATE `ahs_%s`" % f for f in files])

with connection.cursor() as c:
    c.execute(truncate + ';')

from datatype.saver.models import Datasaver

years = [2013, 2011]

for year in years:
    for base_name in files:
        Datasaver(year, base_name).fill_model_by_csv_data()
