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

    @staticmethod
    def get_fields_for(table_name, year):
        """
        Return array with fields for particular table and year
        """
        is_2013 = year == 2013
        is_2011 = year == 2011
        fields = Datatype.objects.filter(table_name=table_name, export_year_2013=is_2013, export_year_2011=is_2011)

        return [field.field_name for field in fields]
