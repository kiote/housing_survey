from django.db import models


class Rmov(models.Model):
    class Meta:
        db_table = 'ahs_rmov'
        index_together = [
            ['control', 'export_year'],
            ['field_in_2013', 'field_in_2011']
        ]

    control = models.BigIntegerField(db_column='CONTROL', unique=True, primary_key=True)

    dbinreas = models.SmallIntegerField(db_column='DBINREAS', null=True)
    dbinvol = models.SmallIntegerField(db_column='DBINVOL', null=True)
    dbinwher = models.SmallIntegerField(db_column='DBINWHER', null=True)
    dbinwhy = models.SmallIntegerField(db_column='DBINWHY', null=True)
    jdbinreas = models.SmallIntegerField(db_column='JDBINREAS', null=True)
    jdbinvol = models.SmallIntegerField(db_column='JDBINVOL', null=True)
    jdbinwher = models.SmallIntegerField(db_column='JDBINWHER', null=True)
    jdbinwhy = models.SmallIntegerField(db_column='JDBINWHY', null=True)
    jovgrp = models.SmallIntegerField(db_column='JOVGRP', null=True)
    jxhead = models.SmallIntegerField(db_column='JXHEAD', null=True)
    jxper = models.SmallIntegerField(db_column='JXPER', null=True)
    jxten = models.SmallIntegerField(db_column='JXTEN', null=True)
    jxunit = models.SmallIntegerField(db_column='JXUNIT', null=True)
    mvg = models.PositiveSmallIntegerField(db_column='MVG', null=True)
    xcond = models.SmallIntegerField(db_column='XCOND', null=True)
    xcoop = models.SmallIntegerField(db_column='XCOOP', null=True)
    xcost = models.SmallIntegerField(db_column='XCOST', null=True)
    xhead = models.SmallIntegerField(db_column='XHEAD', null=True)
    xinus = models.SmallIntegerField(db_column='XINUS', null=True)
    xper = models.SmallIntegerField(db_column='XPER', null=True)
    xrel = models.SmallIntegerField(db_column='XREL', null=True)
    xten = models.SmallIntegerField(db_column='XTEN', null=True)
    xunit = models.SmallIntegerField(db_column='XUNIT', null=True)

    field_in_2013 = models.BooleanField(default=False)
    field_in_2011 = models.BooleanField(default=False)

    export_year = models.PositiveSmallIntegerField(null=True, db_index=True)
