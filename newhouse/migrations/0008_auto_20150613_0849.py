# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0007_auto_20150608_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newhouse',
            old_name='export_year_2011',
            new_name='field_in_2011',
        ),
        migrations.RenameField(
            model_name='newhouse',
            old_name='export_year_2013',
            new_name='field_in_2013',
        ),
        migrations.AddField(
            model_name='newhouse',
            name='asthemr',
            field=models.SmallIntegerField(null=True, db_column=b'ASTHEMR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='asthma',
            field=models.SmallIntegerField(null=True, db_column=b'ASTHMA'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='asthmed',
            field=models.SmallIntegerField(null=True, db_column=b'ASTHMED'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='battery',
            field=models.SmallIntegerField(null=True, db_column=b'BATTERY'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billef',
            field=models.SmallIntegerField(null=True, db_column=b'BILLEF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billeg',
            field=models.SmallIntegerField(null=True, db_column=b'BILLEG'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billeo',
            field=models.SmallIntegerField(null=True, db_column=b'BILLEO'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billet',
            field=models.SmallIntegerField(null=True, db_column=b'BILLET'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billew',
            field=models.SmallIntegerField(null=True, db_column=b'BILLEW'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billfe',
            field=models.SmallIntegerField(null=True, db_column=b'BILLFE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billfg',
            field=models.SmallIntegerField(null=True, db_column=b'BILLFG'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billfo',
            field=models.SmallIntegerField(null=True, db_column=b'BILLFO'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billft',
            field=models.SmallIntegerField(null=True, db_column=b'BILLFT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billfw',
            field=models.SmallIntegerField(null=True, db_column=b'BILLFW'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billge',
            field=models.SmallIntegerField(null=True, db_column=b'BILLGE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billgf',
            field=models.SmallIntegerField(null=True, db_column=b'BILLGF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billgo',
            field=models.SmallIntegerField(null=True, db_column=b'BILLGO'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billgt',
            field=models.SmallIntegerField(null=True, db_column=b'BILLGT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billgw',
            field=models.SmallIntegerField(null=True, db_column=b'BILLGW'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billoe',
            field=models.SmallIntegerField(null=True, db_column=b'BILLOE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billof',
            field=models.SmallIntegerField(null=True, db_column=b'BILLOF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billog',
            field=models.SmallIntegerField(null=True, db_column=b'BILLOG'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billot',
            field=models.SmallIntegerField(null=True, db_column=b'BILLOT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billow',
            field=models.SmallIntegerField(null=True, db_column=b'BILLOW'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billte',
            field=models.SmallIntegerField(null=True, db_column=b'BILLTE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billtf',
            field=models.SmallIntegerField(null=True, db_column=b'BILLTF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billtg',
            field=models.SmallIntegerField(null=True, db_column=b'BILLTG'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billto',
            field=models.SmallIntegerField(null=True, db_column=b'BILLTO'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billtw',
            field=models.SmallIntegerField(null=True, db_column=b'BILLTW'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billwe',
            field=models.SmallIntegerField(null=True, db_column=b'BILLWE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billwf',
            field=models.SmallIntegerField(null=True, db_column=b'BILLWF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billwg',
            field=models.SmallIntegerField(null=True, db_column=b'BILLWG'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billwo',
            field=models.SmallIntegerField(null=True, db_column=b'BILLWO'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='billwt',
            field=models.SmallIntegerField(null=True, db_column=b'BILLWT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='cane',
            field=models.SmallIntegerField(null=True, db_column=b'CANE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='chemstor',
            field=models.SmallIntegerField(null=True, db_column=b'CHEMSTOR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='clift',
            field=models.SmallIntegerField(null=True, db_column=b'CLIFT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='cobatt',
            field=models.SmallIntegerField(null=True, db_column=b'COBATT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='controlm',
            field=models.IntegerField(null=True, db_column=b'CONTROLM'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='copwr',
            field=models.SmallIntegerField(null=True, db_column=b'COPWR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='county',
            field=models.IntegerField(null=True, db_column=b'COUNTY'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='crutch',
            field=models.SmallIntegerField(null=True, db_column=b'CRUTCH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='eairc',
            field=models.SmallIntegerField(null=True, db_column=b'EAIRC'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='echair',
            field=models.SmallIntegerField(null=True, db_column=b'ECHAIR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='ecntair',
            field=models.SmallIntegerField(null=True, db_column=b'ECNTAIR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='edishwr',
            field=models.SmallIntegerField(null=True, db_column=b'EDISHWR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='edryer',
            field=models.SmallIntegerField(null=True, db_column=b'EDRYER'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='efridge',
            field=models.SmallIntegerField(null=True, db_column=b'EFRIDGE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='eheatut',
            field=models.SmallIntegerField(null=True, db_column=b'EHEATUT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='enoeapp',
            field=models.SmallIntegerField(null=True, db_column=b'ENOEAPP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='eoteapp',
            field=models.SmallIntegerField(null=True, db_column=b'EOTEAPP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='etrshcp',
            field=models.SmallIntegerField(null=True, db_column=b'ETRSHCP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='ewashr',
            field=models.SmallIntegerField(null=True, db_column=b'EWASHR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='export_year',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='extc',
            field=models.SmallIntegerField(null=True, db_column=b'EXTC'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='extcond',
            field=models.SmallIntegerField(null=True, db_column=b'EXTCOND'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='firex',
            field=models.SmallIntegerField(null=True, db_column=b'FIREX'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='h20ht',
            field=models.SmallIntegerField(null=True, db_column=b'H20HT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='h20mf',
            field=models.SmallIntegerField(null=True, db_column=b'H20MF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hbtub',
            field=models.SmallIntegerField(null=True, db_column=b'HBTUB'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hcab',
            field=models.SmallIntegerField(null=True, db_column=b'HCAB'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hctruse',
            field=models.SmallIntegerField(null=True, db_column=b'HCTRUSE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hfaucet',
            field=models.SmallIntegerField(null=True, db_column=b'HFAUCET'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hgetbr',
            field=models.SmallIntegerField(null=True, db_column=b'HGETBR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hgrasp',
            field=models.SmallIntegerField(null=True, db_column=b'HGRASP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hkcab',
            field=models.SmallIntegerField(null=True, db_column=b'HKCAB'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hkrac',
            field=models.IntegerField(null=True, db_column=b'HKRAC'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hkran',
            field=models.SmallIntegerField(null=True, db_column=b'HKRAN'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hlth',
            field=models.SmallIntegerField(null=True, db_column=b'HLTH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmacab',
            field=models.SmallIntegerField(null=True, db_column=b'HMACAB'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmbrl',
            field=models.SmallIntegerField(null=True, db_column=b'HMBRL'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmbroom',
            field=models.SmallIntegerField(null=True, db_column=b'HMBROOM'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmbst',
            field=models.SmallIntegerField(null=True, db_column=b'HMBST'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmclctrl',
            field=models.SmallIntegerField(null=True, db_column=b'HMCLCTRL'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmcount',
            field=models.SmallIntegerField(null=True, db_column=b'HMCOUNT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmelevate',
            field=models.SmallIntegerField(null=True, db_column=b'HMELEVATE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmentbd',
            field=models.SmallIntegerField(null=True, db_column=b'HMENTBD'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmentbth',
            field=models.SmallIntegerField(null=True, db_column=b'HMENTBTH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmhndle',
            field=models.SmallIntegerField(null=True, db_column=b'HMHNDLE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmhndrl',
            field=models.SmallIntegerField(null=True, db_column=b'HMHNDRL'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmkit',
            field=models.SmallIntegerField(null=True, db_column=b'HMKIT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmkitry',
            field=models.SmallIntegerField(null=True, db_column=b'HMKITRY'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmlevel',
            field=models.SmallIntegerField(null=True, db_column=b'HMLEVEL'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmorl',
            field=models.SmallIntegerField(null=True, db_column=b'HMORL'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmoutlet',
            field=models.SmallIntegerField(null=True, db_column=b'HMOUTLET'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmramps',
            field=models.SmallIntegerField(null=True, db_column=b'HMRAMPS'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmsklvr',
            field=models.SmallIntegerField(null=True, db_column=b'HMSKLVR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmswitch',
            field=models.SmallIntegerField(null=True, db_column=b'HMSWITCH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmtoilet',
            field=models.SmallIntegerField(null=True, db_column=b'HMTOILET'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmwheeln',
            field=models.SmallIntegerField(null=True, db_column=b'HMWHEELN'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hmxwdr',
            field=models.SmallIntegerField(null=True, db_column=b'HMXWDR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hreach',
            field=models.SmallIntegerField(null=True, db_column=b'HREACH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hsink',
            field=models.SmallIntegerField(null=True, db_column=b'HSINK'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hstoop',
            field=models.SmallIntegerField(null=True, db_column=b'HSTOOP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hstov',
            field=models.SmallIntegerField(null=True, db_column=b'HSTOV'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hudadmin',
            field=models.SmallIntegerField(null=True, db_column=b'HUDADMIN'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hudsamp',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'HUDSAMP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hwshwr',
            field=models.SmallIntegerField(null=True, db_column=b'HWSHWR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmacab',
            field=models.SmallIntegerField(null=True, db_column=b'JHMACAB'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmbrl',
            field=models.SmallIntegerField(null=True, db_column=b'JHMBRL'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmbroom',
            field=models.SmallIntegerField(null=True, db_column=b'JHMBROOM'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmbst',
            field=models.SmallIntegerField(null=True, db_column=b'JHMBST'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmclctrl',
            field=models.SmallIntegerField(null=True, db_column=b'JHMCLCTRL'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmcount',
            field=models.SmallIntegerField(null=True, db_column=b'JHMCOUNT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmelevte',
            field=models.SmallIntegerField(null=True, db_column=b'JHMELEVTE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmentbd',
            field=models.SmallIntegerField(null=True, db_column=b'JHMENTBD'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmentbth',
            field=models.SmallIntegerField(null=True, db_column=b'JHMENTBTH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmhndle',
            field=models.SmallIntegerField(null=True, db_column=b'JHMHNDLE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmhndrl',
            field=models.SmallIntegerField(null=True, db_column=b'JHMHNDRL'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmkit',
            field=models.SmallIntegerField(null=True, db_column=b'JHMKIT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmkitry',
            field=models.SmallIntegerField(null=True, db_column=b'JHMKITRY'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmlevel',
            field=models.SmallIntegerField(null=True, db_column=b'JHMLEVEL'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmorl',
            field=models.SmallIntegerField(null=True, db_column=b'JHMORL'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmoutet',
            field=models.SmallIntegerField(null=True, db_column=b'JHMOUTET'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmramps',
            field=models.SmallIntegerField(null=True, db_column=b'JHMRAMPS'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmsklvr',
            field=models.SmallIntegerField(null=True, db_column=b'JHMSKLVR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmswitch',
            field=models.SmallIntegerField(null=True, db_column=b'JHMSWITCH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmtoilet',
            field=models.SmallIntegerField(null=True, db_column=b'JHMTOILET'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jhmxwdr',
            field=models.SmallIntegerField(null=True, db_column=b'JHMXWDR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillef',
            field=models.SmallIntegerField(null=True, db_column=b'JILLEF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jilleg',
            field=models.SmallIntegerField(null=True, db_column=b'JILLEG'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jilleo',
            field=models.SmallIntegerField(null=True, db_column=b'JILLEO'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillet',
            field=models.SmallIntegerField(null=True, db_column=b'JILLET'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillew',
            field=models.SmallIntegerField(null=True, db_column=b'JILLEW'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillfe',
            field=models.SmallIntegerField(null=True, db_column=b'JILLFE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillfg',
            field=models.SmallIntegerField(null=True, db_column=b'JILLFG'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillfo',
            field=models.SmallIntegerField(null=True, db_column=b'JILLFO'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillft',
            field=models.SmallIntegerField(null=True, db_column=b'JILLFT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillfw',
            field=models.SmallIntegerField(null=True, db_column=b'JILLFW'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillge',
            field=models.SmallIntegerField(null=True, db_column=b'JILLGE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillgf',
            field=models.SmallIntegerField(null=True, db_column=b'JILLGF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillgo',
            field=models.SmallIntegerField(null=True, db_column=b'JILLGO'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillgt',
            field=models.SmallIntegerField(null=True, db_column=b'JILLGT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillgw',
            field=models.SmallIntegerField(null=True, db_column=b'JILLGW'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jilloe',
            field=models.SmallIntegerField(null=True, db_column=b'JILLOE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillof',
            field=models.SmallIntegerField(null=True, db_column=b'JILLOF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillog',
            field=models.SmallIntegerField(null=True, db_column=b'JILLOG'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillot',
            field=models.SmallIntegerField(null=True, db_column=b'JILLOT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillow',
            field=models.SmallIntegerField(null=True, db_column=b'JILLOW'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillte',
            field=models.SmallIntegerField(null=True, db_column=b'JILLTE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jilltf',
            field=models.SmallIntegerField(null=True, db_column=b'JILLTF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jilltg',
            field=models.SmallIntegerField(null=True, db_column=b'JILLTG'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillto',
            field=models.SmallIntegerField(null=True, db_column=b'JILLTO'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jilltw',
            field=models.SmallIntegerField(null=True, db_column=b'JILLTW'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillwe',
            field=models.SmallIntegerField(null=True, db_column=b'JILLWE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillwf',
            field=models.SmallIntegerField(null=True, db_column=b'JILLWF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillwg',
            field=models.SmallIntegerField(null=True, db_column=b'JILLWG'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillwo',
            field=models.SmallIntegerField(null=True, db_column=b'JILLWO'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jillwt',
            field=models.SmallIntegerField(null=True, db_column=b'JILLWT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jpmovm',
            field=models.SmallIntegerField(null=True, db_column=b'JPMOVM'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jpmvyr',
            field=models.SmallIntegerField(null=True, db_column=b'JPMVYR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jwhkit',
            field=models.SmallIntegerField(null=True, db_column=b'JWHKIT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jwnfun',
            field=models.SmallIntegerField(null=True, db_column=b'JWNFUN'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='metro',
            field=models.SmallIntegerField(null=True, db_column=b'METRO'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='mobuse',
            field=models.SmallIntegerField(null=True, db_column=b'MOBUSE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='mold',
            field=models.SmallIntegerField(null=True, db_column=b'MOLD'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='moldbasem',
            field=models.SmallIntegerField(null=True, db_column=b'MOLDBASEM'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='moldbath',
            field=models.SmallIntegerField(null=True, db_column=b'MOLDBATH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='moldbedrm',
            field=models.SmallIntegerField(null=True, db_column=b'MOLDBEDRM'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='moldkitch',
            field=models.SmallIntegerField(null=True, db_column=b'MOLDKITCH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='moldlroom',
            field=models.SmallIntegerField(null=True, db_column=b'MOLDLROOM'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='moldother',
            field=models.SmallIntegerField(null=True, db_column=b'MOLDOTHER'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='monox',
            field=models.SmallIntegerField(null=True, db_column=b'MONOX'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='must',
            field=models.SmallIntegerField(null=True, db_column=b'MUST'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='natlflag',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'NATLFLAG'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='oldmsflg',
            field=models.SmallIntegerField(null=True, db_column=b'OLDMSFLG'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='outlet',
            field=models.SmallIntegerField(null=True, db_column=b'OUTLET'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='pmovm',
            field=models.SmallIntegerField(null=True, db_column=b'PMOVM'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='pmovyr',
            field=models.IntegerField(null=True, db_column=b'PMOVYR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='poolacc',
            field=models.SmallIntegerField(null=True, db_column=b'POOLACC'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='poolfen',
            field=models.SmallIntegerField(null=True, db_column=b'POOLFEN'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='safeu5kd',
            field=models.SmallIntegerField(null=True, db_column=b'SAFEU5KD'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='secsmk',
            field=models.SmallIntegerField(null=True, db_column=b'SECSMK'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='sewdistp',
            field=models.SmallIntegerField(null=True, db_column=b'SEWDISTP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='smkr',
            field=models.SmallIntegerField(null=True, db_column=b'SMKR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='smkvis',
            field=models.SmallIntegerField(null=True, db_column=b'SMKVIS'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='smoke',
            field=models.SmallIntegerField(null=True, db_column=b'SMOKE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='smokpwr',
            field=models.SmallIntegerField(null=True, db_column=b'SMOKPWR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='spothr',
            field=models.SmallIntegerField(null=True, db_column=b'SPOTHR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='sprnklr',
            field=models.SmallIntegerField(null=True, db_column=b'SPRNKLR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='stairbrk',
            field=models.SmallIntegerField(null=True, db_column=b'STAIRBRK'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='staircov',
            field=models.SmallIntegerField(null=True, db_column=b'STAIRCOV'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='stairgat',
            field=models.SmallIntegerField(null=True, db_column=b'STAIRGAT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='stairlgt',
            field=models.SmallIntegerField(null=True, db_column=b'STAIRLGT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='stairmis',
            field=models.SmallIntegerField(null=True, db_column=b'STAIRMIS'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='stairrl',
            field=models.SmallIntegerField(null=True, db_column=b'STAIRRL'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='stairs',
            field=models.SmallIntegerField(null=True, db_column=b'STAIRS'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='state',
            field=models.SmallIntegerField(null=True, db_column=b'STATE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='taxcrd',
            field=models.SmallIntegerField(null=True, db_column=b'TAXCRD'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='wchair',
            field=models.SmallIntegerField(null=True, db_column=b'WCHAIR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='welldis',
            field=models.SmallIntegerField(null=True, db_column=b'WELLDIS'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='welldis2',
            field=models.SmallIntegerField(null=True, db_column=b'WELLDIS2'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='wgtmetro',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'WGTMETRO'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='whkit',
            field=models.SmallIntegerField(null=True, db_column=b'WHKIT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='winterelsp',
            field=models.SmallIntegerField(null=True, db_column=b'WINTERELSP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='winterkesp',
            field=models.SmallIntegerField(null=True, db_column=b'WINTERKESP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='winternone',
            field=models.SmallIntegerField(null=True, db_column=b'WINTERNONE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='winteroven',
            field=models.SmallIntegerField(null=True, db_column=b'WINTEROVEN'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='winterwood',
            field=models.SmallIntegerField(null=True, db_column=b'WINTERWOOD'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='wnfun',
            field=models.SmallIntegerField(null=True, db_column=b'WNFUN'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='zone',
            field=models.PositiveIntegerField(null=True, db_column=b'ZONE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='cmsa',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'CMSA'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='date',
            field=models.IntegerField(null=True, db_column=b'DATE'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='division',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'DIVISION'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='metro3',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'METRO3'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='region',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'REGION'),
        ),
    ]
