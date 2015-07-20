# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rmov', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rmov',
            name='jvcnt1',
            field=models.SmallIntegerField(null=True, db_column=b'JVCNT1'),
        ),
        migrations.AddField(
            model_name='rmov',
            name='jvcnt2',
            field=models.SmallIntegerField(null=True, db_column=b'JVCNT2'),
        ),
        migrations.AddField(
            model_name='rmov',
            name='jvcnt3',
            field=models.SmallIntegerField(null=True, db_column=b'JVCNT3'),
        ),
    ]
