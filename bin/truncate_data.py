import django_init

from django.db import connection

truncate = "; ".join(["drop database housing_survey; create database housing_survey;"])

with connection.cursor() as c:
    c.execute(truncate + ';')
