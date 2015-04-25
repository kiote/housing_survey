from django.db import models
from newhouse.models import Newhouse


class Ratiov(models.Model):
    control = models.OneToOneField(Newhouse, primary_key=True)