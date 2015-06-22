# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datatype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('table_name', models.CharField(max_length=120)),
                ('field_name', models.CharField(max_length=120)),
                ('field_type', models.CharField(max_length=120)),
                ('extra_params', models.CharField(max_length=350)),
                ('export_year_2013', models.BooleanField(default=False)),
                ('export_year_2011', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ahs_service_datatype',
            },
        ),
        migrations.AlterUniqueTogether(
            name='datatype',
            unique_together=set([('table_name', 'field_name')]),
        ),
    ]
