from django.db import models


class Datatype(models.Model):
    class Meta:
        db_table = 'ahs_service_datatype'
        unique_together = ('table_name', 'field_name')

    table_name = models.CharField(max_length=120)
    field_name = models.CharField(max_length=120)
    field_type = models.CharField(max_length=120)
    extra_params = models.CharField(max_length=350)

    @staticmethod
    def fields_by_table(table_name):
        """Return array with fields for particular table."""
        return Datatype.objects.filter(table_name=table_name)

    @staticmethod
    def get_row_names(table_name):
        """Get rows list from service table, to prepare insert-query."""
        return [row.field_name for row in Datatype.fields_by_table(table_name)]

    @staticmethod
    def get_row_types(table_name):
        return [row.field_type for row in Datatype.fields_by_table(table_name)]
