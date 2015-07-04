from django.db import models


class Ratiov(models.Model):
    class Meta:
        db_table = 'ahs_ratiov'
        index_together = [
            ['control', 'export_year'],
            ['field_in_2013', 'field_in_2011']
        ]
        unique_together = ('control', 'export_year')

    control = models.BigIntegerField(db_column='CONTROL', null=True)
    rcarp = models.SmallIntegerField(db_column='RCARP', null=True)
    rclot = models.SmallIntegerField(db_column='RCLOT', null=True)
    rcost = models.SmallIntegerField(db_column='RCOST', null=True)
    rgroc = models.SmallIntegerField(db_column='RGROC', null=True)
    rkidc = models.SmallIntegerField(db_column='RKIDC', null=True)
    rmedi = models.SmallIntegerField(db_column='RMEDI', null=True)
    rothe = models.SmallIntegerField(db_column='ROTHE', null=True)
    rutil = models.SmallIntegerField(db_column='RUTIL', null=True)

    field_in_2013 = models.BooleanField(default=False)
    field_in_2011 = models.BooleanField(default=False)

    export_year = models.PositiveSmallIntegerField(null=True, db_index=True)
