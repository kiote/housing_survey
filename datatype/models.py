from django.db import models


class ParticularTable:
    def __init__(self, table):
        self.objects = Datatype.objects.filter(table_name=table)

    def get_row_names(self):
        return [row.field_name for row in self.objects]

    def get_row_types(self):
        return [row.field_type for row in self.objects]

class Datatype(models.Model):
    class Meta:
        db_table = 'ahs_service_datatype'
        unique_together = ('table_name', 'field_name')

    table_name = models.CharField(max_length=120, db_index=True)
    field_name = models.CharField(max_length=120)
    field_type = models.CharField(max_length=120)
    extra_params = models.CharField(max_length=350)
