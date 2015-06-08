from django.db import models


class Ratiov(models.Model):
    class Meta:
        db_table = 'ahs_ratiov'

    control = models.BigIntegerField(db_column='CONTROL', unique=True, primary_key=True)
    rgroc = models.SmallIntegerField(db_column='RGROC', null=True)
    rmedi = models.SmallIntegerField(db_column='RMEDI', null=True)
    rcarp = models.SmallIntegerField(db_column='RCARP', null=True)
    rutil = models.SmallIntegerField(db_column='RUTIL', null=True)
    rcost = models.SmallIntegerField(db_column='RCOST', null=True)
    rclot = models.SmallIntegerField(db_column='RCLOT', null=True)
    rkidc = models.SmallIntegerField(db_column='RKIDC', null=True)
    rothe = models.SmallIntegerField(db_column='ROTHE', null=True)
    export_year_2013 = models.BooleanField(default=False)
    export_year_2011 = models.BooleanField(default=False)
