from django.db import models


class Rmov(models.Model):
    control = models.BigIntegerField(db_column='CONTROL', unique=True, primary_key=True)

    jdbinreas = models.SmallIntegerField(db_column='JDBINREAS', null=True)
    dbinwhy = models.SmallIntegerField(db_column='DBINWHY', null=True)
    xunit = models.SmallIntegerField(db_column='XUNIT', null=True)
    jxunit = models.SmallIntegerField(db_column='JXUNIT', null=True)
    xcoop = models.SmallIntegerField(db_column='XCOOP', null=True)
    jxper = models.SmallIntegerField(db_column='JXPER', null=True)
    smsa = models.PositiveIntegerField(db_column='SMSA', null=True)
    dbinreas = models.SmallIntegerField(db_column='DBINREAS', null=True)
    dbinwher = models.SmallIntegerField(db_column='DBINWHER', null=True)
    dbinvol = models.SmallIntegerField(db_column='DBINVOL', null=True)
    xcond = models.SmallIntegerField(db_column='XCOND', null=True)
    jxten = models.SmallIntegerField(db_column='JXTEN', null=True)
    jdbinwhy = models.SmallIntegerField(db_column='JDBINWHY', null=True)
    mvg = models.PositiveSmallIntegerField(db_column='MVG', null=True)
    jdbinwher = models.SmallIntegerField(db_column='JDBINWHER', null=True)
    xcost = models.SmallIntegerField(db_column='XCOST', null=True)
    jxhead = models.SmallIntegerField(db_column='JXHEAD', null=True)
    jovgrp = models.SmallIntegerField(db_column='JOVGRP', null=True)
    xrel = models.SmallIntegerField(db_column='XREL', null=True)
    xhead = models.SmallIntegerField(db_column='XHEAD', null=True)
    xper = models.SmallIntegerField(db_column='XPER', null=True)
    xten = models.SmallIntegerField(db_column='XTEN', null=True)
    jdbinvol = models.SmallIntegerField(db_column='JDBINVOL', null=True)
