from django.db import models


class Ratiov(models.Model):
    class Meta:
        db_table = 'ahs_ratiov'
        index_together = [
            ['control', 'export_year']
        ]

    control = models.BigIntegerField(db_column='CONTROL', null=False, db_index=True)
    rcarp = models.SmallIntegerField(db_column='RCARP', null=True)
    rclot = models.SmallIntegerField(db_column='RCLOT', null=True)
    rcost = models.SmallIntegerField(db_column='RCOST', null=True)
    rgroc = models.SmallIntegerField(db_column='RGROC', null=True)
    rkidc = models.SmallIntegerField(db_column='RKIDC', null=True)
    rmedi = models.SmallIntegerField(db_column='RMEDI', null=True)
    rothe = models.SmallIntegerField(db_column='ROTHE', null=True)
    rutil = models.SmallIntegerField(db_column='RUTIL', null=True)

    export_year = models.PositiveSmallIntegerField(null=True, db_index=True)
