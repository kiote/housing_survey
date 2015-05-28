from django.db import models


class Homimp(models.Model):
    class Meta:
        db_table = 'ahs_homimp'

    control = models.BigIntegerField(db_column='CONTROL', db_index=True, null=True)

    rad = models.PositiveIntegerField(db_column='RAD', null=True)
    rah = models.PositiveSmallIntegerField(db_column='RAH', null=True)
    jrad = models.SmallIntegerField(db_column='JRAD', null=True)
    ras = models.PositiveSmallIntegerField(db_column='RAS', null=True)
    jras = models.SmallIntegerField(db_column='JRAS', null=True)
