from django.db import models


class Owner(models.Model):
    class Meta:
        db_table = 'ahs_owner'

    control = models.BigIntegerField(db_column='CONTROL', unique=True, primary_key=True)

    jwnher = models.SmallIntegerField(db_column='JWNHER', null=True)
    ownhere = models.SmallIntegerField(db_column='OWNHERE', null=True)
    add_year = models.PositiveSmallIntegerField(db_column='ADD_YEAR', default=2013, db_index=True)
