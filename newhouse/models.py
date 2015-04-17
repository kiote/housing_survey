from django.db import models

class Newhouse(models.Model):
    control = models.BigIntegerField(Field.db_column = "CONTROL", Field.unique = True, Field.primary_key = True)
