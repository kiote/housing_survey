from django.db import models


class Omov(models.Model):
    class Meta:
        db_table = 'ahs_omov'

    control = models.BigIntegerField(db_column='CONTROL', null=True, db_index=True)

    smsa = models.PositiveIntegerField(db_column='SMSA', null=True, db_index=True)
    dboutreas = models.SmallIntegerField(db_column='DBOUTREAS', null=True)
    dboutlen = models.SmallIntegerField(db_column='DBOUTLEN', null=True)
    dbgrpcnt = models.PositiveSmallIntegerField(db_column='DBGRPCNT', null=True)
    dboutvol = models.SmallIntegerField(db_column='DBOUTVOL', null=True)
    dbugroup = models.PositiveSmallIntegerField(db_column='DBUGROUP', null=True)
    dboutwhy = models.SmallIntegerField(db_column='DBOUTWHY', null=True)
    dboutwher = models.SmallIntegerField(db_column='DBOUTWHER', null=True)
