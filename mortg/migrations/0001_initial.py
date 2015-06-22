# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mortg',
            fields=[
                ('control', models.BigIntegerField(unique=True, serialize=False, primary_key=True, db_column=b'CONTROL')),
                ('addtn2', models.SmallIntegerField(null=True, db_column=b'ADDTN2')),
                ('addtn3', models.SmallIntegerField(null=True, db_column=b'ADDTN3')),
                ('addtns', models.SmallIntegerField(null=True, db_column=b'ADDTNS')),
                ('adjdep', models.SmallIntegerField(null=True, db_column=b'ADJDEP')),
                ('adjdep2', models.SmallIntegerField(null=True, db_column=b'ADJDEP2')),
                ('adjdep3', models.SmallIntegerField(null=True, db_column=b'ADJDEP3')),
                ('adjfix', models.SmallIntegerField(null=True, db_column=b'ADJFIX')),
                ('adjfix2', models.SmallIntegerField(null=True, db_column=b'ADJFIX2')),
                ('adjfix3', models.SmallIntegerField(null=True, db_column=b'ADJFIX3')),
                ('adjpm', models.SmallIntegerField(null=True, db_column=b'ADJPM')),
                ('adjpm2', models.SmallIntegerField(null=True, db_column=b'ADJPM2')),
                ('adjpm3', models.SmallIntegerField(null=True, db_column=b'ADJPM3')),
                ('adjrtf', models.SmallIntegerField(null=True, db_column=b'ADJRTF')),
                ('adjrtf2', models.SmallIntegerField(null=True, db_column=b'ADJRTF2')),
                ('adjrtf3', models.SmallIntegerField(null=True, db_column=b'ADJRTF3')),
                ('ammort', models.IntegerField(null=True, db_column=b'AMMORT')),
                ('ammrt2', models.IntegerField(null=True, db_column=b'AMMRT2')),
                ('ammrt3', models.IntegerField(null=True, db_column=b'AMMRT3')),
                ('ammrt4', models.IntegerField(null=True, db_column=b'AMMRT4')),
                ('amrtz', models.SmallIntegerField(null=True, db_column=b'AMRTZ')),
                ('amrtz2', models.SmallIntegerField(null=True, db_column=b'AMRTZ2')),
                ('amrtz3', models.SmallIntegerField(null=True, db_column=b'AMRTZ3')),
                ('amtm', models.IntegerField(null=True, db_column=b'AMTM')),
                ('amtm2', models.IntegerField(null=True, db_column=b'AMTM2')),
                ('amtm3', models.IntegerField(null=True, db_column=b'AMTM3')),
                ('arm', models.SmallIntegerField(null=True, db_column=b'ARM')),
                ('arm2', models.SmallIntegerField(null=True, db_column=b'ARM2')),
                ('arm3', models.SmallIntegerField(null=True, db_column=b'ARM3')),
                ('balamt', models.IntegerField(null=True, db_column=b'BALAMT')),
                ('balamt2', models.IntegerField(null=True, db_column=b'BALAMT2')),
                ('balamt3', models.SmallIntegerField(null=True, db_column=b'BALAMT3')),
                ('bank', models.SmallIntegerField(null=True, db_column=b'BANK')),
                ('bank2', models.SmallIntegerField(null=True, db_column=b'BANK2')),
                ('bank3', models.SmallIntegerField(null=True, db_column=b'BANK3')),
                ('bloon', models.SmallIntegerField(null=True, db_column=b'BLOON')),
                ('bloon2', models.SmallIntegerField(null=True, db_column=b'BLOON2')),
                ('bloon3', models.SmallIntegerField(null=True, db_column=b'BLOON3')),
                ('canvar', models.SmallIntegerField(null=True, db_column=b'CANVAR')),
                ('canvr2', models.SmallIntegerField(null=True, db_column=b'CANVR2')),
                ('canvr3', models.SmallIntegerField(null=True, db_column=b'CANVR3')),
                ('cash', models.IntegerField(null=True, db_column=b'CASH')),
                ('cash2', models.IntegerField(null=True, db_column=b'CASH2')),
                ('cash3', models.SmallIntegerField(null=True, db_column=b'CASH3')),
                ('doc', models.SmallIntegerField(null=True, db_column=b'DOC')),
                ('doc2', models.SmallIntegerField(null=True, db_column=b'DOC2')),
                ('doc3', models.SmallIntegerField(null=True, db_column=b'DOC3')),
                ('extln2', models.SmallIntegerField(null=True, db_column=b'EXTLN2')),
                ('extln3', models.SmallIntegerField(null=True, db_column=b'EXTLN3')),
                ('extlon', models.SmallIntegerField(null=True, db_column=b'EXTLON')),
                ('fixed', models.SmallIntegerField(null=True, db_column=b'FIXED')),
                ('fixed2', models.SmallIntegerField(null=True, db_column=b'FIXED2')),
                ('fixed3', models.SmallIntegerField(null=True, db_column=b'FIXED3')),
                ('fmrpmt', models.SmallIntegerField(null=True, db_column=b'FMRPMT')),
                ('fmrpmt2', models.SmallIntegerField(null=True, db_column=b'FMRPMT2')),
                ('fmrpmt3', models.SmallIntegerField(null=True, db_column=b'FMRPMT3')),
                ('frstrm', models.SmallIntegerField(null=True, db_column=b'FRSTRM')),
                ('frstrm2', models.SmallIntegerField(null=True, db_column=b'FRSTRM2')),
                ('frstrm3', models.SmallIntegerField(null=True, db_column=b'FRSTRM3')),
                ('fxdpm', models.SmallIntegerField(null=True, db_column=b'FXDPM')),
                ('fxdpm2', models.SmallIntegerField(null=True, db_column=b'FXDPM2')),
                ('fxdpm3', models.SmallIntegerField(null=True, db_column=b'FXDPM3')),
                ('gpmwp', models.SmallIntegerField(null=True, db_column=b'GPMWP')),
                ('gpmwp2', models.SmallIntegerField(null=True, db_column=b'GPMWP2')),
                ('gpmwp3', models.SmallIntegerField(null=True, db_column=b'GPMWP3')),
                ('gtcas2', models.SmallIntegerField(null=True, db_column=b'GTCAS2')),
                ('gtcas3', models.SmallIntegerField(null=True, db_column=b'GTCAS3')),
                ('gtcash', models.SmallIntegerField(null=True, db_column=b'GTCASH')),
                ('hebal1', models.SmallIntegerField(null=True, db_column=b'HEBAL1')),
                ('hebal2', models.SmallIntegerField(null=True, db_column=b'HEBAL2')),
                ('hebal3', models.SmallIntegerField(null=True, db_column=b'HEBAL3')),
                ('hebam1', models.IntegerField(null=True, db_column=b'HEBAM1')),
                ('hebam2', models.IntegerField(null=True, db_column=b'HEBAM2')),
                ('hebam3', models.SmallIntegerField(null=True, db_column=b'HEBAM3')),
                ('hecr1', models.IntegerField(null=True, db_column=b'HECR1')),
                ('hecr2', models.IntegerField(null=True, db_column=b'HECR2')),
                ('hecr3', models.SmallIntegerField(null=True, db_column=b'HECR3')),
                ('heinf1', models.SmallIntegerField(null=True, db_column=b'HEINF1')),
                ('heinf2', models.SmallIntegerField(null=True, db_column=b'HEINF2')),
                ('heinf3', models.SmallIntegerField(null=True, db_column=b'HEINF3')),
                ('heinr1', models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'HEINR1')),
                ('heinr2', models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'HEINR2')),
                ('heinr3', models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'HEINR3')),
                ('heinw1', models.SmallIntegerField(null=True, db_column=b'HEINW1')),
                ('heinw2', models.SmallIntegerField(null=True, db_column=b'HEINW2')),
                ('heinw3', models.SmallIntegerField(null=True, db_column=b'HEINW3')),
                ('hemnmor', models.SmallIntegerField(null=True, db_column=b'HEMNMOR')),
                ('hemnmor2', models.SmallIntegerField(null=True, db_column=b'HEMNMOR2')),
                ('hepmt1', models.IntegerField(null=True, db_column=b'HEPMT1')),
                ('hepmt2', models.IntegerField(null=True, db_column=b'HEPMT2')),
                ('hepmt3', models.SmallIntegerField(null=True, db_column=b'HEPMT3')),
                ('heyrmor', models.IntegerField(null=True, db_column=b'HEYRMOR')),
                ('heyrmor2', models.IntegerField(null=True, db_column=b'HEYRMOR2')),
                ('heyrmor3', models.IntegerField(null=True, db_column=b'HEYRMOR3')),
                ('hybarm', models.SmallIntegerField(null=True, db_column=b'HYBARM')),
                ('hybarm2', models.SmallIntegerField(null=True, db_column=b'HYBARM2')),
                ('hybarm3', models.SmallIntegerField(null=True, db_column=b'HYBARM3')),
                ('hybmyr', models.SmallIntegerField(null=True, db_column=b'HYBMYR')),
                ('hybmyr2', models.SmallIntegerField(null=True, db_column=b'HYBMYR2')),
                ('hybmyr3', models.SmallIntegerField(null=True, db_column=b'HYBMYR3')),
                ('improv', models.SmallIntegerField(null=True, db_column=b'IMPROV')),
                ('imprv2', models.SmallIntegerField(null=True, db_column=b'IMPRV2')),
                ('imprv3', models.SmallIntegerField(null=True, db_column=b'IMPRV3')),
                ('incper', models.SmallIntegerField(null=True, db_column=b'INCPER')),
                ('incpr2', models.SmallIntegerField(null=True, db_column=b'INCPR2')),
                ('incpr3', models.SmallIntegerField(null=True, db_column=b'INCPR3')),
                ('inpmt2', models.SmallIntegerField(null=True, db_column=b'INPMT2')),
                ('inpmt3', models.SmallIntegerField(null=True, db_column=b'INPMT3')),
                ('inspm', models.SmallIntegerField(null=True, db_column=b'INSPM')),
                ('inspm2', models.SmallIntegerField(null=True, db_column=b'INSPM2')),
                ('inspm3', models.SmallIntegerField(null=True, db_column=b'INSPM3')),
                ('inspmt', models.SmallIntegerField(null=True, db_column=b'INSPMT')),
                ('intf', models.SmallIntegerField(null=True, db_column=b'INTF')),
                ('intf2', models.SmallIntegerField(null=True, db_column=b'INTF2')),
                ('intf3', models.SmallIntegerField(null=True, db_column=b'INTF3')),
                ('intpm', models.SmallIntegerField(null=True, db_column=b'INTPM')),
                ('intpm2', models.SmallIntegerField(null=True, db_column=b'INTPM2')),
                ('intpm3', models.SmallIntegerField(null=True, db_column=b'INTPM3')),
                ('intpmt', models.SmallIntegerField(null=True, db_column=b'INTPMT')),
                ('intpmt2', models.SmallIntegerField(null=True, db_column=b'INTPMT2')),
                ('intpmt3', models.SmallIntegerField(null=True, db_column=b'INTPMT3')),
                ('intr', models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'INTR')),
                ('intr2', models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'INTR2')),
                ('intr3', models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'INTR3')),
                ('intw', models.SmallIntegerField(null=True, db_column=b'INTW')),
                ('intw2', models.SmallIntegerField(null=True, db_column=b'INTW2')),
                ('intw3', models.SmallIntegerField(null=True, db_column=b'INTW3')),
                ('io', models.SmallIntegerField(null=True, db_column=b'IO')),
                ('io2', models.SmallIntegerField(null=True, db_column=b'IO2')),
                ('io3', models.SmallIntegerField(null=True, db_column=b'IO3')),
                ('jamrtz', models.SmallIntegerField(null=True, db_column=b'JAMRTZ')),
                ('jamtm', models.SmallIntegerField(null=True, db_column=b'JAMTM')),
                ('jamtm2', models.SmallIntegerField(null=True, db_column=b'JAMTM2')),
                ('jamtm3', models.SmallIntegerField(null=True, db_column=b'JAMTM3')),
                ('janvar', models.SmallIntegerField(null=True, db_column=b'JANVAR')),
                ('janvr2', models.SmallIntegerField(null=True, db_column=b'JANVR2')),
                ('janvr3', models.SmallIntegerField(null=True, db_column=b'JANVR3')),
                ('jatbuy', models.SmallIntegerField(null=True, db_column=b'JATBUY')),
                ('jatby2', models.SmallIntegerField(null=True, db_column=b'JATBY2')),
                ('jatby3', models.SmallIntegerField(null=True, db_column=b'JATBY3')),
                ('jaxpmt', models.SmallIntegerField(null=True, db_column=b'JAXPMT')),
                ('jbank', models.SmallIntegerField(null=True, db_column=b'JBANK')),
                ('jbank2', models.SmallIntegerField(null=True, db_column=b'JBANK2')),
                ('jbank3', models.SmallIntegerField(null=True, db_column=b'JBANK3')),
                ('jblon2', models.SmallIntegerField(null=True, db_column=b'JBLON2')),
                ('jblon3', models.SmallIntegerField(null=True, db_column=b'JBLON3')),
                ('jbloon', models.SmallIntegerField(null=True, db_column=b'JBLOON')),
                ('jewmor', models.SmallIntegerField(null=True, db_column=b'JEWMOR')),
                ('jewmr2', models.SmallIntegerField(null=True, db_column=b'JEWMR2')),
                ('jewmr3', models.SmallIntegerField(null=True, db_column=b'JEWMR3')),
                ('jhecr1', models.SmallIntegerField(null=True, db_column=b'JHECR1')),
                ('jintf', models.SmallIntegerField(null=True, db_column=b'JINTF')),
                ('jintf2', models.SmallIntegerField(null=True, db_column=b'JINTF2')),
                ('jintf3', models.SmallIntegerField(null=True, db_column=b'JINTF3')),
                ('jintw', models.SmallIntegerField(null=True, db_column=b'JINTW')),
                ('jintw2', models.SmallIntegerField(null=True, db_column=b'JINTW2')),
                ('jintw3', models.SmallIntegerField(null=True, db_column=b'JINTW3')),
                ('jmamt2', models.SmallIntegerField(null=True, db_column=b'JMAMT2')),
                ('jmamt3', models.SmallIntegerField(null=True, db_column=b'JMAMT3')),
                ('jmiamt', models.SmallIntegerField(null=True, db_column=b'JMIAMT')),
                ('jmipmt', models.SmallIntegerField(null=True, db_column=b'JMIPMT')),
                ('jmmort', models.SmallIntegerField(null=True, db_column=b'JMMORT')),
                ('jmmrt2', models.SmallIntegerField(null=True, db_column=b'JMMRT2')),
                ('jmmrt3', models.SmallIntegerField(null=True, db_column=b'JMMRT3')),
                ('jmmrt4', models.SmallIntegerField(null=True, db_column=b'JMMRT4')),
                ('jmpmt2', models.SmallIntegerField(null=True, db_column=b'JMPMT2')),
                ('jmrtz2', models.SmallIntegerField(null=True, db_column=b'JMRTZ2')),
                ('jmrtz3', models.SmallIntegerField(null=True, db_column=b'JMRTZ3')),
                ('jnpmt2', models.SmallIntegerField(null=True, db_column=b'JNPMT2')),
                ('jnpmt3', models.SmallIntegerField(null=True, db_column=b'JNPMT3')),
                ('jnspmt', models.SmallIntegerField(null=True, db_column=b'JNSPMT')),
                ('jortin', models.SmallIntegerField(null=True, db_column=b'JORTIN')),
                ('jortn2', models.SmallIntegerField(null=True, db_column=b'JORTN2')),
                ('jortn3', models.SmallIntegerField(null=True, db_column=b'JORTN3')),
                ('jpmt', models.SmallIntegerField(null=True, db_column=b'JPMT')),
                ('jpmt2', models.SmallIntegerField(null=True, db_column=b'JPMT2')),
                ('jpmt3', models.SmallIntegerField(null=True, db_column=b'JPMT3')),
                ('jpmt4', models.SmallIntegerField(null=True, db_column=b'JPMT4')),
                ('jrefi', models.SmallIntegerField(null=True, db_column=b'JREFI')),
                ('jrefi2', models.SmallIntegerField(null=True, db_column=b'JREFI2')),
                ('jrmor2', models.SmallIntegerField(null=True, db_column=b'JRMOR2')),
                ('jrmor3', models.SmallIntegerField(null=True, db_column=b'JRMOR3')),
                ('jrtyp1', models.SmallIntegerField(null=True, db_column=b'JRTYP1')),
                ('jrtyp2', models.SmallIntegerField(null=True, db_column=b'JRTYP2')),
                ('jrtyp3', models.SmallIntegerField(null=True, db_column=b'JRTYP3')),
                ('jtcas2', models.SmallIntegerField(null=True, db_column=b'JTCAS2')),
                ('jtcas3', models.SmallIntegerField(null=True, db_column=b'JTCAS3')),
                ('jtcash', models.SmallIntegerField(null=True, db_column=b'JTCASH')),
                ('jterm', models.SmallIntegerField(null=True, db_column=b'JTERM')),
                ('jterm2', models.SmallIntegerField(null=True, db_column=b'JTERM2')),
                ('jterm3', models.SmallIntegerField(null=True, db_column=b'JTERM3')),
                ('jthpmt', models.SmallIntegerField(null=True, db_column=b'JTHPMT')),
                ('jtpmt2', models.SmallIntegerField(null=True, db_column=b'JTPMT2')),
                ('jtpmt3', models.SmallIntegerField(null=True, db_column=b'JTPMT3')),
                ('jubmor', models.SmallIntegerField(null=True, db_column=b'JUBMOR')),
                ('jubmr2', models.SmallIntegerField(null=True, db_column=b'JUBMR2')),
                ('junpbal', models.SmallIntegerField(null=True, db_column=b'JUNPBAL')),
                ('junpbal2', models.SmallIntegerField(null=True, db_column=b'JUNPBAL2')),
                ('junpbal3', models.SmallIntegerField(null=True, db_column=b'JUNPBAL3')),
                ('junpbal4', models.SmallIntegerField(null=True, db_column=b'JUNPBAL4')),
                ('jvary', models.SmallIntegerField(null=True, db_column=b'JVARY')),
                ('jvary2', models.SmallIntegerField(null=True, db_column=b'JVARY2')),
                ('jvary3', models.SmallIntegerField(null=True, db_column=b'JVARY3')),
                ('jxpmt2', models.SmallIntegerField(null=True, db_column=b'JXPMT2')),
                ('jxpmt3', models.SmallIntegerField(null=True, db_column=b'JXPMT3')),
                ('jyrmor', models.SmallIntegerField(null=True, db_column=b'JYRMOR')),
                ('lenmod', models.SmallIntegerField(null=True, db_column=b'LENMOD')),
                ('lenmod2', models.SmallIntegerField(null=True, db_column=b'LENMOD2')),
                ('lenmod3', models.SmallIntegerField(null=True, db_column=b'LENMOD3')),
                ('lnfnbr', models.SmallIntegerField(null=True, db_column=b'LNFNBR')),
                ('lnfnbr2', models.SmallIntegerField(null=True, db_column=b'LNFNBR2')),
                ('lnfnbr3', models.SmallIntegerField(null=True, db_column=b'LNFNBR3')),
                ('looncl', models.SmallIntegerField(null=True, db_column=b'LOONCL')),
                ('looncl2', models.SmallIntegerField(null=True, db_column=b'LOONCL2')),
                ('looncl3', models.SmallIntegerField(null=True, db_column=b'LOONCL3')),
                ('lowin2', models.SmallIntegerField(null=True, db_column=b'LOWIN2')),
                ('lowin3', models.SmallIntegerField(null=True, db_column=b'LOWIN3')),
                ('lowint', models.SmallIntegerField(null=True, db_column=b'LOWINT')),
                ('matbuy', models.SmallIntegerField(null=True, db_column=b'MATBUY')),
                ('matby2', models.SmallIntegerField(null=True, db_column=b'MATBY2')),
                ('matby3', models.SmallIntegerField(null=True, db_column=b'MATBY3')),
                ('maxadj', models.SmallIntegerField(null=True, db_column=b'MAXADJ')),
                ('maxadj2', models.SmallIntegerField(null=True, db_column=b'MAXADJ2')),
                ('maxadj3', models.SmallIntegerField(null=True, db_column=b'MAXADJ3')),
                ('mgresa', models.SmallIntegerField(null=True, db_column=b'MGRESA')),
                ('mgresa2', models.SmallIntegerField(null=True, db_column=b'MGRESA2')),
                ('mgresa3', models.SmallIntegerField(null=True, db_column=b'MGRESA3')),
                ('minpm', models.SmallIntegerField(null=True, db_column=b'MINPM')),
                ('minpm2', models.SmallIntegerField(null=True, db_column=b'MINPM2')),
                ('minpm3', models.SmallIntegerField(null=True, db_column=b'MINPM3')),
                ('mlncls', models.SmallIntegerField(null=True, db_column=b'MLNCLS')),
                ('mlncls2', models.SmallIntegerField(null=True, db_column=b'MLNCLS2')),
                ('mlncls3', models.SmallIntegerField(null=True, db_column=b'MLNCLS3')),
                ('mlndwn', models.SmallIntegerField(null=True, db_column=b'MLNDWN')),
                ('mlndwn2', models.SmallIntegerField(null=True, db_column=b'MLNDWN2')),
                ('mlndwn3', models.SmallIntegerField(null=True, db_column=b'MLNDWN3')),
                ('mlnint', models.SmallIntegerField(null=True, db_column=b'MLNINT')),
                ('mlnint2', models.SmallIntegerField(null=True, db_column=b'MLNINT2')),
                ('mlnint3', models.SmallIntegerField(null=True, db_column=b'MLNINT3')),
                ('mlnoth', models.SmallIntegerField(null=True, db_column=b'MLNOTH')),
                ('mlnoth2', models.SmallIntegerField(null=True, db_column=b'MLNOTH2')),
                ('mlnoth3', models.SmallIntegerField(null=True, db_column=b'MLNOTH3')),
                ('mlnpm', models.SmallIntegerField(null=True, db_column=b'MLNPM')),
                ('mlnpm2', models.SmallIntegerField(null=True, db_column=b'MLNPM2')),
                ('mlnpm3', models.SmallIntegerField(null=True, db_column=b'MLNPM3')),
                ('mnmor', models.SmallIntegerField(null=True, db_column=b'MNMOR')),
                ('mnmor2', models.SmallIntegerField(null=True, db_column=b'MNMOR2')),
                ('mnmor3', models.SmallIntegerField(null=True, db_column=b'MNMOR3')),
                ('mortin', models.SmallIntegerField(null=True, db_column=b'MORTIN')),
                ('mortn2', models.SmallIntegerField(null=True, db_column=b'MORTN2')),
                ('mortn3', models.SmallIntegerField(null=True, db_column=b'MORTN3')),
                ('mrtyp1', models.SmallIntegerField(null=True, db_column=b'MRTYP1')),
                ('mrtyp2', models.SmallIntegerField(null=True, db_column=b'MRTYP2')),
                ('mrtyp3', models.SmallIntegerField(null=True, db_column=b'MRTYP3')),
                ('mxdjtm', models.IntegerField(null=True, db_column=b'MXDJTM')),
                ('mxdjtm2', models.SmallIntegerField(null=True, db_column=b'MXDJTM2')),
                ('mxdjtm3', models.SmallIntegerField(null=True, db_column=b'MXDJTM3')),
                ('mxintf', models.SmallIntegerField(null=True, db_column=b'MXINTF')),
                ('mxintf2', models.SmallIntegerField(null=True, db_column=b'MXINTF2')),
                ('mxintf3', models.SmallIntegerField(null=True, db_column=b'MXINTF3')),
                ('mxintr', models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'MXINTR')),
                ('mxintr2', models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'MXINTR2')),
                ('mxintr3', models.SmallIntegerField(null=True, db_column=b'MXINTR3')),
                ('mxintw', models.SmallIntegerField(null=True, db_column=b'MXINTW')),
                ('mxintw2', models.SmallIntegerField(null=True, db_column=b'MXINTW2')),
                ('mxintw3', models.SmallIntegerField(null=True, db_column=b'MXINTW3')),
                ('newmor', models.SmallIntegerField(null=True, db_column=b'NEWMOR')),
                ('newmr2', models.SmallIntegerField(null=True, db_column=b'NEWMR2')),
                ('newmr3', models.SmallIntegerField(null=True, db_column=b'NEWMR3')),
                ('orintf', models.SmallIntegerField(null=True, db_column=b'ORINTF')),
                ('orintf2', models.SmallIntegerField(null=True, db_column=b'ORINTF2')),
                ('orintf3', models.SmallIntegerField(null=True, db_column=b'ORINTF3')),
                ('orintr', models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'ORINTR')),
                ('orintr2', models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'ORINTR2')),
                ('orintr3', models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'ORINTR3')),
                ('orintw', models.SmallIntegerField(null=True, db_column=b'ORINTW')),
                ('orintw2', models.SmallIntegerField(null=True, db_column=b'ORINTW2')),
                ('orintw3', models.SmallIntegerField(null=True, db_column=b'ORINTW3')),
                ('othpmt', models.SmallIntegerField(null=True, db_column=b'OTHPMT')),
                ('othref', models.SmallIntegerField(null=True, db_column=b'OTHREF')),
                ('otpmt2', models.SmallIntegerField(null=True, db_column=b'OTPMT2')),
                ('otpmt3', models.SmallIntegerField(null=True, db_column=b'OTPMT3')),
                ('otref2', models.SmallIntegerField(null=True, db_column=b'OTREF2')),
                ('otref3', models.SmallIntegerField(null=True, db_column=b'OTREF3')),
                ('otrpm', models.SmallIntegerField(null=True, db_column=b'OTRPM')),
                ('otrpm2', models.SmallIntegerField(null=True, db_column=b'OTRPM2')),
                ('otrpm3', models.SmallIntegerField(null=True, db_column=b'OTRPM3')),
                ('perus1', models.SmallIntegerField(null=True, db_column=b'PERUS1')),
                ('perus2', models.SmallIntegerField(null=True, db_column=b'PERUS2')),
                ('perus3', models.SmallIntegerField(null=True, db_column=b'PERUS3')),
                ('pmamt2', models.IntegerField(null=True, db_column=b'PMAMT2')),
                ('pmamt3', models.SmallIntegerField(null=True, db_column=b'PMAMT3')),
                ('pmiamt', models.IntegerField(null=True, db_column=b'PMIAMT')),
                ('pmipmt', models.SmallIntegerField(null=True, db_column=b'PMIPMT')),
                ('pmpmt2', models.SmallIntegerField(null=True, db_column=b'PMPMT2')),
                ('pmpmt3', models.SmallIntegerField(null=True, db_column=b'PMPMT3')),
                ('pmt', models.IntegerField(null=True, db_column=b'PMT')),
                ('pmt2', models.IntegerField(null=True, db_column=b'PMT2')),
                ('pmt3', models.IntegerField(null=True, db_column=b'PMT3')),
                ('pmt4', models.IntegerField(null=True, db_column=b'PMT4')),
                ('pmtinc', models.SmallIntegerField(null=True, db_column=b'PMTINC')),
                ('pmtinc2', models.SmallIntegerField(null=True, db_column=b'PMTINC2')),
                ('pmtinc3', models.SmallIntegerField(null=True, db_column=b'PMTINC3')),
                ('pripmt', models.SmallIntegerField(null=True, db_column=b'PRIPMT')),
                ('pripmt2', models.SmallIntegerField(null=True, db_column=b'PRIPMT2')),
                ('pripmt3', models.SmallIntegerField(null=True, db_column=b'PRIPMT3')),
                ('ptcham', models.IntegerField(null=True, db_column=b'PTCHAM')),
                ('ptcham2', models.IntegerField(null=True, db_column=b'PTCHAM2')),
                ('ptcham3', models.IntegerField(null=True, db_column=b'PTCHAM3')),
                ('ptchyr', models.SmallIntegerField(null=True, db_column=b'PTCHYR')),
                ('ptchyr2', models.SmallIntegerField(null=True, db_column=b'PTCHYR2')),
                ('ptchyr3', models.SmallIntegerField(null=True, db_column=b'PTCHYR3')),
                ('ratepm', models.SmallIntegerField(null=True, db_column=b'RATEPM')),
                ('ratepm2', models.SmallIntegerField(null=True, db_column=b'RATEPM2')),
                ('ratepm3', models.SmallIntegerField(null=True, db_column=b'RATEPM3')),
                ('redmo2', models.SmallIntegerField(null=True, db_column=b'REDMO2')),
                ('redmo3', models.SmallIntegerField(null=True, db_column=b'REDMO3')),
                ('redmon', models.SmallIntegerField(null=True, db_column=b'REDMON')),
                ('redpa2', models.SmallIntegerField(null=True, db_column=b'REDPA2')),
                ('redpa3', models.SmallIntegerField(null=True, db_column=b'REDPA3')),
                ('redpay', models.SmallIntegerField(null=True, db_column=b'REDPAY')),
                ('refi', models.SmallIntegerField(null=True, db_column=b'REFI')),
                ('refi2', models.SmallIntegerField(null=True, db_column=b'REFI2')),
                ('refi3', models.SmallIntegerField(null=True, db_column=b'REFI3')),
                ('sell', models.SmallIntegerField(null=True, db_column=b'SELL')),
                ('sell2', models.SmallIntegerField(null=True, db_column=b'SELL2')),
                ('sell3', models.SmallIntegerField(null=True, db_column=b'SELL3')),
                ('shock', models.SmallIntegerField(null=True, db_column=b'SHOCK')),
                ('shock2', models.SmallIntegerField(null=True, db_column=b'SHOCK2')),
                ('shock3', models.SmallIntegerField(null=True, db_column=b'SHOCK3')),
                ('submor', models.SmallIntegerField(null=True, db_column=b'SUBMOR')),
                ('submr2', models.SmallIntegerField(null=True, db_column=b'SUBMR2')),
                ('submr3', models.SmallIntegerField(null=True, db_column=b'SUBMR3')),
                ('submr4', models.SmallIntegerField(null=True, db_column=b'SUBMR4')),
                ('taxpmt', models.SmallIntegerField(null=True, db_column=b'TAXPMT')),
                ('term', models.SmallIntegerField(null=True, db_column=b'TERM')),
                ('term2', models.SmallIntegerField(null=True, db_column=b'TERM2')),
                ('term3', models.SmallIntegerField(null=True, db_column=b'TERM3')),
                ('timbom', models.SmallIntegerField(null=True, db_column=b'TIMBOM')),
                ('timbom2', models.SmallIntegerField(null=True, db_column=b'TIMBOM2')),
                ('timbom3', models.SmallIntegerField(null=True, db_column=b'TIMBOM3')),
                ('txpmt2', models.SmallIntegerField(null=True, db_column=b'TXPMT2')),
                ('txpmt3', models.SmallIntegerField(null=True, db_column=b'TXPMT3')),
                ('unpbal', models.IntegerField(null=True, db_column=b'UNPBAL')),
                ('unpbal2', models.IntegerField(null=True, db_column=b'UNPBAL2')),
                ('unpbal3', models.IntegerField(null=True, db_column=b'UNPBAL3')),
                ('unpbal4', models.IntegerField(null=True, db_column=b'UNPBAL4')),
                ('varm', models.SmallIntegerField(null=True, db_column=b'VARM')),
                ('varm2', models.SmallIntegerField(null=True, db_column=b'VARM2')),
                ('varm3', models.SmallIntegerField(null=True, db_column=b'VARM3')),
                ('vary', models.SmallIntegerField(null=True, db_column=b'VARY')),
                ('vary2', models.SmallIntegerField(null=True, db_column=b'VARY2')),
                ('vary3', models.SmallIntegerField(null=True, db_column=b'VARY3')),
                ('yrmor', models.IntegerField(null=True, db_column=b'YRMOR')),
                ('yrmor2', models.IntegerField(null=True, db_column=b'YRMOR2')),
                ('yrmor3', models.IntegerField(null=True, db_column=b'YRMOR3')),
                ('field_in_2013', models.BooleanField(default=False)),
                ('field_in_2011', models.BooleanField(default=False)),
                ('export_year', models.PositiveSmallIntegerField(null=True, db_index=True)),
            ],
            options={
                'db_table': 'ahs_mortg',
            },
        ),
        migrations.AlterIndexTogether(
            name='mortg',
            index_together=set([('control', 'export_year'), ('field_in_2013', 'field_in_2011')]),
        ),
    ]
