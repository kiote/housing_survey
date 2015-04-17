from django.db import models

class Newhouse(models.Model):
    control = models.BigIntegerField(db_column = "CONTROL", unique = True, primary_key = True)
