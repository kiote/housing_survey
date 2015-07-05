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
    def get_fields_for(table_name, year):
        """
        Return array with fields for particular table and year
        """
        fields = Datatype.objects.filter(table_name=table_name,
                                         export_year=year)

        return [field.field_name for field in fields]
