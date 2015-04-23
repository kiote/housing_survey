# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newhouse',
            name='access',
            field=models.SmallIntegerField(null=True, db_column=b'ACCESS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='afuel',
            field=models.SmallIntegerField(null=True, db_column=b'AFUEL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='air',
            field=models.SmallIntegerField(null=True, db_column=b'AIR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='airsys',
            field=models.SmallIntegerField(null=True, db_column=b'AIRSYS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='almv',
            field=models.SmallIntegerField(null=True, db_column=b'ALMV'),
        ),
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
            field=models.IntegerField(null=True, db_column=b'AMTG'),
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
            name='baths',
            field=models.SmallIntegerField(null=True, db_column=b'BATHS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='bedrms',
            field=models.SmallIntegerField(null=True, db_column=b'BEDRMS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='bigp',
            field=models.SmallIntegerField(null=True, db_column=b'BIGP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='bille',
            field=models.SmallIntegerField(null=True, db_column=b'BILLE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='billg',
            field=models.SmallIntegerField(null=True, db_column=b'BILLG'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='billw',
            field=models.SmallIntegerField(null=True, db_column=b'BILLW'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='bsink',
            field=models.SmallIntegerField(null=True, db_column=b'BSINK'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='busper',
            field=models.SmallIntegerField(null=True, db_column=b'BUSPER'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='buyf',
            field=models.SmallIntegerField(null=True, db_column=b'BUYF'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='buyi',
            field=models.SmallIntegerField(null=True, db_column=b'BUYI'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='buyo',
            field=models.SmallIntegerField(null=True, db_column=b'BUYO'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='buyt',
            field=models.SmallIntegerField(null=True, db_column=b'BUYT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='camf',
            field=models.SmallIntegerField(null=True, db_column=b'CAMF'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='cars',
            field=models.SmallIntegerField(null=True, db_column=b'CARS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='cellar',
            field=models.SmallIntegerField(null=True, db_column=b'CELLAR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='cfuel',
            field=models.SmallIntegerField(null=True, db_column=b'CFUEL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='clpeva',
            field=models.IntegerField(null=True, db_column=b'CLPEVA'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='condo',
            field=models.SmallIntegerField(null=True, db_column=b'CONDO'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='confee',
            field=models.IntegerField(null=True, db_column=b'CONFEE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='cook',
            field=models.SmallIntegerField(null=True, db_column=b'COOK'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='cprice',
            field=models.IntegerField(null=True, db_column=b'CPRICE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='cracks',
            field=models.SmallIntegerField(null=True, db_column=b'CRACKS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='cstmnt',
            field=models.IntegerField(null=True, db_column=b'CSTMNT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dbgrpnum',
            field=models.SmallIntegerField(null=True, db_column=b'DBGRPNUM'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dbin1reas',
            field=models.SmallIntegerField(null=True, db_column=b'DBIN1REAS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dbin1vol',
            field=models.SmallIntegerField(null=True, db_column=b'DBIN1VOL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dbin1wher',
            field=models.SmallIntegerField(null=True, db_column=b'DBIN1WHER'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dbin1why',
            field=models.SmallIntegerField(null=True, db_column=b'DBIN1WHY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dboutmove',
            field=models.SmallIntegerField(null=True, db_column=b'DBOUTMOVE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dbutbill',
            field=models.SmallIntegerField(null=True, db_column=b'DBUTBILL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dens',
            field=models.SmallIntegerField(null=True, db_column=b'DENS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dfuel',
            field=models.SmallIntegerField(null=True, db_column=b'DFUEL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dining',
            field=models.SmallIntegerField(null=True, db_column=b'DINING'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dish',
            field=models.SmallIntegerField(null=True, db_column=b'DISH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='displ',
            field=models.SmallIntegerField(null=True, db_column=b'DISPL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dline1',
            field=models.SmallIntegerField(null=True, db_column=b'DLINE1'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='drshop',
            field=models.SmallIntegerField(null=True, db_column=b'DRSHOP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dry',
            field=models.SmallIntegerField(null=True, db_column=b'DRY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dwnpay',
            field=models.SmallIntegerField(null=True, db_column=b'DWNPAY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='ebar',
            field=models.SmallIntegerField(null=True, db_column=b'EBAR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='eboard',
            field=models.SmallIntegerField(null=True, db_column=b'EBOARD'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='ebroke',
            field=models.SmallIntegerField(null=True, db_column=b'EBROKE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='ecrumb',
            field=models.SmallIntegerField(null=True, db_column=b'ECRUMB'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='egood',
            field=models.SmallIntegerField(null=True, db_column=b'EGOOD'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='eholer',
            field=models.SmallIntegerField(null=True, db_column=b'EHOLER'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='elder',
            field=models.SmallIntegerField(null=True, db_column=b'ELDER'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='emissr',
            field=models.SmallIntegerField(null=True, db_column=b'EMISSR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='emissw',
            field=models.SmallIntegerField(null=True, db_column=b'EMISSW'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='enefic',
            field=models.SmallIntegerField(null=True, db_column=b'ENEFIC'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='eroach',
            field=models.SmallIntegerField(null=True, db_column=b'EROACH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='esagr',
            field=models.SmallIntegerField(null=True, db_column=b'ESAGR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='eslopw',
            field=models.SmallIntegerField(null=True, db_column=b'ESLOPW'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='evrod',
            field=models.SmallIntegerField(null=True, db_column=b'EVROD'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='exclus',
            field=models.SmallIntegerField(null=True, db_column=b'EXCLUS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='famrm',
            field=models.SmallIntegerField(null=True, db_column=b'FAMRM'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='floors',
            field=models.SmallIntegerField(null=True, db_column=b'FLOORS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='fplwk',
            field=models.SmallIntegerField(null=True, db_column=b'FPLWK'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='freeze',
            field=models.SmallIntegerField(null=True, db_column=b'FREEZE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='frstho',
            field=models.SmallIntegerField(null=True, db_column=b'FRSTHO'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='frstoc',
            field=models.SmallIntegerField(null=True, db_column=b'FRSTOC'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='garage',
            field=models.SmallIntegerField(null=True, db_column=b'GARAGE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='gaspip',
            field=models.SmallIntegerField(null=True, db_column=b'GASPIP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='halfb',
            field=models.SmallIntegerField(null=True, db_column=b'HALFB'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hcare',
            field=models.SmallIntegerField(null=True, db_column=b'HCARE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hdsb',
            field=models.SmallIntegerField(null=True, db_column=b'HDSB'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hearhs',
            field=models.SmallIntegerField(null=True, db_column=b'HEARHS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='helc',
            field=models.SmallIntegerField(null=True, db_column=b'HELC'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='helump',
            field=models.SmallIntegerField(null=True, db_column=b'HELUMP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hequip',
            field=models.SmallIntegerField(null=True, db_column=b'HEQUIP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='herrnd',
            field=models.SmallIntegerField(null=True, db_column=b'HERRND'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hfuel',
            field=models.SmallIntegerField(null=True, db_column=b'HFUEL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhage',
            field=models.SmallIntegerField(null=True, db_column=b'HHAGE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhcitshp',
            field=models.SmallIntegerField(null=True, db_column=b'HHCITSHP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhear',
            field=models.SmallIntegerField(null=True, db_column=b'HHEAR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhgrad',
            field=models.SmallIntegerField(null=True, db_column=b'HHGRAD'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhinusyr',
            field=models.IntegerField(null=True, db_column=b'HHINUSYR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhkidu18',
            field=models.SmallIntegerField(null=True, db_column=b'HHKIDU18'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhldkid',
            field=models.SmallIntegerField(null=True, db_column=b'HHLDKID'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhmar',
            field=models.SmallIntegerField(null=True, db_column=b'HHMAR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhmovm',
            field=models.SmallIntegerField(null=True, db_column=b'HHMOVM'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhmvg',
            field=models.SmallIntegerField(null=True, db_column=b'HHMVG'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhnatvty',
            field=models.IntegerField(null=True, db_column=b'HHNATVTY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpcare',
            field=models.SmallIntegerField(null=True, db_column=b'HHPCARE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhperrnd',
            field=models.SmallIntegerField(null=True, db_column=b'HHPERRND'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhphear',
            field=models.SmallIntegerField(null=True, db_column=b'HHPHEAR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpline',
            field=models.SmallIntegerField(null=True, db_column=b'HHPLINE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpmemry',
            field=models.SmallIntegerField(null=True, db_column=b'HHPMEMRY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpqalim',
            field=models.SmallIntegerField(null=True, db_column=b'HHPQALIM'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpqdiv',
            field=models.SmallIntegerField(null=True, db_column=b'HHPQDIV'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpqint',
            field=models.SmallIntegerField(null=True, db_column=b'HHPQINT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpqother',
            field=models.SmallIntegerField(null=True, db_column=b'HHPQOTHER'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpqrent',
            field=models.SmallIntegerField(null=True, db_column=b'HHPQRENT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpqretir',
            field=models.SmallIntegerField(null=True, db_column=b'HHPQRETIR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpqsal',
            field=models.SmallIntegerField(null=True, db_column=b'HHPQSAL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpqself',
            field=models.SmallIntegerField(null=True, db_column=b'HHPQSELF'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpqss',
            field=models.SmallIntegerField(null=True, db_column=b'HHPQSS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpqssi',
            field=models.SmallIntegerField(null=True, db_column=b'HHPQSSI'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpqwelf',
            field=models.SmallIntegerField(null=True, db_column=b'HHPQWELF'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpqwkcmp',
            field=models.SmallIntegerField(null=True, db_column=b'HHPQWKCMP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpsee',
            field=models.SmallIntegerField(null=True, db_column=b'HHPSEE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhpwalk',
            field=models.SmallIntegerField(null=True, db_column=b'HHPWALK'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhrace',
            field=models.SmallIntegerField(null=True, db_column=b'HHRACE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhrel',
            field=models.SmallIntegerField(null=True, db_column=b'HHREL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhsal',
            field=models.IntegerField(null=True, db_column=b'HHSAL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhsex',
            field=models.SmallIntegerField(null=True, db_column=b'HHSEX'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhspan',
            field=models.SmallIntegerField(null=True, db_column=b'HHSPAN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hhten',
            field=models.SmallIntegerField(null=True, db_column=b'HHTEN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hmemry',
            field=models.SmallIntegerField(null=True, db_column=b'HMEMRY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='holes',
            field=models.SmallIntegerField(null=True, db_column=b'HOLES'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hotpip',
            field=models.SmallIntegerField(null=True, db_column=b'HOTPIP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='howh',
            field=models.SmallIntegerField(null=True, db_column=b'HOWH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hown',
            field=models.SmallIntegerField(null=True, db_column=b'HOWN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hsee',
            field=models.SmallIntegerField(null=True, db_column=b'HSEE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='hwalk',
            field=models.SmallIntegerField(null=True, db_column=b'HWALK'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='ifblow',
            field=models.SmallIntegerField(null=True, db_column=b'IFBLOW'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='ifdry',
            field=models.SmallIntegerField(null=True, db_column=b'IFDRY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='iffee',
            field=models.SmallIntegerField(null=True, db_column=b'IFFEE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='ifsew',
            field=models.SmallIntegerField(null=True, db_column=b'IFSEW'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='iftlt',
            field=models.SmallIntegerField(null=True, db_column=b'IFTLT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='ileak',
            field=models.SmallIntegerField(null=True, db_column=b'ILEAK'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jalmv',
            field=models.SmallIntegerField(null=True, db_column=b'JALMV'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jamte',
            field=models.SmallIntegerField(null=True, db_column=b'JAMTE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jamtg',
            field=models.SmallIntegerField(null=True, db_column=b'JAMTG'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jamti',
            field=models.SmallIntegerField(null=True, db_column=b'JAMTI'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jaundy',
            field=models.SmallIntegerField(null=True, db_column=b'JAUNDY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jbille',
            field=models.SmallIntegerField(null=True, db_column=b'JBILLE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jbillf',
            field=models.SmallIntegerField(null=True, db_column=b'JBILLF'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jbillg',
            field=models.SmallIntegerField(null=True, db_column=b'JBILLG'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jbillo',
            field=models.SmallIntegerField(null=True, db_column=b'JBILLO'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jbillt',
            field=models.SmallIntegerField(null=True, db_column=b'JBILLT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jbillw',
            field=models.SmallIntegerField(null=True, db_column=b'JBILLW'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jelump',
            field=models.SmallIntegerField(null=True, db_column=b'JELUMP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jfamrm',
            field=models.SmallIntegerField(null=True, db_column=b'JFAMRM'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jhhpvother',
            field=models.SmallIntegerField(null=True, db_column=b'JHHPVOTHER'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jhymov',
            field=models.SmallIntegerField(null=True, db_column=b'JHYMOV'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jmg',
            field=models.SmallIntegerField(null=True, db_column=b'JMG'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jothfn',
            field=models.SmallIntegerField(null=True, db_column=b'JOTHFN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jrecrm',
            field=models.SmallIntegerField(null=True, db_column=b'JRECRM'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jsegas',
            field=models.SmallIntegerField(null=True, db_column=b'JSEGAS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jthrun',
            field=models.SmallIntegerField(null=True, db_column=b'JTHRUN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='juselect',
            field=models.SmallIntegerField(null=True, db_column=b'JUSELECT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jvalu',
            field=models.SmallIntegerField(null=True, db_column=b'JVALU'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jvother',
            field=models.SmallIntegerField(null=True, db_column=b'JVOTHER'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='jvother2',
            field=models.SmallIntegerField(null=True, db_column=b'JVOTHER2'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='kidu18',
            field=models.SmallIntegerField(null=True, db_column=b'KIDU18'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='kitch',
            field=models.SmallIntegerField(null=True, db_column=b'KITCH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='kitchen',
            field=models.SmallIntegerField(null=True, db_column=b'KITCHEN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='lang',
            field=models.SmallIntegerField(null=True, db_column=b'LANG'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='laundy',
            field=models.SmallIntegerField(null=True, db_column=b'LAUNDY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='leak',
            field=models.SmallIntegerField(null=True, db_column=b'LEAK'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='living',
            field=models.SmallIntegerField(null=True, db_column=b'LIVING'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='lodg',
            field=models.IntegerField(null=True, db_column=b'LODG'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='lookhs',
            field=models.SmallIntegerField(null=True, db_column=b'LOOKHS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='lookns',
            field=models.SmallIntegerField(null=True, db_column=b'LOOKNS'),
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
            field=models.IntegerField(null=True, db_column=b'LRENT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='lvalue',
            field=models.IntegerField(null=True, db_column=b'LVALUE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='markt',
            field=models.SmallIntegerField(null=True, db_column=b'MARKT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mg',
            field=models.SmallIntegerField(null=True, db_column=b'MG'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mhotfe',
            field=models.IntegerField(null=True, db_column=b'MHOTFE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mosall',
            field=models.SmallIntegerField(null=True, db_column=b'MOSALL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mosapr',
            field=models.SmallIntegerField(null=True, db_column=b'MOSAPR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mosaug',
            field=models.SmallIntegerField(null=True, db_column=b'MOSAUG'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mosdec',
            field=models.SmallIntegerField(null=True, db_column=b'MOSDEC'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mosfeb',
            field=models.SmallIntegerField(null=True, db_column=b'MOSFEB'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mosjan',
            field=models.SmallIntegerField(null=True, db_column=b'MOSJAN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mosjul',
            field=models.SmallIntegerField(null=True, db_column=b'MOSJUL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mosjun',
            field=models.SmallIntegerField(null=True, db_column=b'MOSJUN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mosmar',
            field=models.SmallIntegerField(null=True, db_column=b'MOSMAR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mosmay',
            field=models.SmallIntegerField(null=True, db_column=b'MOSMAY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mosnov',
            field=models.SmallIntegerField(null=True, db_column=b'MOSNOV'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mosoct',
            field=models.SmallIntegerField(null=True, db_column=b'MOSOCT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mossep',
            field=models.SmallIntegerField(null=True, db_column=b'MOSSEP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='movedly',
            field=models.SmallIntegerField(null=True, db_column=b'MOVEDLY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mvcnt1',
            field=models.SmallIntegerField(null=True, db_column=b'MVCNT1'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mvcnt2',
            field=models.SmallIntegerField(null=True, db_column=b'MVCNT2'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='mvcnt3',
            field=models.SmallIntegerField(null=True, db_column=b'MVCNT3'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nlbsy',
            field=models.SmallIntegerField(null=True, db_column=b'NLBSY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nlhppy',
            field=models.SmallIntegerField(null=True, db_column=b'NLHPPY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nlmobl',
            field=models.SmallIntegerField(null=True, db_column=b'NLMOBL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nlmov',
            field=models.SmallIntegerField(null=True, db_column=b'NLMOV'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nlnlik',
            field=models.SmallIntegerField(null=True, db_column=b'NLNLIK'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nlnpr',
            field=models.SmallIntegerField(null=True, db_column=b'NLNPR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nlothr',
            field=models.SmallIntegerField(null=True, db_column=b'NLOTHR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nlunk',
            field=models.SmallIntegerField(null=True, db_column=b'NLUNK'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='none',
            field=models.SmallIntegerField(null=True, db_column=b'NONE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nonrel',
            field=models.SmallIntegerField(null=True, db_column=b'NONREL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nostep',
            field=models.SmallIntegerField(null=True, db_column=b'NOSTEP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nowire',
            field=models.SmallIntegerField(null=True, db_column=b'NOWIRE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nrownr',
            field=models.SmallIntegerField(null=True, db_column=b'NROWNR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nrpaym',
            field=models.SmallIntegerField(null=True, db_column=b'NRPAYM'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='numhs',
            field=models.SmallIntegerField(null=True, db_column=b'NUMHS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nunit2',
            field=models.SmallIntegerField(null=True, db_column=b'NUNIT2'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='nunits',
            field=models.IntegerField(null=True, db_column=b'NUNITS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='oarsys',
            field=models.SmallIntegerField(null=True, db_column=b'OARSYS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='otbup',
            field=models.SmallIntegerField(null=True, db_column=b'OTBUP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='othfn',
            field=models.SmallIntegerField(null=True, db_column=b'OTHFN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='othrun',
            field=models.SmallIntegerField(null=True, db_column=b'OTHRUN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='per',
            field=models.SmallIntegerField(null=True, db_column=b'PER'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='phone',
            field=models.SmallIntegerField(null=True, db_column=b'PHONE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='plugs',
            field=models.SmallIntegerField(null=True, db_column=b'PLUGS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='plumb',
            field=models.SmallIntegerField(null=True, db_column=b'PLUMB'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='poor',
            field=models.IntegerField(null=True, db_column=b'POOR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='porch',
            field=models.SmallIntegerField(null=True, db_column=b'PORCH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='prent',
            field=models.IntegerField(null=True, db_column=b'PRENT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='preocc',
            field=models.SmallIntegerField(null=True, db_column=b'PREOCC'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='prin01',
            field=models.IntegerField(null=True, db_column=b'PRIN01'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='pubsew',
            field=models.SmallIntegerField(null=True, db_column=b'PUBSEW'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='pvalue',
            field=models.IntegerField(null=True, db_column=b'PVALUE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='qalim',
            field=models.SmallIntegerField(null=True, db_column=b'QALIM'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='qdiv',
            field=models.SmallIntegerField(null=True, db_column=b'QDIV'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='qfs1',
            field=models.SmallIntegerField(null=True, db_column=b'QFS1'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='qint',
            field=models.SmallIntegerField(null=True, db_column=b'QINT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='qother',
            field=models.SmallIntegerField(null=True, db_column=b'QOTHER'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='qrent',
            field=models.SmallIntegerField(null=True, db_column=b'QRENT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='qretir',
            field=models.SmallIntegerField(null=True, db_column=b'QRETIR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='qself',
            field=models.SmallIntegerField(null=True, db_column=b'QSELF'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='qss',
            field=models.SmallIntegerField(null=True, db_column=b'QSS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='qssi',
            field=models.SmallIntegerField(null=True, db_column=b'QSSI'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='qwelf',
            field=models.SmallIntegerField(null=True, db_column=b'QWELF'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='qwkcmp',
            field=models.SmallIntegerField(null=True, db_column=b'QWKCMP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='rac',
            field=models.IntegerField(null=True, db_column=b'RAC'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='ram',
            field=models.SmallIntegerField(null=True, db_column=b'RAM'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='ran',
            field=models.SmallIntegerField(null=True, db_column=b'RAN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='recrm',
            field=models.SmallIntegerField(null=True, db_column=b'RECRM'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='refr',
            field=models.SmallIntegerField(null=True, db_column=b'REFR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='rent',
            field=models.IntegerField(null=True, db_column=b'RENT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='resptyp',
            field=models.SmallIntegerField(null=True, db_column=b'RESPTYP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='rooms',
            field=models.SmallIntegerField(null=True, db_column=b'ROOMS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='samedu',
            field=models.SmallIntegerField(null=True, db_column=b'SAMEDU'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='sameelec',
            field=models.SmallIntegerField(null=True, db_column=b'SAMEELEC'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='samegas',
            field=models.SmallIntegerField(null=True, db_column=b'SAMEGAS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='samehh',
            field=models.SmallIntegerField(null=True, db_column=b'SAMEHH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='samehh2',
            field=models.SmallIntegerField(null=True, db_column=b'SAMEHH2'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='sharat',
            field=models.SmallIntegerField(null=True, db_column=b'SHARAT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='sharfr',
            field=models.SmallIntegerField(null=True, db_column=b'SHARFR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='sharpf',
            field=models.SmallIntegerField(null=True, db_column=b'SHARPF'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='sink',
            field=models.SmallIntegerField(null=True, db_column=b'SINK'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='subfix',
            field=models.SmallIntegerField(null=True, db_column=b'SUBFIX'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='tadj',
            field=models.SmallIntegerField(null=True, db_column=b'TADJ'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='tenure',
            field=models.SmallIntegerField(null=True, db_column=b'TENURE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='toilet',
            field=models.SmallIntegerField(null=True, db_column=b'TOILET'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='tpbpai',
            field=models.SmallIntegerField(null=True, db_column=b'TPBPAI'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='tpbpip',
            field=models.SmallIntegerField(null=True, db_column=b'TPBPIP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='tpbsol',
            field=models.SmallIntegerField(null=True, db_column=b'TPBSOL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='trash',
            field=models.SmallIntegerField(null=True, db_column=b'TRASH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='trep',
            field=models.SmallIntegerField(null=True, db_column=b'TREP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='trucks',
            field=models.SmallIntegerField(null=True, db_column=b'TRUCKS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='tub',
            field=models.SmallIntegerField(null=True, db_column=b'TUB'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='txre',
            field=models.SmallIntegerField(null=True, db_column=b'TXRE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='type',
            field=models.SmallIntegerField(null=True, db_column=b'TYPE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='usegas',
            field=models.SmallIntegerField(null=True, db_column=b'USEGAS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='uselect',
            field=models.SmallIntegerField(null=True, db_column=b'USELECT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='useoil',
            field=models.SmallIntegerField(null=True, db_column=b'USEOIL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='useothr',
            field=models.SmallIntegerField(null=True, db_column=b'USEOTHR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='usfcam',
            field=models.IntegerField(null=True, db_column=b'USFCAM'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='usfchg',
            field=models.SmallIntegerField(null=True, db_column=b'USFCHG'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wash',
            field=models.SmallIntegerField(null=True, db_column=b'WASH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='water',
            field=models.SmallIntegerField(null=True, db_column=b'WATER'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='waters',
            field=models.SmallIntegerField(null=True, db_column=b'WATERS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='weldus',
            field=models.SmallIntegerField(null=True, db_column=b'WELDUS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wfuel',
            field=models.SmallIntegerField(null=True, db_column=b'WFUEL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='whavl',
            field=models.SmallIntegerField(null=True, db_column=b'WHAVL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='whdsn',
            field=models.SmallIntegerField(null=True, db_column=b'WHDSN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='whext',
            field=models.SmallIntegerField(null=True, db_column=b'WHEXT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='whfin',
            field=models.SmallIntegerField(null=True, db_column=b'WHFIN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='whnhd',
            field=models.SmallIntegerField(null=True, db_column=b'WHNHD'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='whoth',
            field=models.SmallIntegerField(null=True, db_column=b'WHOTH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='whqul',
            field=models.SmallIntegerField(null=True, db_column=b'WHQUL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='whsiz',
            field=models.SmallIntegerField(null=True, db_column=b'WHSIZ'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='whymove',
            field=models.SmallIntegerField(null=True, db_column=b'WHYMOVE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='whyrd',
            field=models.SmallIntegerField(null=True, db_column=b'WHYRD'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='whytoh',
            field=models.SmallIntegerField(null=True, db_column=b'WHYTOH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='whyton',
            field=models.SmallIntegerField(null=True, db_column=b'WHYTON'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmchep',
            field=models.SmallIntegerField(null=True, db_column=b'WMCHEP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmchtn',
            field=models.SmallIntegerField(null=True, db_column=b'WMCHTN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmclos',
            field=models.SmallIntegerField(null=True, db_column=b'WMCLOS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmdisl',
            field=models.SmallIntegerField(null=True, db_column=b'WMDISL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmevic',
            field=models.SmallIntegerField(null=True, db_column=b'WMEVIC'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmfaml',
            field=models.SmallIntegerField(null=True, db_column=b'WMFAML'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmfemp',
            field=models.SmallIntegerField(null=True, db_column=b'WMFEMP'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmfore',
            field=models.SmallIntegerField(null=True, db_column=b'WMFORE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmgovt',
            field=models.SmallIntegerField(null=True, db_column=b'WMGOVT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmhous',
            field=models.SmallIntegerField(null=True, db_column=b'WMHOUS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmjobs',
            field=models.SmallIntegerField(null=True, db_column=b'WMJOBS'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmlarg',
            field=models.SmallIntegerField(null=True, db_column=b'WMLARG'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmmarr',
            field=models.SmallIntegerField(null=True, db_column=b'WMMARR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmonhh',
            field=models.SmallIntegerField(null=True, db_column=b'WMONHH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmothr',
            field=models.SmallIntegerField(null=True, db_column=b'WMOTHR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmpriv',
            field=models.SmallIntegerField(null=True, db_column=b'WMPRIV'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wmqual',
            field=models.SmallIntegerField(null=True, db_column=b'WMQUAL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wnamen',
            field=models.SmallIntegerField(null=True, db_column=b'WNAMEN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wnfamilr',
            field=models.SmallIntegerField(null=True, db_column=b'WNFAMILR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wnhome',
            field=models.SmallIntegerField(null=True, db_column=b'WNHOME'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wnjob',
            field=models.SmallIntegerField(null=True, db_column=b'WNJOB'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wnlook',
            field=models.SmallIntegerField(null=True, db_column=b'WNLOOK'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wnothr',
            field=models.SmallIntegerField(null=True, db_column=b'WNOTHR'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wnpepl',
            field=models.SmallIntegerField(null=True, db_column=b'WNPEPL'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wnsafety',
            field=models.SmallIntegerField(null=True, db_column=b'WNSAFETY'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wnsch',
            field=models.SmallIntegerField(null=True, db_column=b'WNSCH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wnsrv',
            field=models.SmallIntegerField(null=True, db_column=b'WNSRV'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wntran',
            field=models.SmallIntegerField(null=True, db_column=b'WNTRAN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='xhrate',
            field=models.SmallIntegerField(null=True, db_column=b'XHRATE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='xnrate',
            field=models.SmallIntegerField(null=True, db_column=b'XNRATE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='zadeq',
            field=models.SmallIntegerField(null=True, db_column=b'ZADEQ'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='zadult',
            field=models.SmallIntegerField(null=True, db_column=b'ZADULT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='zinch',
            field=models.SmallIntegerField(null=True, db_column=b'ZINCH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='zincn',
            field=models.IntegerField(null=True, db_column=b'ZINCN'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='zmvgrp',
            field=models.SmallIntegerField(null=True, db_column=b'ZMVGRP'),
        ),
    ]
