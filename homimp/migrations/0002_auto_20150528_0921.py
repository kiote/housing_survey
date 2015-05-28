# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homimp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homimp',
            name='smsa',
        ),
        migrations.AlterField(
            model_name='homimp',
            name='rad',
            field=models.PositiveIntegerField(null=True, db_column=b'RAD'),
        ),
    ]
