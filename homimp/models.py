from django.db import models


class Homimp(models.Model):
    class Meta:
        db_table = 'ahs_homimp'
        index_together = [
            ['control', 'export_year']
        ]

    control = models.BigIntegerField(db_column='CONTROL', null=False, db_index=True)

    jrad = models.SmallIntegerField(db_column='JRAD', null=True)
    jras = models.SmallIntegerField(db_column='JRAS', null=True)
    rad = models.IntegerField(db_column='RAD', null=True)
    rah = models.SmallIntegerField(db_column='RAH', null=True)
    rahk = models.SmallIntegerField(db_column='RAHK', null=True)
    ras = models.PositiveSmallIntegerField(db_column='RAS', null=True)

    export_year = models.PositiveSmallIntegerField(null=True, db_index=True)
