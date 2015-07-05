# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datatype', '0003_auto_20150705_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.PositiveSmallIntegerField()),
                ('filed', models.ForeignKey(to='datatype.Datatype')),
            ],
            options={
                'db_table': 'ahs_service_datatype_year',
            },
        ),
    ]
