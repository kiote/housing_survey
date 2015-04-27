# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topical', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topical',
            name='cefclosknit',
            field=models.SmallIntegerField(null=True, db_column=b'CEFCLOSKNIT'),
        ),
        migrations.AddField(
            model_name='topical',
            name='cefdisrspct',
            field=models.SmallIntegerField(null=True, db_column=b'CEFDISRSPCT'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ceffighting',
            field=models.SmallIntegerField(null=True, db_column=b'CEFFIGHTING'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ceffiresta',
            field=models.SmallIntegerField(null=True, db_column=b'CEFFIRESTA'),
        ),
        migrations.AddField(
            model_name='topical',
            name='cefgetalong',
            field=models.SmallIntegerField(null=True, db_column=b'CEFGETALONG'),
        ),
        migrations.AddField(
            model_name='topical',
            name='cefgpblock',
            field=models.SmallIntegerField(null=True, db_column=b'CEFGPBLOCK'),
        ),
        migrations.AddField(
            model_name='topical',
            name='cefgpchurch',
            field=models.SmallIntegerField(null=True, db_column=b'CEFGPCHURCH'),
        ),
        migrations.AddField(
            model_name='topical',
            name='cefgpcivic',
            field=models.SmallIntegerField(null=True, db_column=b'CEFGPCIVIC'),
        ),
        migrations.AddField(
            model_name='topical',
            name='cefhelpnbor',
            field=models.SmallIntegerField(null=True, db_column=b'CEFHELPNBOR'),
        ),
        migrations.AddField(
            model_name='topical',
            name='cefsharvals',
            field=models.SmallIntegerField(null=True, db_column=b'CEFSHARVALS'),
        ),
        migrations.AddField(
            model_name='topical',
            name='cefskipschl',
            field=models.SmallIntegerField(null=True, db_column=b'CEFSKIPSCHL'),
        ),
        migrations.AddField(
            model_name='topical',
            name='cefspkmeetg',
            field=models.SmallIntegerField(null=True, db_column=b'CEFSPKMEETG'),
        ),
        migrations.AddField(
            model_name='topical',
            name='cefspknbors',
            field=models.SmallIntegerField(null=True, db_column=b'CEFSPKNBORS'),
        ),
        migrations.AddField(
            model_name='topical',
            name='cefspkoffcl',
            field=models.SmallIntegerField(null=True, db_column=b'CEFSPKOFFCL'),
        ),
        migrations.AddField(
            model_name='topical',
            name='cefspkprblm',
            field=models.SmallIntegerField(null=True, db_column=b'CEFSPKPRBLM'),
        ),
        migrations.AddField(
            model_name='topical',
            name='cefspkrelg',
            field=models.SmallIntegerField(null=True, db_column=b'CEFSPKRELG'),
        ),
        migrations.AddField(
            model_name='topical',
            name='cefsprypnt',
            field=models.SmallIntegerField(null=True, db_column=b'CEFSPRYPNT'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ceftrusted',
            field=models.SmallIntegerField(null=True, db_column=b'CEFTRUSTED'),
        ),
        migrations.AddField(
            model_name='topical',
            name='dpaltcom',
            field=models.SmallIntegerField(null=True, db_column=b'DPALTCOM'),
        ),
        migrations.AddField(
            model_name='topical',
            name='dpbnread',
            field=models.SmallIntegerField(null=True, db_column=b'DPBNREAD'),
        ),
        migrations.AddField(
            model_name='topical',
            name='dpdrfood',
            field=models.SmallIntegerField(null=True, db_column=b'DPDRFOOD'),
        ),
        migrations.AddField(
            model_name='topical',
            name='dpemwater',
            field=models.SmallIntegerField(null=True, db_column=b'DPEMWATER'),
        ),
        migrations.AddField(
            model_name='topical',
            name='dpevacpets',
            field=models.SmallIntegerField(null=True, db_column=b'DPEVACPETS'),
        ),
        migrations.AddField(
            model_name='topical',
            name='dpevfin',
            field=models.SmallIntegerField(null=True, db_column=b'DPEVFIN'),
        ),
        migrations.AddField(
            model_name='topical',
            name='dpevinfo',
            field=models.SmallIntegerField(null=True, db_column=b'DPEVINFO'),
        ),
        migrations.AddField(
            model_name='topical',
            name='dpevkit',
            field=models.SmallIntegerField(null=True, db_column=b'DPEVKIT'),
        ),
        migrations.AddField(
            model_name='topical',
            name='dpevloc',
            field=models.SmallIntegerField(null=True, db_column=b'DPEVLOC'),
        ),
        migrations.AddField(
            model_name='topical',
            name='dpevsep',
            field=models.SmallIntegerField(null=True, db_column=b'DPEVSEP'),
        ),
        migrations.AddField(
            model_name='topical',
            name='dpevvehic',
            field=models.SmallIntegerField(null=True, db_column=b'DPEVVEHIC'),
        ),
        migrations.AddField(
            model_name='topical',
            name='dpgenert',
            field=models.SmallIntegerField(null=True, db_column=b'DPGENERT'),
        ),
        migrations.AddField(
            model_name='topical',
            name='drugstore',
            field=models.SmallIntegerField(null=True, db_column=b'DRUGSTORE'),
        ),
        migrations.AddField(
            model_name='topical',
            name='eaban',
            field=models.SmallIntegerField(null=True, db_column=b'EABAN'),
        ),
        migrations.AddField(
            model_name='topical',
            name='eage',
            field=models.SmallIntegerField(null=True, db_column=b'EAGE'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ebarcl',
            field=models.SmallIntegerField(null=True, db_column=b'EBARCL'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ecom1',
            field=models.SmallIntegerField(null=True, db_column=b'ECOM1'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ecom2',
            field=models.SmallIntegerField(null=True, db_column=b'ECOM2'),
        ),
        migrations.AddField(
            model_name='topical',
            name='egreen',
            field=models.SmallIntegerField(null=True, db_column=b'EGREEN'),
        ),
        migrations.AddField(
            model_name='topical',
            name='eheight',
            field=models.SmallIntegerField(null=True, db_column=b'EHEIGHT'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ejunk',
            field=models.SmallIntegerField(null=True, db_column=b'EJUNK'),
        ),
        migrations.AddField(
            model_name='topical',
            name='eprkg',
            field=models.SmallIntegerField(null=True, db_column=b'EPRKG'),
        ),
        migrations.AddField(
            model_name='topical',
            name='eroad',
            field=models.SmallIntegerField(null=True, db_column=b'EROAD'),
        ),
        migrations.AddField(
            model_name='topical',
            name='etrans',
            field=models.SmallIntegerField(null=True, db_column=b'ETRANS'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ewater',
            field=models.SmallIntegerField(null=True, db_column=b'EWATER'),
        ),
        migrations.AddField(
            model_name='topical',
            name='friends',
            field=models.SmallIntegerField(null=True, db_column=b'FRIENDS'),
        ),
        migrations.AddField(
            model_name='topical',
            name='grocery',
            field=models.SmallIntegerField(null=True, db_column=b'GROCERY'),
        ),
        migrations.AddField(
            model_name='topical',
            name='nhdbldmh',
            field=models.SmallIntegerField(null=True, db_column=b'NHDBLDMH'),
        ),
        migrations.AddField(
            model_name='topical',
            name='nhdbldmu',
            field=models.SmallIntegerField(null=True, db_column=b'NHDBLDMU'),
        ),
        migrations.AddField(
            model_name='topical',
            name='nhdbldsua',
            field=models.SmallIntegerField(null=True, db_column=b'NHDBLDSUA'),
        ),
        migrations.AddField(
            model_name='topical',
            name='nhdbldsud',
            field=models.SmallIntegerField(null=True, db_column=b'NHDBLDSUD'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptbank',
            field=models.SmallIntegerField(null=True, db_column=b'PTBANK'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptcostcarm',
            field=models.IntegerField(null=True, db_column=b'PTCOSTCARM'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptcostcarp',
            field=models.IntegerField(null=True, db_column=b'PTCOSTCARP'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptcostgas',
            field=models.IntegerField(null=True, db_column=b'PTCOSTGAS'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptcostinsu',
            field=models.IntegerField(null=True, db_column=b'PTCOSTINSU'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptcostpark',
            field=models.IntegerField(null=True, db_column=b'PTCOSTPARK'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptcostptr',
            field=models.IntegerField(null=True, db_column=b'PTCOSTPTR'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptdisbus',
            field=models.SmallIntegerField(null=True, db_column=b'PTDISBUS'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptdispub',
            field=models.SmallIntegerField(null=True, db_column=b'PTDISPUB'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptdisrail',
            field=models.SmallIntegerField(null=True, db_column=b'PTDISRAIL'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptdisshut',
            field=models.SmallIntegerField(null=True, db_column=b'PTDISSHUT'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptdissub',
            field=models.SmallIntegerField(null=True, db_column=b'PTDISSUB'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptentmnt',
            field=models.SmallIntegerField(null=True, db_column=b'PTENTMNT'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptgetbus',
            field=models.SmallIntegerField(null=True, db_column=b'PTGETBUS'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptgetrail',
            field=models.SmallIntegerField(null=True, db_column=b'PTGETRAIL'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptgetshut',
            field=models.SmallIntegerField(null=True, db_column=b'PTGETSHUT'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptgetsub',
            field=models.SmallIntegerField(null=True, db_column=b'PTGETSUB'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptgrocer',
            field=models.SmallIntegerField(null=True, db_column=b'PTGROCER'),
        ),
        migrations.AddField(
            model_name='topical',
            name='pthealth',
            field=models.SmallIntegerField(null=True, db_column=b'PTHEALTH'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptoftbus',
            field=models.SmallIntegerField(null=True, db_column=b'PTOFTBUS'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptoftrail',
            field=models.SmallIntegerField(null=True, db_column=b'PTOFTRAIL'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptoftshut',
            field=models.SmallIntegerField(null=True, db_column=b'PTOFTSHUT'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptoftsub',
            field=models.SmallIntegerField(null=True, db_column=b'PTOFTSUB'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptpubtrn',
            field=models.SmallIntegerField(null=True, db_column=b'PTPUBTRN'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptretail',
            field=models.SmallIntegerField(null=True, db_column=b'PTRETAIL'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptservic',
            field=models.SmallIntegerField(null=True, db_column=b'PTSERVIC'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptusbus',
            field=models.SmallIntegerField(null=True, db_column=b'PTUSBUS'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptuscrpl',
            field=models.SmallIntegerField(null=True, db_column=b'PTUSCRPL'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptuscrsh',
            field=models.SmallIntegerField(null=True, db_column=b'PTUSCRSH'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptusotr',
            field=models.SmallIntegerField(null=True, db_column=b'PTUSOTR'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptusrail',
            field=models.SmallIntegerField(null=True, db_column=b'PTUSRAIL'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptusshut',
            field=models.SmallIntegerField(null=True, db_column=b'PTUSSHUT'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptussub',
            field=models.SmallIntegerField(null=True, db_column=b'PTUSSUB'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptustaxi',
            field=models.SmallIntegerField(null=True, db_column=b'PTUSTAXI'),
        ),
        migrations.AddField(
            model_name='topical',
            name='ptwkschl',
            field=models.SmallIntegerField(null=True, db_column=b'PTWKSCHL'),
        ),
        migrations.AddField(
            model_name='topical',
            name='satpol',
            field=models.SmallIntegerField(null=True, db_column=b'SATPOL'),
        ),
        migrations.AddField(
            model_name='topical',
            name='smsa',
            field=models.PositiveIntegerField(null=True, db_column=b'SMSA'),
        ),
        migrations.AddField(
            model_name='topical',
            name='spltwgt1',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'SPLTWGT1'),
        ),
        migrations.AddField(
            model_name='topical',
            name='spltwgt2',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'SPLTWGT2'),
        ),
        migrations.AddField(
            model_name='topical',
            name='talknbor',
            field=models.SmallIntegerField(null=True, db_column=b'TALKNBOR'),
        ),
        migrations.AddField(
            model_name='topical',
            name='volnteer',
            field=models.SmallIntegerField(null=True, db_column=b'VOLNTEER'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbbank',
            field=models.SmallIntegerField(null=True, db_column=b'WBBANK'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbbikelane',
            field=models.SmallIntegerField(null=True, db_column=b'WBBIKELANE'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbbikewalk',
            field=models.SmallIntegerField(null=True, db_column=b'WBBIKEWALK'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbentmnt',
            field=models.SmallIntegerField(null=True, db_column=b'WBENTMNT'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbgrocer',
            field=models.SmallIntegerField(null=True, db_column=b'WBGROCER'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbhealth',
            field=models.SmallIntegerField(null=True, db_column=b'WBHEALTH'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbnobike',
            field=models.SmallIntegerField(null=True, db_column=b'WBNOBIKE'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbnobkbdsw',
            field=models.SmallIntegerField(null=True, db_column=b'WBNOBKBDSW'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbnobkbike',
            field=models.SmallIntegerField(null=True, db_column=b'WBNOBKBIKE'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbnobkcrim',
            field=models.SmallIntegerField(null=True, db_column=b'WBNOBKCRIM'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbnobkdest',
            field=models.SmallIntegerField(null=True, db_column=b'WBNOBKDEST'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbnobkfast',
            field=models.SmallIntegerField(null=True, db_column=b'WBNOBKFAST'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbnobkhlth',
            field=models.SmallIntegerField(null=True, db_column=b'WBNOBKHLTH'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbnobklane',
            field=models.SmallIntegerField(null=True, db_column=b'WBNOBKLANE'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbnobklite',
            field=models.SmallIntegerField(null=True, db_column=b'WBNOBKLITE'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbnobknosw',
            field=models.SmallIntegerField(null=True, db_column=b'WBNOBKNOSW'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbnobkothr',
            field=models.SmallIntegerField(null=True, db_column=b'WBNOBKOTHR'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbnobktime',
            field=models.SmallIntegerField(null=True, db_column=b'WBNOBKTIME'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbnobktraf',
            field=models.SmallIntegerField(null=True, db_column=b'WBNOBKTRAF'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbretail',
            field=models.SmallIntegerField(null=True, db_column=b'WBRETAIL'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbservic',
            field=models.SmallIntegerField(null=True, db_column=b'WBSERVIC'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbsidewalk',
            field=models.SmallIntegerField(null=True, db_column=b'WBSIDEWALK'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wbwkschl',
            field=models.SmallIntegerField(null=True, db_column=b'WBWKSCHL'),
        ),
        migrations.AddField(
            model_name='topical',
            name='wfprop',
            field=models.SmallIntegerField(null=True, db_column=b'WFPROP'),
        ),
    ]
