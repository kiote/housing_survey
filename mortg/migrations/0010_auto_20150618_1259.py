# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mortg', '0009_auto_20150616_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mortg',
            name='addtn2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADDTN2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='addtn3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADDTN3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='addtns',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADDTNS'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='adjdep',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADJDEP'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='adjdep2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADJDEP2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='adjdep3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADJDEP3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='adjfix',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADJFIX'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='adjfix2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADJFIX2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='adjfix3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADJFIX3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='adjpm',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADJPM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='adjpm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADJPM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='adjpm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADJPM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='adjrtf',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADJRTF'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='adjrtf2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADJRTF2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='adjrtf3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ADJRTF3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ammort',
            field=models.IntegerField(default=-9, null=True, db_column=b'AMMORT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ammrt2',
            field=models.IntegerField(default=-9, null=True, db_column=b'AMMRT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ammrt3',
            field=models.IntegerField(default=-9, null=True, db_column=b'AMMRT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ammrt4',
            field=models.IntegerField(default=-9, null=True, db_column=b'AMMRT4'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='amrtz',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'AMRTZ'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='amrtz2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'AMRTZ2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='amrtz3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'AMRTZ3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='amtm',
            field=models.IntegerField(default=-9, null=True, db_column=b'AMTM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='amtm2',
            field=models.IntegerField(default=-9, null=True, db_column=b'AMTM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='amtm3',
            field=models.IntegerField(default=-9, null=True, db_column=b'AMTM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='arm',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ARM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='arm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ARM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='arm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ARM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='balamt',
            field=models.IntegerField(default=-9, null=True, db_column=b'BALAMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='balamt2',
            field=models.IntegerField(default=-9, null=True, db_column=b'BALAMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='balamt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'BALAMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='bank',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'BANK'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='bank2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'BANK2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='bank3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'BANK3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='bloon',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'BLOON'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='bloon2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'BLOON2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='bloon3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'BLOON3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='canvar',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'CANVAR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='canvr2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'CANVR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='canvr3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'CANVR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='cash',
            field=models.IntegerField(default=-9, null=True, db_column=b'CASH'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='cash2',
            field=models.IntegerField(default=-9, null=True, db_column=b'CASH2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='cash3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'CASH3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='doc',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'DOC'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='doc2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'DOC2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='doc3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'DOC3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='extln2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'EXTLN2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='extln3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'EXTLN3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='extlon',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'EXTLON'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='fixed',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'FIXED'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='fixed2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'FIXED2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='fixed3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'FIXED3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='fmrpmt',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'FMRPMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='fmrpmt2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'FMRPMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='fmrpmt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'FMRPMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='frstrm',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'FRSTRM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='frstrm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'FRSTRM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='frstrm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'FRSTRM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='fxdpm',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'FXDPM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='fxdpm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'FXDPM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='fxdpm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'FXDPM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='gpmwp',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'GPMWP'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='gpmwp2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'GPMWP2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='gpmwp3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'GPMWP3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='gtcas2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'GTCAS2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='gtcas3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'GTCAS3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='gtcash',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'GTCASH'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hebal1',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HEBAL1'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hebal2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HEBAL2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hebal3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HEBAL3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hebam1',
            field=models.IntegerField(default=-9, null=True, db_column=b'HEBAM1'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hebam2',
            field=models.IntegerField(default=-9, null=True, db_column=b'HEBAM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hebam3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HEBAM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hecr1',
            field=models.IntegerField(default=-9, null=True, db_column=b'HECR1'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hecr2',
            field=models.IntegerField(default=-9, null=True, db_column=b'HECR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hecr3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HECR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='heinf1',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HEINF1'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='heinf2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HEINF2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='heinf3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HEINF3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='heinr1',
            field=models.DecimalField(default=-9, null=True, decimal_places=10, max_digits=20, db_column=b'HEINR1'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='heinr2',
            field=models.DecimalField(default=-9, null=True, decimal_places=10, max_digits=20, db_column=b'HEINR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='heinr3',
            field=models.DecimalField(default=-9, null=True, decimal_places=10, max_digits=20, db_column=b'HEINR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='heinw1',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HEINW1'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='heinw2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HEINW2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='heinw3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HEINW3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hemnmor',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HEMNMOR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hemnmor2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HEMNMOR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hepmt1',
            field=models.IntegerField(default=-9, null=True, db_column=b'HEPMT1'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hepmt2',
            field=models.IntegerField(default=-9, null=True, db_column=b'HEPMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hepmt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HEPMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='heyrmor',
            field=models.IntegerField(default=-9, null=True, db_column=b'HEYRMOR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='heyrmor2',
            field=models.IntegerField(default=-9, null=True, db_column=b'HEYRMOR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='heyrmor3',
            field=models.IntegerField(default=-9, null=True, db_column=b'HEYRMOR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hybarm',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HYBARM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hybarm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HYBARM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hybarm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HYBARM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hybmyr',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HYBMYR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hybmyr2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HYBMYR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hybmyr3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'HYBMYR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='improv',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'IMPROV'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='imprv2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'IMPRV2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='imprv3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'IMPRV3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='incper',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INCPER'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='incpr2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INCPR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='incpr3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INCPR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='inpmt2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INPMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='inpmt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INPMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='inspm',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INSPM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='inspm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INSPM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='inspm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INSPM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='inspmt',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INSPMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intf',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INTF'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intf2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INTF2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intf3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INTF3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intpm',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INTPM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intpm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INTPM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intpm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INTPM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intpmt',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INTPMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intpmt2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INTPMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intpmt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INTPMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intr',
            field=models.DecimalField(default=-9, null=True, decimal_places=10, max_digits=20, db_column=b'INTR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intr2',
            field=models.DecimalField(default=-9, null=True, decimal_places=10, max_digits=20, db_column=b'INTR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intr3',
            field=models.DecimalField(default=-9, null=True, decimal_places=10, max_digits=20, db_column=b'INTR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intw',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INTW'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intw2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INTW2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='intw3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'INTW3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='io',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'IO'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='io2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'IO2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='io3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'IO3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jamrtz',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JAMRTZ'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jamtm',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JAMTM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jamtm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JAMTM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jamtm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JAMTM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='janvar',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JANVAR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='janvr2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JANVR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='janvr3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JANVR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jatbuy',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JATBUY'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jatby2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JATBY2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jatby3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JATBY3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jaxpmt',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JAXPMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jbank',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JBANK'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jbank2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JBANK2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jbank3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JBANK3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jblon2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JBLON2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jblon3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JBLON3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jbloon',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JBLOON'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jewmor',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JEWMOR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jewmr2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JEWMR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jewmr3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JEWMR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jhecr1',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JHECR1'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jintf',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JINTF'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jintf2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JINTF2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jintf3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JINTF3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jintw',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JINTW'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jintw2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JINTW2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jintw3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JINTW3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jmamt2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JMAMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jmamt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JMAMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jmiamt',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JMIAMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jmipmt',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JMIPMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jmmort',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JMMORT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jmmrt2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JMMRT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jmmrt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JMMRT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jmmrt4',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JMMRT4'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jmpmt2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JMPMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jmrtz2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JMRTZ2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jmrtz3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JMRTZ3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jnpmt2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JNPMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jnpmt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JNPMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jnspmt',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JNSPMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jortin',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JORTIN'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jortn2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JORTN2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jortn3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JORTN3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jpmt',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JPMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jpmt2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JPMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jpmt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JPMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jpmt4',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JPMT4'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jrefi',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JREFI'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jrefi2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JREFI2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jrmor2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JRMOR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jrmor3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JRMOR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jrtyp1',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JRTYP1'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jrtyp2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JRTYP2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jrtyp3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JRTYP3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jtcas2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JTCAS2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jtcas3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JTCAS3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jtcash',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JTCASH'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jterm',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JTERM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jterm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JTERM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jterm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JTERM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jthpmt',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JTHPMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jtpmt2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JTPMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jtpmt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JTPMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jubmor',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JUBMOR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jubmr2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JUBMR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='junpbal',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JUNPBAL'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='junpbal2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JUNPBAL2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='junpbal3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JUNPBAL3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='junpbal4',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JUNPBAL4'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jvary',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JVARY'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jvary2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JVARY2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jvary3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JVARY3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jxpmt2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JXPMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jxpmt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JXPMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='jyrmor',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'JYRMOR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='lenmod',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'LENMOD'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='lenmod2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'LENMOD2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='lenmod3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'LENMOD3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='lnfnbr',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'LNFNBR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='lnfnbr2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'LNFNBR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='lnfnbr3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'LNFNBR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='looncl',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'LOONCL'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='looncl2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'LOONCL2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='looncl3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'LOONCL3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='lowin2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'LOWIN2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='lowin3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'LOWIN3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='lowint',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'LOWINT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='matbuy',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MATBUY'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='matby2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MATBY2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='matby3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MATBY3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='maxadj',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MAXADJ'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='maxadj2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MAXADJ2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='maxadj3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MAXADJ3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mgresa',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MGRESA'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mgresa2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MGRESA2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mgresa3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MGRESA3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='minpm',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MINPM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='minpm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MINPM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='minpm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MINPM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlncls',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNCLS'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlncls2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNCLS2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlncls3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNCLS3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlndwn',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNDWN'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlndwn2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNDWN2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlndwn3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNDWN3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlnint',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNINT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlnint2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNINT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlnint3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNINT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlnoth',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNOTH'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlnoth2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNOTH2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlnoth3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNOTH3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlnpm',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNPM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlnpm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNPM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mlnpm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MLNPM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mnmor',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MNMOR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mnmor2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MNMOR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mnmor3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MNMOR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mortin',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MORTIN'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mortn2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MORTN2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mortn3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MORTN3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mrtyp1',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MRTYP1'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mrtyp2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MRTYP2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mrtyp3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MRTYP3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mxdjtm',
            field=models.IntegerField(default=-9, null=True, db_column=b'MXDJTM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mxdjtm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MXDJTM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mxdjtm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MXDJTM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mxintf',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MXINTF'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mxintf2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MXINTF2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mxintf3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MXINTF3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mxintr',
            field=models.DecimalField(default=-9, null=True, decimal_places=10, max_digits=20, db_column=b'MXINTR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mxintr2',
            field=models.DecimalField(default=-9, null=True, decimal_places=10, max_digits=20, db_column=b'MXINTR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mxintr3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MXINTR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mxintw',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MXINTW'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mxintw2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MXINTW2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mxintw3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'MXINTW3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='newmor',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'NEWMOR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='newmr2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'NEWMR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='newmr3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'NEWMR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='orintf',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ORINTF'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='orintf2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ORINTF2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='orintf3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ORINTF3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='orintr',
            field=models.DecimalField(default=-9, null=True, decimal_places=10, max_digits=20, db_column=b'ORINTR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='orintr2',
            field=models.DecimalField(default=-9, null=True, decimal_places=10, max_digits=20, db_column=b'ORINTR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='orintr3',
            field=models.DecimalField(default=-9, null=True, decimal_places=10, max_digits=20, db_column=b'ORINTR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='orintw',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ORINTW'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='orintw2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ORINTW2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='orintw3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'ORINTW3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='othpmt',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'OTHPMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='othref',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'OTHREF'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='otpmt2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'OTPMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='otpmt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'OTPMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='otref2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'OTREF2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='otref3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'OTREF3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='otrpm',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'OTRPM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='otrpm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'OTRPM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='otrpm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'OTRPM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='perus1',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PERUS1'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='perus2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PERUS2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='perus3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PERUS3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmamt2',
            field=models.IntegerField(default=-9, null=True, db_column=b'PMAMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmamt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PMAMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmiamt',
            field=models.IntegerField(default=-9, null=True, db_column=b'PMIAMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmipmt',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PMIPMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmpmt2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PMPMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmpmt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PMPMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmt',
            field=models.IntegerField(default=-9, null=True, db_column=b'PMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmt2',
            field=models.IntegerField(default=-9, null=True, db_column=b'PMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmt3',
            field=models.IntegerField(default=-9, null=True, db_column=b'PMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmt4',
            field=models.IntegerField(default=-9, null=True, db_column=b'PMT4'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmtinc',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PMTINC'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmtinc2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PMTINC2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmtinc3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PMTINC3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pripmt',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PRIPMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pripmt2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PRIPMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pripmt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PRIPMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ptcham',
            field=models.IntegerField(default=-9, null=True, db_column=b'PTCHAM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ptcham2',
            field=models.IntegerField(default=-9, null=True, db_column=b'PTCHAM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ptcham3',
            field=models.IntegerField(default=-9, null=True, db_column=b'PTCHAM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ptchyr',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PTCHYR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ptchyr2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PTCHYR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ptchyr3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'PTCHYR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ratepm',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'RATEPM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ratepm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'RATEPM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ratepm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'RATEPM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='redmo2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'REDMO2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='redmo3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'REDMO3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='redmon',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'REDMON'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='redpa2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'REDPA2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='redpa3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'REDPA3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='redpay',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'REDPAY'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='refi',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'REFI'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='refi2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'REFI2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='refi3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'REFI3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='sell',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'SELL'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='sell2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'SELL2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='sell3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'SELL3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='shock',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'SHOCK'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='shock2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'SHOCK2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='shock3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'SHOCK3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='submor',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'SUBMOR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='submr2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'SUBMR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='submr3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'SUBMR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='submr4',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'SUBMR4'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='taxpmt',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'TAXPMT'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='term',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'TERM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='term2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'TERM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='term3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'TERM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='timbom',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'TIMBOM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='timbom2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'TIMBOM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='timbom3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'TIMBOM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='txpmt2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'TXPMT2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='txpmt3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'TXPMT3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='unpbal',
            field=models.IntegerField(default=-9, null=True, db_column=b'UNPBAL'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='unpbal2',
            field=models.IntegerField(default=-9, null=True, db_column=b'UNPBAL2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='unpbal3',
            field=models.IntegerField(default=-9, null=True, db_column=b'UNPBAL3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='unpbal4',
            field=models.IntegerField(default=-9, null=True, db_column=b'UNPBAL4'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='varm',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'VARM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='varm2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'VARM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='varm3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'VARM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='vary',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'VARY'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='vary2',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'VARY2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='vary3',
            field=models.SmallIntegerField(default=-9, null=True, db_column=b'VARY3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='yrmor',
            field=models.IntegerField(default=-9, null=True, db_column=b'YRMOR'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='yrmor2',
            field=models.IntegerField(default=-9, null=True, db_column=b'YRMOR2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='yrmor3',
            field=models.IntegerField(default=-9, null=True, db_column=b'YRMOR3'),
        ),
    ]
