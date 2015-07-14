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
            name='aptch',
            field=models.SmallIntegerField(null=True, db_column=b'APTCH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='badstep',
            field=models.SmallIntegerField(null=True, db_column=b'BADSTEP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='changedrecord',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'ChangedRecord'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='crimea',
            field=models.SmallIntegerField(null=True, db_column=b'CRIMEA'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='crimeb',
            field=models.SmallIntegerField(null=True, db_column=b'CRIMEB'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='crimec',
            field=models.SmallIntegerField(null=True, db_column=b'CRIMEC'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='dafur',
            field=models.SmallIntegerField(null=True, db_column=b'DAFUR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='dcokst',
            field=models.SmallIntegerField(null=True, db_column=b'DCOKST'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='delect',
            field=models.SmallIntegerField(null=True, db_column=b'DELECT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='dflot',
            field=models.SmallIntegerField(null=True, db_column=b'DFLOT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='dfrpl',
            field=models.SmallIntegerField(null=True, db_column=b'dfrpl'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='dfrpli',
            field=models.SmallIntegerField(null=True, db_column=b'dfrpli'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='dhoth',
            field=models.SmallIntegerField(null=True, db_column=b'DHOTH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='dhpmp',
            field=models.SmallIntegerField(null=True, db_column=b'DHPMP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='dplf',
            field=models.SmallIntegerField(null=True, db_column=b'DPLF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='dsteam',
            field=models.SmallIntegerField(null=True, db_column=b'DSTEAM'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='dstove',
            field=models.SmallIntegerField(null=True, db_column=b'DSTOVE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='fafur',
            field=models.SmallIntegerField(null=True, db_column=b'FAFUR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='fcokst',
            field=models.SmallIntegerField(null=True, db_column=b'FCOKST'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='felect',
            field=models.SmallIntegerField(null=True, db_column=b'FELECT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='fflin',
            field=models.SmallIntegerField(null=True, db_column=b'FFLIN'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='fflot',
            field=models.SmallIntegerField(null=True, db_column=b'FFLOT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='ffrpl',
            field=models.SmallIntegerField(null=True, db_column=b'ffrpl'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='ffrpli',
            field=models.SmallIntegerField(null=True, db_column=b'ffrpli'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='fhoth',
            field=models.SmallIntegerField(null=True, db_column=b'FHOTH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='fhpmp',
            field=models.SmallIntegerField(null=True, db_column=b'FHPMP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='fplf',
            field=models.SmallIntegerField(null=True, db_column=b'FPLF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='fporth',
            field=models.SmallIntegerField(null=True, db_column=b'FPORTH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='fsteam',
            field=models.SmallIntegerField(null=True, db_column=b'FSTEAM'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='fstove',
            field=models.SmallIntegerField(null=True, db_column=b'FSTOVE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jdafur',
            field=models.SmallIntegerField(null=True, db_column=b'JDAFUR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jdcook',
            field=models.SmallIntegerField(null=True, db_column=b'JDCOOK'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jdelec',
            field=models.SmallIntegerField(null=True, db_column=b'JDELEC'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jdflot',
            field=models.SmallIntegerField(null=True, db_column=b'JDFLOT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jdfpli',
            field=models.SmallIntegerField(null=True, db_column=b'JDFPLI'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jdfrpl',
            field=models.SmallIntegerField(null=True, db_column=b'JDFRPL'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jdhoth',
            field=models.SmallIntegerField(null=True, db_column=b'JDHOTH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jdhpmp',
            field=models.SmallIntegerField(null=True, db_column=b'JDHPMP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jdplf',
            field=models.SmallIntegerField(null=True, db_column=b'JDPLF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jdstea',
            field=models.SmallIntegerField(null=True, db_column=b'JDSTEA'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jdstov',
            field=models.SmallIntegerField(null=True, db_column=b'JDSTOV'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jfafur',
            field=models.SmallIntegerField(null=True, db_column=b'JFAFUR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jfcook',
            field=models.SmallIntegerField(null=True, db_column=b'JFCOOK'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jfelec',
            field=models.SmallIntegerField(null=True, db_column=b'JFELEC'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jfflin',
            field=models.SmallIntegerField(null=True, db_column=b'JFFLIN'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jfflot',
            field=models.SmallIntegerField(null=True, db_column=b'JFFLOT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jffpli',
            field=models.SmallIntegerField(null=True, db_column=b'JFFPLI'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jffrpl',
            field=models.SmallIntegerField(null=True, db_column=b'JFFRPL'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jfhoth',
            field=models.SmallIntegerField(null=True, db_column=b'JFHOTH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jfhpmp',
            field=models.SmallIntegerField(null=True, db_column=b'JFHPMP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jfplf',
            field=models.SmallIntegerField(null=True, db_column=b'JFPLF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jfporh',
            field=models.SmallIntegerField(null=True, db_column=b'JFPORH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jfstea',
            field=models.SmallIntegerField(null=True, db_column=b'JFSTEA'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jfstov',
            field=models.SmallIntegerField(null=True, db_column=b'JFSTOV'),
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
            name='jsflin',
            field=models.SmallIntegerField(null=True, db_column=b'JSFLIN'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='jsporh',
            field=models.SmallIntegerField(null=True, db_column=b'JSPORH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='ltsok',
            field=models.SmallIntegerField(null=True, db_column=b'LTSOK'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='odora',
            field=models.SmallIntegerField(null=True, db_column=b'ODORA'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='odorb',
            field=models.SmallIntegerField(null=True, db_column=b'ODORB'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='odorc',
            field=models.SmallIntegerField(null=True, db_column=b'ODORC'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='pafur',
            field=models.SmallIntegerField(null=True, db_column=b'PAFUR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='pcokst',
            field=models.SmallIntegerField(null=True, db_column=b'PCOKST'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='pelect',
            field=models.SmallIntegerField(null=True, db_column=b'PELECT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='pflot',
            field=models.SmallIntegerField(null=True, db_column=b'PFLOT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='pfrpl',
            field=models.SmallIntegerField(null=True, db_column=b'pfrpl'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='pfrpli',
            field=models.SmallIntegerField(null=True, db_column=b'pfrpli'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='photh',
            field=models.SmallIntegerField(null=True, db_column=b'PHOTH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='phpmp',
            field=models.SmallIntegerField(null=True, db_column=b'PHPMP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='pplf',
            field=models.SmallIntegerField(null=True, db_column=b'PPLF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='psteam',
            field=models.SmallIntegerField(null=True, db_column=b'PSTEAM'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='pstove',
            field=models.SmallIntegerField(null=True, db_column=b'PSTOVE'),
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
        migrations.AddField(
            model_name='newhouse',
            name='railok',
            field=models.SmallIntegerField(null=True, db_column=b'RAILOK'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='repha',
            field=models.SmallIntegerField(null=True, db_column=b'REPHA'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='safur',
            field=models.SmallIntegerField(null=True, db_column=b'SAFUR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='scoal',
            field=models.SmallIntegerField(null=True, db_column=b'scoal'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='scokst',
            field=models.SmallIntegerField(null=True, db_column=b'SCOKST'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='select',
            field=models.SmallIntegerField(null=True, db_column=b'SELECT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='sflin',
            field=models.SmallIntegerField(null=True, db_column=b'sflin'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='sflot',
            field=models.SmallIntegerField(null=True, db_column=b'SFLOT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='sfrpl',
            field=models.SmallIntegerField(null=True, db_column=b'sfrpl'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='sfrpli',
            field=models.SmallIntegerField(null=True, db_column=b'sfrpli'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='sgas',
            field=models.SmallIntegerField(null=True, db_column=b'sgas'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='shoth',
            field=models.SmallIntegerField(null=True, db_column=b'SHOTH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='shpmp',
            field=models.SmallIntegerField(null=True, db_column=b'SHPMP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='sjuice',
            field=models.SmallIntegerField(null=True, db_column=b'sjuice'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='skero',
            field=models.SmallIntegerField(null=True, db_column=b'skero'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='soil',
            field=models.SmallIntegerField(null=True, db_column=b'soil'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='sother',
            field=models.SmallIntegerField(null=True, db_column=b'sother'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='splf',
            field=models.SmallIntegerField(null=True, db_column=b'SPLF'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='sporth',
            field=models.SmallIntegerField(null=True, db_column=b'sporth'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='ssteam',
            field=models.SmallIntegerField(null=True, db_column=b'SSTEAM'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='sstove',
            field=models.SmallIntegerField(null=True, db_column=b'SSTOVE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='ssun',
            field=models.SmallIntegerField(null=True, db_column=b'ssun'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='strna',
            field=models.SmallIntegerField(null=True, db_column=b'STRNA'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='strnb',
            field=models.SmallIntegerField(null=True, db_column=b'STRNB'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='strnc',
            field=models.SmallIntegerField(null=True, db_column=b'STRNC'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='swood',
            field=models.SmallIntegerField(null=True, db_column=b'swood'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='trn',
            field=models.SmallIntegerField(null=True, db_column=b'TRN'),
        ),
    ]
