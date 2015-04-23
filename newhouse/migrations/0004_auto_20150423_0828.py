# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0003_auto_20150423_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newhouse',
            name='usfcam',
            field=models.PositiveIntegerField(null=True, db_column=b'USFCAM'),
        ),
    ]
