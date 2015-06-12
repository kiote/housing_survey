from django.db import models


class Datatype(models.Model):
    class Meta:
        db_table = 'ahs_service_datatype'
        unique_together = ('table_name', 'field_name')

    table_name = models.CharField(max_length=120)
    field_name = models.CharField(max_length=120)
    field_type = models.CharField(max_length=120)
    extra_params = models.CharField(max_length=350)
    export_year_2013 = models.BooleanField(default=False)
    export_year_2011 = models.BooleanField(default=False)
