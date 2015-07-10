import initializers.framework

from django.db import connection

truncate = "; ".join(["drop database housing_survey; create database housing_survey;"])

with connection.cursor() as c:
    c.execute(truncate + ';')
