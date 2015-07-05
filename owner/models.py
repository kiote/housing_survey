from django.db import models


class Owner(models.Model):
    class Meta:
        db_table = 'ahs_owner'
        index_together = [
            ['control', 'export_year']
        ]

    control = models.BigIntegerField(db_column='CONTROL', null=True)
    jwnher = models.SmallIntegerField(db_column='JWNHER', null=True)
    ownhere = models.SmallIntegerField(db_column='OWNHERE', null=True)

    export_year = models.PositiveSmallIntegerField(null=True, db_index=True)
