from django.db import models


class Homimp(models.Model):
    class Meta:
        db_table = 'ahs_homimp'
        index_together = [
            ['control', 'export_year'],
            ['field_in_2013', 'field_in_2011']
        ]

    control = models.BigIntegerField(db_column='CONTROL', null=True)
    jrad = models.SmallIntegerField(db_column='JRAD', null=True)
    jras = models.SmallIntegerField(db_column='JRAS', null=True)
    rad = models.IntegerField(db_column='RAD', null=True)
    rah = models.SmallIntegerField(db_column='RAH', null=True)
    rahk = models.SmallIntegerField(db_column='RAHK', null=True)
    ras = models.PositiveSmallIntegerField(db_column='RAS', null=True)

    field_in_2013 = models.BooleanField(default=False)
    field_in_2011 = models.BooleanField(default=False)

    export_year = models.PositiveSmallIntegerField(null=True, db_index=True)
