# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='jpqidri',
            field=models.SmallIntegerField(null=True, db_column=b'JPQIDRI'),
        ),
        migrations.AddField(
            model_name='person',
            name='jpqotalm',
            field=models.SmallIntegerField(null=True, db_column=b'JPQOTALM'),
        ),
        migrations.AddField(
            model_name='person',
            name='othest',
            field=models.SmallIntegerField(null=True, db_column=b'OTHEST'),
        ),
        migrations.AddField(
            model_name='person',
            name='pqidri',
            field=models.SmallIntegerField(null=True, db_column=b'PQIDRI'),
        ),
        migrations.AddField(
            model_name='person',
            name='pqotalm',
            field=models.SmallIntegerField(null=True, db_column=b'PQOTALM'),
        ),
    ]
