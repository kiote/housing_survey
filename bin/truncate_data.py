import django_init

from django.db import connection

files = ['homimp', 'mortg', 'newhouse', 'omov', 'owner', 'person', 'ratiov', 'repwgt', 'rmov', 'topical']
truncate = "; ".join(["TRUNCATE `ahs_%s`" % f for f in files])

with connection.cursor() as c:
    c.execute(truncate + ';')
