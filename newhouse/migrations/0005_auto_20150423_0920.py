# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0004_auto_20150423_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newhouse',
            name='amte',
            field=models.IntegerField(null=True, db_column=b'AMTE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='amtf',
            field=models.IntegerField(null=True, db_column=b'AMTF'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='amtg',
            field=models.SmallIntegerField(null=True, db_column=b'AMTG'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='amti',
            field=models.IntegerField(null=True, db_column=b'AMTI'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='amto',
            field=models.IntegerField(null=True, db_column=b'AMTO'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='amtt',
            field=models.IntegerField(null=True, db_column=b'AMTT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='amtw',
            field=models.IntegerField(null=True, db_column=b'AMTW'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='amtx',
            field=models.IntegerField(null=True, db_column=b'AMTX'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='built',
            field=models.IntegerField(null=True, db_column=b'BUILT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='clpeva',
            field=models.IntegerField(null=True, db_column=b'CLPEVA'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='confee',
            field=models.SmallIntegerField(null=True, db_column=b'CONFEE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='cprice',
            field=models.IntegerField(null=True, db_column=b'CPRICE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='cstmnt',
            field=models.IntegerField(null=True, db_column=b'CSTMNT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhinusyr',
            field=models.IntegerField(null=True, db_column=b'HHINUSYR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhmove',
            field=models.IntegerField(null=True, db_column=b'HHMOVE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhnatvty',
            field=models.IntegerField(null=True, db_column=b'HHNATVTY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpvother',
            field=models.IntegerField(null=True, db_column=b'HHPVOTHER'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhsal',
            field=models.IntegerField(null=True, db_column=b'HHSAL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='ipov',
            field=models.IntegerField(null=True, db_column=b'IPOV'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='lodg',
            field=models.SmallIntegerField(null=True, db_column=b'LODG'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='lot',
            field=models.IntegerField(null=True, db_column=b'LOT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='lprice',
            field=models.IntegerField(null=True, db_column=b'LPRICE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='lrent',
            field=models.SmallIntegerField(null=True, db_column=b'LRENT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='lvalue',
            field=models.IntegerField(null=True, db_column=b'LVALUE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mhotfe',
            field=models.SmallIntegerField(null=True, db_column=b'MHOTFE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nunits',
            field=models.SmallIntegerField(null=True, db_column=b'NUNITS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='poor',
            field=models.IntegerField(null=True, db_column=b'POOR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='prent',
            field=models.IntegerField(null=True, db_column=b'PRENT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='prin01',
            field=models.IntegerField(null=True, db_column=b'PRIN01'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='pvalue',
            field=models.IntegerField(null=True, db_column=b'PVALUE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='rac',
            field=models.IntegerField(null=True, db_column=b'RAC'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='rent',
            field=models.IntegerField(null=True, db_column=b'RENT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='samedu',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'SAMEDU'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='samehh',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'SAMEHH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='type',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'TYPE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='unitsf',
            field=models.IntegerField(null=True, db_column=b'UNITSF'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='usfcam',
            field=models.SmallIntegerField(null=True, db_column=b'USFCAM'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='value',
            field=models.IntegerField(null=True, db_column=b'VALUE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='vother',
            field=models.IntegerField(null=True, db_column=b'VOTHER'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='vother2',
            field=models.IntegerField(null=True, db_column=b'VOTHER2'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='whnget',
            field=models.IntegerField(null=True, db_column=b'WHNGET'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='zinc',
            field=models.IntegerField(null=True, db_column=b'ZINC'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='zinc2',
            field=models.IntegerField(null=True, db_column=b'ZINC2'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='zsmhc',
            field=models.IntegerField(null=True, db_column=b'ZSMHC'),
        ),
    ]
