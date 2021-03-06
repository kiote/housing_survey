from django.db import models


class Omov(models.Model):
    class Meta:
        db_table = 'ahs_omov'
        index_together = [
            ['control', 'export_year']
        ]

    control = models.BigIntegerField(db_column='CONTROL', null=False, db_index=True)

    dbgrpcnt = models.PositiveSmallIntegerField(db_column='DBGRPCNT', null=True)
    dboutlen = models.SmallIntegerField(db_column='DBOUTLEN', null=True)
    dboutreas = models.SmallIntegerField(db_column='DBOUTREAS', null=True)
    dboutvol = models.SmallIntegerField(db_column='DBOUTVOL', null=True)
    dboutwher = models.SmallIntegerField(db_column='DBOUTWHER', null=True)
    dboutwhy = models.SmallIntegerField(db_column='DBOUTWHY', null=True)
    dbugroup = models.PositiveSmallIntegerField(db_column='DBUGROUP', null=True)

    export_year = models.PositiveSmallIntegerField(null=True, db_index=True)
