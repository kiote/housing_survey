from django.db import models
from newhouse.models import Newhouse


class Ratiov(models.Model):
    control = models.OneToOneField(Newhouse, primary_key=True)

    rgroc = models.SmallIntegerField(db_column='RGROC', null=True)
    rmedi = models.SmallIntegerField(db_column='RMEDI', null=True)
    smsa = models.PositiveIntegerField(db_column='SMSA', null=True)
    rcarp = models.SmallIntegerField(db_column='RCARP', null=True)
    rutil = models.SmallIntegerField(db_column='RUTIL', null=True)
    rcost = models.SmallIntegerField(db_column='RCOST', null=True)
    rclot = models.SmallIntegerField(db_column='RCLOT', null=True)
    rkidc = models.SmallIntegerField(db_column='RKIDC', null=True)
    rothe = models.SmallIntegerField(db_column='ROTHE', null=True)
