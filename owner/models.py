from django.db import models


class Owner(models.Model):
    class Meta:
        db_table = 'ahs_owner'

    control = models.BigIntegerField(db_column='CONTROL', unique=True, primary_key=True)

    jwnher = models.SmallIntegerField(db_column='JWNHER', null=True)
    ownhere = models.SmallIntegerField(db_column='OWNHERE', null=True)
    export_year_2013 = models.BooleanField(default=False)
    export_year_2011 = models.BooleanField(default=False)
