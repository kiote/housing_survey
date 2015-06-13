# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20150608_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='export_year_2011',
            new_name='field_in_2011',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='export_year_2013',
            new_name='field_in_2013',
        ),
        migrations.AddField(
            model_name='person',
            name='export_year',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='pasthwho',
            field=models.SmallIntegerField(null=True, db_column=b'PASTHWHO'),
        ),
        migrations.AddField(
            model_name='person',
            name='pbtub',
            field=models.SmallIntegerField(null=True, db_column=b'PBTUB'),
        ),
        migrations.AddField(
            model_name='person',
            name='pctruse',
            field=models.SmallIntegerField(null=True, db_column=b'PCTRUSE'),
        ),
        migrations.AddField(
            model_name='person',
            name='pfaucet',
            field=models.SmallIntegerField(null=True, db_column=b'PFAUCET'),
        ),
        migrations.AddField(
            model_name='person',
            name='pgetbr',
            field=models.SmallIntegerField(null=True, db_column=b'PGETBR'),
        ),
        migrations.AddField(
            model_name='person',
            name='pgrasp',
            field=models.SmallIntegerField(null=True, db_column=b'PGRASP'),
        ),
        migrations.AddField(
            model_name='person',
            name='pkcab',
            field=models.SmallIntegerField(null=True, db_column=b'PKCAB'),
        ),
        migrations.AddField(
            model_name='person',
            name='pocab',
            field=models.SmallIntegerField(null=True, db_column=b'POCAB'),
        ),
        migrations.AddField(
            model_name='person',
            name='preach',
            field=models.SmallIntegerField(null=True, db_column=b'PREACH'),
        ),
        migrations.AddField(
            model_name='person',
            name='psink',
            field=models.SmallIntegerField(null=True, db_column=b'PSINK'),
        ),
        migrations.AddField(
            model_name='person',
            name='pstoop',
            field=models.SmallIntegerField(null=True, db_column=b'PSTOOP'),
        ),
        migrations.AddField(
            model_name='person',
            name='pstov',
            field=models.SmallIntegerField(null=True, db_column=b'PSTOV'),
        ),
        migrations.AddField(
            model_name='person',
            name='pwshwr',
            field=models.SmallIntegerField(null=True, db_column=b'PWSHWR'),
        ),
        migrations.AlterField(
            model_name='person',
            name='pline',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'PLINE'),
        ),
    ]
