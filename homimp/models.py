from django.db import models


class Homimp(models.Model):
    class Meta:
        db_table = 'ahs_homimp'

    control = models.BigIntegerField(db_column='CONTROL', unique=True, primary_key=True)

    rad = models.IntegerField(db_column='RAD', null=True)
    smsa = models.PositiveIntegerField(db_column='SMSA', null=True, db_index=True)
    rah = models.PositiveSmallIntegerField(db_column='RAH', null=True)
    jrad = models.SmallIntegerField(db_column='JRAD', null=True)
    ras = models.PositiveSmallIntegerField(db_column='RAS', null=True)
    jras = models.SmallIntegerField(db_column='JRAS', null=True)
