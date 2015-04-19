# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newhouse',
            fields=[
                ('control', models.BigIntegerField(unique=True, serialize=False, primary_key=True, db_column=b'CONTROL')),
            ],
        ),
    ]
