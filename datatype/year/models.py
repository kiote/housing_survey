from django.db import models
from datatype.models import Datatype


class Year(models.Model):
    class Meta:
        db_table = 'ahs_service_datatype_year'

    table_field = models.ForeignKey(Datatype)
    year = models.PositiveSmallIntegerField()
