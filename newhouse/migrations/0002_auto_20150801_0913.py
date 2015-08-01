# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newhouse',
            name='changedrecord',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'ChangedRecord'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jqidri',
            field=models.SmallIntegerField(null=True, db_column=b'jqidri'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jqotalm',
            field=models.SmallIntegerField(null=True, db_column=b'jqotalm'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='qidri',
            field=models.SmallIntegerField(null=True, db_column=b'qidri'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='qotalm',
            field=models.SmallIntegerField(null=True, db_column=b'qotalm'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dfrpl',
            field=models.SmallIntegerField(null=True, db_column=b'dfrpl'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dfrpli',
            field=models.SmallIntegerField(null=True, db_column=b'dfrpli'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='ffrpl',
            field=models.SmallIntegerField(null=True, db_column=b'ffrpl'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='ffrpli',
            field=models.SmallIntegerField(null=True, db_column=b'ffrpli'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='pfrpl',
            field=models.SmallIntegerField(null=True, db_column=b'pfrpl'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='pfrpli',
            field=models.SmallIntegerField(null=True, db_column=b'pfrpli'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='scoal',
            field=models.SmallIntegerField(null=True, db_column=b'scoal'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='sflin',
            field=models.SmallIntegerField(null=True, db_column=b'sflin'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='sfrpl',
            field=models.SmallIntegerField(null=True, db_column=b'sfrpl'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='sfrpli',
            field=models.SmallIntegerField(null=True, db_column=b'sfrpli'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='sgas',
            field=models.SmallIntegerField(null=True, db_column=b'sgas'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='sjuice',
            field=models.SmallIntegerField(null=True, db_column=b'sjuice'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='skero',
            field=models.SmallIntegerField(null=True, db_column=b'skero'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='soil',
            field=models.SmallIntegerField(null=True, db_column=b'soil'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='sother',
            field=models.SmallIntegerField(null=True, db_column=b'sother'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='sporth',
            field=models.SmallIntegerField(null=True, db_column=b'sporth'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='ssun',
            field=models.SmallIntegerField(null=True, db_column=b'ssun'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='swood',
            field=models.SmallIntegerField(null=True, db_column=b'swood'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='timetrn',
            field=models.IntegerField(null=True, db_column=b'TIMETRN'),
        ),
    ]
