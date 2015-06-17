import django_init

from django.db import connection

files = ['ahs_homimp', 'ahs_mortg', 'ahs_newhouse', 'ahs_omov',
         'ahs_owner', 'ahs_person', 'ahs_ratiov', 'ahs_repwgt',
         'ahs_rmov', 'ahs_topical']
truncate = "; ".join(["TRUNCATE `%s`" % f for f in files])

with connection.cursor() as c:
    c.execute(truncate + ';')
