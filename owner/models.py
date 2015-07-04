from django.db import models


class Owner(models.Model):
    class Meta:
        db_table = 'ahs_owner'
        index_together = [
            ['control', 'export_year'],
            ['field_in_2013', 'field_in_2011']
        ]

    control = models.BigIntegerField(db_column='CONTROL', null=True)
    jwnher = models.SmallIntegerField(db_column='JWNHER', null=True)
    ownhere = models.SmallIntegerField(db_column='OWNHERE', null=True)

    field_in_2013 = models.BooleanField(default=False)
    field_in_2011 = models.BooleanField(default=False)

    export_year = models.PositiveSmallIntegerField(null=True, db_index=True)
