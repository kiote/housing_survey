# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0001_squashed_0002_auto_20150424_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratiov',
            fields=[
                ('control', models.OneToOneField(primary_key=True, serialize=False, to='newhouse.Newhouse')),
                ('rgroc', models.SmallIntegerField(null=True, db_column=b'RGROC')),
                ('rmedi', models.SmallIntegerField(null=True, db_column=b'RMEDI')),
                ('smsa', models.PositiveIntegerField(null=True, db_column=b'SMSA')),
                ('rcarp', models.SmallIntegerField(null=True, db_column=b'RCARP')),
                ('rutil', models.SmallIntegerField(null=True, db_column=b'RUTIL')),
                ('rcost', models.SmallIntegerField(null=True, db_column=b'RCOST')),
                ('rclot', models.SmallIntegerField(null=True, db_column=b'RCLOT')),
                ('rkidc', models.SmallIntegerField(null=True, db_column=b'RKIDC')),
                ('rothe', models.SmallIntegerField(null=True, db_column=b'ROTHE')),
            ],
        ),
    ]
