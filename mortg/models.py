from django.db import models


class Mortg(models.Model):
    class Meta:
        db_table = 'ahs_mortg'

    control = models.BigIntegerField(db_column='CONTROL', unique=True, primary_key=True)

    ptchyr3 = models.SmallIntegerField(db_column='PTCHYR3', null=True)
    ptchyr2 = models.SmallIntegerField(db_column='PTCHYR2', null=True)
    jbloon = models.SmallIntegerField(db_column='JBLOON', null=True)
    jnpmt3 = models.SmallIntegerField(db_column='JNPMT3', null=True)
    jnpmt2 = models.SmallIntegerField(db_column='JNPMT2', null=True)
    imprv2 = models.SmallIntegerField(db_column='IMPRV2', null=True)
    imprv3 = models.SmallIntegerField(db_column='IMPRV3', null=True)
    inspm3 = models.SmallIntegerField(db_column='INSPM3', null=True)
    inspm2 = models.SmallIntegerField(db_column='INSPM2', null=True)
    minpm = models.SmallIntegerField(db_column='MINPM', null=True)
    mxdjtm = models.SmallIntegerField(db_column='MXDJTM', null=True)
    bank3 = models.SmallIntegerField(db_column='BANK3', null=True)
    bank2 = models.SmallIntegerField(db_column='BANK2', null=True)
    heinr1 = models.DecimalField(db_column='HEINR1', max_digits=20, decimal_places=10, null=True)
    heinr2 = models.DecimalField(db_column='HEINR2', max_digits=20, decimal_places=10, null=True)
    heinr3 = models.DecimalField(db_column='HEINR3', max_digits=20, decimal_places=10, null=True)
    inspmt = models.SmallIntegerField(db_column='INSPMT', null=True)
    jtcas3 = models.SmallIntegerField(db_column='JTCAS3', null=True)
    jtcas2 = models.SmallIntegerField(db_column='JTCAS2', null=True)
    mlnpm2 = models.SmallIntegerField(db_column='MLNPM2', null=True)
    mlnpm3 = models.SmallIntegerField(db_column='MLNPM3', null=True)
    pripmt = models.SmallIntegerField(db_column='PRIPMT', null=True)
    orintf = models.SmallIntegerField(db_column='ORINTF', null=True)
    orintr = models.DecimalField(db_column='ORINTR', max_digits=20, decimal_places=10, null=True)
    orintw = models.SmallIntegerField(db_column='ORINTW', null=True)
    minpm3 = models.SmallIntegerField(db_column='MINPM3', null=True)
    minpm2 = models.SmallIntegerField(db_column='MINPM2', null=True)
    ptchyr = models.SmallIntegerField(db_column='PTCHYR', null=True)
    jhecr1 = models.SmallIntegerField(db_column='JHECR1', null=True)
    otref2 = models.SmallIntegerField(db_column='OTREF2', null=True)
    otref3 = models.SmallIntegerField(db_column='OTREF3', null=True)
    mxintf3 = models.SmallIntegerField(db_column='MXINTF3', null=True)
    mxintf2 = models.SmallIntegerField(db_column='MXINTF2', null=True)
    fmrpmt3 = models.SmallIntegerField(db_column='FMRPMT3', null=True)
    sell2 = models.SmallIntegerField(db_column='SELL2', null=True)
    shock2 = models.SmallIntegerField(db_column='SHOCK2', null=True)
    shock3 = models.SmallIntegerField(db_column='SHOCK3', null=True)
    hepmt2 = models.IntegerField(db_column='HEPMT2', null=True)
    hepmt3 = models.SmallIntegerField(db_column='HEPMT3', null=True)
    hepmt1 = models.IntegerField(db_column='HEPMT1', null=True)
    jamtm = models.SmallIntegerField(db_column='JAMTM', null=True)
    lnfnbr3 = models.SmallIntegerField(db_column='LNFNBR3', null=True)
    lnfnbr2 = models.SmallIntegerField(db_column='LNFNBR2', null=True)
    yrmor = models.IntegerField(db_column='YRMOR', null=True)
    refi3 = models.SmallIntegerField(db_column='REFI3', null=True)
    refi2 = models.SmallIntegerField(db_column='REFI2', null=True)
    hebam3 = models.SmallIntegerField(db_column='HEBAM3', null=True)
    hebam2 = models.IntegerField(db_column='HEBAM2', null=True)
    hebam1 = models.IntegerField(db_column='HEBAM1', null=True)
    mortn2 = models.SmallIntegerField(db_column='MORTN2', null=True)
    mortn3 = models.SmallIntegerField(db_column='MORTN3', null=True)
    mortin = models.SmallIntegerField(db_column='MORTIN', null=True)
    mlnoth3 = models.SmallIntegerField(db_column='MLNOTH3', null=True)
    mlnoth2 = models.SmallIntegerField(db_column='MLNOTH2', null=True)
    mlnint = models.SmallIntegerField(db_column='MLNINT', null=True)
    jtpmt3 = models.SmallIntegerField(db_column='JTPMT3', null=True)
    jrefi2 = models.SmallIntegerField(db_column='JREFI2', null=True)
    doc = models.SmallIntegerField(db_column='DOC', null=True)
    orintf3 = models.SmallIntegerField(db_column='ORINTF3', null=True)
    orintf2 = models.SmallIntegerField(db_column='ORINTF2', null=True)
    jmrtz3 = models.SmallIntegerField(db_column='JMRTZ3', null=True)
    jmrtz2 = models.SmallIntegerField(db_column='JMRTZ2', null=True)
    othpmt = models.SmallIntegerField(db_column='OTHPMT', null=True)
    gpmwp = models.SmallIntegerField(db_column='GPMWP', null=True)
    intpmt = models.SmallIntegerField(db_column='INTPMT', null=True)
    adjdep = models.SmallIntegerField(db_column='ADJDEP', null=True)
    looncl = models.SmallIntegerField(db_column='LOONCL', null=True)
    hybmyr = models.SmallIntegerField(db_column='HYBMYR', null=True)
    intpm2 = models.SmallIntegerField(db_column='INTPM2', null=True)
    intpm3 = models.SmallIntegerField(db_column='INTPM3', null=True)
    refi = models.SmallIntegerField(db_column='REFI', null=True)
    maxadj2 = models.SmallIntegerField(db_column='MAXADJ2', null=True)
    maxadj3 = models.SmallIntegerField(db_column='MAXADJ3', null=True)
    jtcash = models.SmallIntegerField(db_column='JTCASH', null=True)
    heinw3 = models.SmallIntegerField(db_column='HEINW3', null=True)
    heinw2 = models.SmallIntegerField(db_column='HEINW2', null=True)
    heinw1 = models.SmallIntegerField(db_column='HEINW1', null=True)
    pmamt3 = models.SmallIntegerField(db_column='PMAMT3', null=True)
    pmamt2 = models.IntegerField(db_column='PMAMT2', null=True)
    pmpmt2 = models.SmallIntegerField(db_column='PMPMT2', null=True)
    pmpmt3 = models.SmallIntegerField(db_column='PMPMT3', null=True)
    jatbuy = models.SmallIntegerField(db_column='JATBUY', null=True)
    txpmt3 = models.SmallIntegerField(db_column='TXPMT3', null=True)
    txpmt2 = models.SmallIntegerField(db_column='TXPMT2', null=True)
    varm = models.SmallIntegerField(db_column='VARM', null=True)
    jmpmt2 = models.SmallIntegerField(db_column='JMPMT2', null=True)
    doc2 = models.SmallIntegerField(db_column='DOC2', null=True)
    doc3 = models.SmallIntegerField(db_column='DOC3', null=True)
    hybarm = models.SmallIntegerField(db_column='HYBARM', null=True)
    jterm2 = models.SmallIntegerField(db_column='JTERM2', null=True)
    jterm3 = models.SmallIntegerField(db_column='JTERM3', null=True)
    bloon = models.SmallIntegerField(db_column='BLOON', null=True)
    jvary = models.SmallIntegerField(db_column='JVARY', null=True)
    bank = models.SmallIntegerField(db_column='BANK', null=True)
    jaxpmt = models.SmallIntegerField(db_column='JAXPMT', null=True)
    ammort = models.IntegerField(db_column='AMMORT', null=True)
    jintw2 = models.SmallIntegerField(db_column='JINTW2', null=True)
    jintw3 = models.SmallIntegerField(db_column='JINTW3', null=True)
    jmiamt = models.SmallIntegerField(db_column='JMIAMT', null=True)
    intpm = models.SmallIntegerField(db_column='INTPM', null=True)
    jbank2 = models.SmallIntegerField(db_column='JBANK2', null=True)
    jbank3 = models.SmallIntegerField(db_column='JBANK3', null=True)
    mlnpm = models.SmallIntegerField(db_column='MLNPM', null=True)
    gpmwp3 = models.SmallIntegerField(db_column='GPMWP3', null=True)
    gpmwp2 = models.SmallIntegerField(db_column='GPMWP2', null=True)
    jthpmt = models.SmallIntegerField(db_column='JTHPMT', null=True)
    janvar = models.SmallIntegerField(db_column='JANVAR', null=True)
    amrtz2 = models.SmallIntegerField(db_column='AMRTZ2', null=True)
    amrtz3 = models.SmallIntegerField(db_column='AMRTZ3', null=True)
    mxdjtm3 = models.SmallIntegerField(db_column='MXDJTM3', null=True)
    mxdjtm2 = models.SmallIntegerField(db_column='MXDJTM2', null=True)
    taxpmt = models.SmallIntegerField(db_column='TAXPMT', null=True)
    ptcham = models.IntegerField(db_column='PTCHAM', null=True)
    maxadj = models.SmallIntegerField(db_column='MAXADJ', null=True)
    unpbal = models.IntegerField(db_column='UNPBAL', null=True)
    fxdpm3 = models.SmallIntegerField(db_column='FXDPM3', null=True)
    unpbal2 = models.IntegerField(db_column='UNPBAL2', null=True)
    unpbal4 = models.SmallIntegerField(db_column='UNPBAL4', null=True)
    otrpm = models.SmallIntegerField(db_column='OTRPM', null=True)
    jnspmt = models.SmallIntegerField(db_column='JNSPMT', null=True)
    jblon3 = models.SmallIntegerField(db_column='JBLON3', null=True)
    jblon2 = models.SmallIntegerField(db_column='JBLON2', null=True)
    vary3 = models.SmallIntegerField(db_column='VARY3', null=True)
    vary2 = models.SmallIntegerField(db_column='VARY2', null=True)
    lenmod = models.SmallIntegerField(db_column='LENMOD', null=True)
    addtn3 = models.SmallIntegerField(db_column='ADDTN3', null=True)
    addtn2 = models.SmallIntegerField(db_column='ADDTN2', null=True)
    jrmor2 = models.SmallIntegerField(db_column='JRMOR2', null=True)
    jrmor3 = models.SmallIntegerField(db_column='JRMOR3', null=True)
    submor = models.SmallIntegerField(db_column='SUBMOR', null=True)
    mxintf = models.SmallIntegerField(db_column='MXINTF', null=True)
    pmtinc2 = models.SmallIntegerField(db_column='PMTINC2', null=True)
    pmtinc3 = models.SmallIntegerField(db_column='PMTINC3', null=True)
    mxintr = models.DecimalField(db_column='MXINTR', max_digits=20, decimal_places=10, null=True)
    jintf3 = models.SmallIntegerField(db_column='JINTF3', null=True)
    mxintw = models.SmallIntegerField(db_column='MXINTW', null=True)
    jintf2 = models.SmallIntegerField(db_column='JINTF2', null=True)
    io = models.SmallIntegerField(db_column='IO', null=True)
    shock = models.SmallIntegerField(db_column='SHOCK', null=True)
    heinf1 = models.SmallIntegerField(db_column='HEINF1', null=True)
    heinf2 = models.SmallIntegerField(db_column='HEINF2', null=True)
    heinf3 = models.SmallIntegerField(db_column='HEINF3', null=True)
    intf2 = models.SmallIntegerField(db_column='INTF2', null=True)
    intf3 = models.SmallIntegerField(db_column='INTF3', null=True)
    jpmt = models.SmallIntegerField(db_column='JPMT', null=True)
    pmiamt = models.IntegerField(db_column='PMIAMT', null=True)
    timbom = models.SmallIntegerField(db_column='TIMBOM', null=True)
    perus1 = models.SmallIntegerField(db_column='PERUS1', null=True)
    perus3 = models.SmallIntegerField(db_column='PERUS3', null=True)
    perus2 = models.SmallIntegerField(db_column='PERUS2', null=True)
    intpmt3 = models.SmallIntegerField(db_column='INTPMT3', null=True)
    intpmt2 = models.SmallIntegerField(db_column='INTPMT2', null=True)
    jmamt3 = models.SmallIntegerField(db_column='JMAMT3', null=True)
    jmamt2 = models.SmallIntegerField(db_column='JMAMT2', null=True)
    mgresa2 = models.SmallIntegerField(db_column='MGRESA2', null=True)
    mgresa3 = models.SmallIntegerField(db_column='MGRESA3', null=True)
    jubmr2 = models.SmallIntegerField(db_column='JUBMR2', null=True)
    mlnint3 = models.SmallIntegerField(db_column='MLNINT3', null=True)
    mlnint2 = models.SmallIntegerField(db_column='MLNINT2', null=True)
    hybarm2 = models.SmallIntegerField(db_column='HYBARM2', null=True)
    hybarm3 = models.SmallIntegerField(db_column='HYBARM3', null=True)
    balamt2 = models.IntegerField(db_column='BALAMT2', null=True)
    adjrtf3 = models.SmallIntegerField(db_column='ADJRTF3', null=True)
    jyrmor = models.SmallIntegerField(db_column='JYRMOR', null=True)
    cash2 = models.IntegerField(db_column='CASH2', null=True)
    cash3 = models.SmallIntegerField(db_column='CASH3', null=True)
    ammrt4 = models.SmallIntegerField(db_column='AMMRT4', null=True)
    amtm2 = models.IntegerField(db_column='AMTM2', null=True)
    amtm3 = models.SmallIntegerField(db_column='AMTM3', null=True)
    jpmt2 = models.SmallIntegerField(db_column='JPMT2', null=True)
    jpmt3 = models.SmallIntegerField(db_column='JPMT3', null=True)
    ammrt3 = models.IntegerField(db_column='AMMRT3', null=True)
    ammrt2 = models.IntegerField(db_column='AMMRT2', null=True)
    sell3 = models.SmallIntegerField(db_column='SELL3', null=True)
    fmrpmt2 = models.SmallIntegerField(db_column='FMRPMT2', null=True)
    heyrmor2 = models.IntegerField(db_column='HEYRMOR2', null=True)
    heyrmor3 = models.IntegerField(db_column='HEYRMOR3', null=True)
    heyrmor = models.IntegerField(db_column='HEYRMOR', null=True)
    pripmt3 = models.SmallIntegerField(db_column='PRIPMT3', null=True)
    pripmt2 = models.SmallIntegerField(db_column='PRIPMT2', null=True)
    intf = models.SmallIntegerField(db_column='INTF', null=True)
    pmipmt = models.SmallIntegerField(db_column='PMIPMT', null=True)
    lenmod2 = models.SmallIntegerField(db_column='LENMOD2', null=True)
    lenmod3 = models.SmallIntegerField(db_column='LENMOD3', null=True)
    intw = models.SmallIntegerField(db_column='INTW', null=True)
    intr = models.DecimalField(db_column='INTR', max_digits=20, decimal_places=10, null=True)
    submr3 = models.SmallIntegerField(db_column='SUBMR3', null=True)
    submr2 = models.SmallIntegerField(db_column='SUBMR2', null=True)
    fixed = models.SmallIntegerField(db_column='FIXED', null=True)
    submr4 = models.SmallIntegerField(db_column='SUBMR4', null=True)
    jrefi = models.SmallIntegerField(db_column='JREFI', null=True)
    ratepm = models.SmallIntegerField(db_column='RATEPM', null=True)
    adjrtf = models.SmallIntegerField(db_column='ADJRTF', null=True)
    lnfnbr = models.SmallIntegerField(db_column='LNFNBR', null=True)
    jamtm3 = models.SmallIntegerField(db_column='JAMTM3', null=True)
    jamtm2 = models.SmallIntegerField(db_column='JAMTM2', null=True)
    pmt4 = models.SmallIntegerField(db_column='PMT4', null=True)
    pmt3 = models.IntegerField(db_column='PMT3', null=True)
    pmt2 = models.IntegerField(db_column='PMT2', null=True)
    jewmor = models.SmallIntegerField(db_column='JEWMOR', null=True)
    newmr3 = models.SmallIntegerField(db_column='NEWMR3', null=True)
    newmr2 = models.SmallIntegerField(db_column='NEWMR2', null=True)
    mlncls = models.SmallIntegerField(db_column='MLNCLS', null=True)
    frstrm = models.SmallIntegerField(db_column='FRSTRM', null=True)
    improv = models.SmallIntegerField(db_column='IMPROV', null=True)
    incpr2 = models.SmallIntegerField(db_column='INCPR2', null=True)
    incpr3 = models.SmallIntegerField(db_column='INCPR3', null=True)
    matbuy = models.SmallIntegerField(db_column='MATBUY', null=True)
    hybmyr2 = models.SmallIntegerField(db_column='HYBMYR2', null=True)
    hybmyr3 = models.SmallIntegerField(db_column='HYBMYR3', null=True)
    balamt = models.IntegerField(db_column='BALAMT', null=True)
    adjrtf2 = models.SmallIntegerField(db_column='ADJRTF2', null=True)
    junpbal = models.SmallIntegerField(db_column='JUNPBAL', null=True)
    balamt3 = models.SmallIntegerField(db_column='BALAMT3', null=True)
    fmrpmt = models.SmallIntegerField(db_column='FMRPMT', null=True)
    newmor = models.SmallIntegerField(db_column='NEWMOR', null=True)
    fxdpm = models.SmallIntegerField(db_column='FXDPM', null=True)
    otpmt2 = models.SmallIntegerField(db_column='OTPMT2', null=True)
    otpmt3 = models.SmallIntegerField(db_column='OTPMT3', null=True)
    redmo2 = models.SmallIntegerField(db_column='REDMO2', null=True)
    jmmrt4 = models.SmallIntegerField(db_column='JMMRT4', null=True)
    jmmrt2 = models.SmallIntegerField(db_column='JMMRT2', null=True)
    jmmrt3 = models.SmallIntegerField(db_column='JMMRT3', null=True)
    cash = models.IntegerField(db_column='CASH', null=True)
    intw3 = models.SmallIntegerField(db_column='INTW3', null=True)
    intw2 = models.SmallIntegerField(db_column='INTW2', null=True)
    adjfix3 = models.SmallIntegerField(db_column='ADJFIX3', null=True)
    looncl2 = models.SmallIntegerField(db_column='LOONCL2', null=True)
    adjpm2 = models.SmallIntegerField(db_column='ADJPM2', null=True)
    adjpm3 = models.SmallIntegerField(db_column='ADJPM3', null=True)
    arm2 = models.SmallIntegerField(db_column='ARM2', null=True)
    jintw = models.SmallIntegerField(db_column='JINTW', null=True)
    jintf = models.SmallIntegerField(db_column='JINTF', null=True)
    extlon = models.SmallIntegerField(db_column='EXTLON', null=True)
    janvr3 = models.SmallIntegerField(db_column='JANVR3', null=True)
    janvr2 = models.SmallIntegerField(db_column='JANVR2', null=True)
    jpmt4 = models.SmallIntegerField(db_column='JPMT4', null=True)
    incper = models.SmallIntegerField(db_column='INCPER', null=True)
    jterm = models.SmallIntegerField(db_column='JTERM', null=True)
    vary = models.SmallIntegerField(db_column='VARY', null=True)
    jewmr3 = models.SmallIntegerField(db_column='JEWMR3', null=True)
    jewmr2 = models.SmallIntegerField(db_column='JEWMR2', null=True)
    lowint = models.SmallIntegerField(db_column='LOWINT', null=True)
    term = models.SmallIntegerField(db_column='TERM', null=True)
    jortn3 = models.SmallIntegerField(db_column='JORTN3', null=True)
    jortn2 = models.SmallIntegerField(db_column='JORTN2', null=True)
    yrmor3 = models.IntegerField(db_column='YRMOR3', null=True)
    yrmor2 = models.IntegerField(db_column='YRMOR2', null=True)
    hecr3 = models.SmallIntegerField(db_column='HECR3', null=True)
    hecr2 = models.IntegerField(db_column='HECR2', null=True)
    hecr1 = models.IntegerField(db_column='HECR1', null=True)
    jvary2 = models.SmallIntegerField(db_column='JVARY2', null=True)
    jvary3 = models.SmallIntegerField(db_column='JVARY3', null=True)
    jmmort = models.SmallIntegerField(db_column='JMMORT', null=True)
    adjfix = models.SmallIntegerField(db_column='ADJFIX', null=True)
    frstrm3 = models.SmallIntegerField(db_column='FRSTRM3', null=True)
    frstrm2 = models.SmallIntegerField(db_column='FRSTRM2', null=True)
    mxintr3 = models.SmallIntegerField(db_column='MXINTR3', null=True)
    mxintr2 = models.DecimalField(db_column='MXINTR2', max_digits=20, decimal_places=10, null=True)
    mlndwn3 = models.SmallIntegerField(db_column='MLNDWN3', null=True)
    mlndwn2 = models.SmallIntegerField(db_column='MLNDWN2', null=True)
    matby3 = models.SmallIntegerField(db_column='MATBY3', null=True)
    matby2 = models.SmallIntegerField(db_column='MATBY2', null=True)
    inspm = models.SmallIntegerField(db_column='INSPM', null=True)
    lowin3 = models.SmallIntegerField(db_column='LOWIN3', null=True)
    lowin2 = models.SmallIntegerField(db_column='LOWIN2', null=True)
    arm = models.SmallIntegerField(db_column='ARM', null=True)
    canvr2 = models.SmallIntegerField(db_column='CANVR2', null=True)
    canvr3 = models.SmallIntegerField(db_column='CANVR3', null=True)
    intr2 = models.DecimalField(db_column='INTR2', max_digits=20, decimal_places=10, null=True)
    intr3 = models.DecimalField(db_column='INTR3', max_digits=20, decimal_places=10, null=True)
    adjdep3 = models.SmallIntegerField(db_column='ADJDEP3', null=True)
    adjdep2 = models.SmallIntegerField(db_column='ADJDEP2', null=True)
    amrtz = models.SmallIntegerField(db_column='AMRTZ', null=True)
    redmo3 = models.SmallIntegerField(db_column='REDMO3', null=True)
    looncl3 = models.SmallIntegerField(db_column='LOONCL3', null=True)
    jubmor = models.SmallIntegerField(db_column='JUBMOR', null=True)
    otrpm2 = models.SmallIntegerField(db_column='OTRPM2', null=True)
    otrpm3 = models.SmallIntegerField(db_column='OTRPM3', null=True)
    term3 = models.SmallIntegerField(db_column='TERM3', null=True)
    term2 = models.SmallIntegerField(db_column='TERM2', null=True)
    redmon = models.SmallIntegerField(db_column='REDMON', null=True)
    io3 = models.SmallIntegerField(db_column='IO3', null=True)
    io2 = models.SmallIntegerField(db_column='IO2', null=True)
    orintr3 = models.SmallIntegerField(db_column='ORINTR3', null=True)
    orintr2 = models.DecimalField(db_column='ORINTR2', max_digits=20, decimal_places=10, null=True)
    jatby2 = models.SmallIntegerField(db_column='JATBY2', null=True)
    jatby3 = models.SmallIntegerField(db_column='JATBY3', null=True)
    ratepm2 = models.SmallIntegerField(db_column='RATEPM2', null=True)
    ratepm3 = models.SmallIntegerField(db_column='RATEPM3', null=True)
    hebal1 = models.SmallIntegerField(db_column='HEBAL1', null=True)
    hebal2 = models.SmallIntegerField(db_column='HEBAL2', null=True)
    hebal3 = models.SmallIntegerField(db_column='HEBAL3', null=True)
    jbank = models.SmallIntegerField(db_column='JBANK', null=True)
    unpbal3 = models.IntegerField(db_column='UNPBAL3', null=True)
    fxdpm2 = models.SmallIntegerField(db_column='FXDPM2', null=True)
    timbom3 = models.SmallIntegerField(db_column='TIMBOM3', null=True)
    timbom2 = models.SmallIntegerField(db_column='TIMBOM2', null=True)
    jmipmt = models.SmallIntegerField(db_column='JMIPMT', null=True)
    ptcham2 = models.IntegerField(db_column='PTCHAM2', null=True)
    ptcham3 = models.SmallIntegerField(db_column='PTCHAM3', null=True)
    jrtyp3 = models.SmallIntegerField(db_column='JRTYP3', null=True)
    jrtyp2 = models.SmallIntegerField(db_column='JRTYP2', null=True)
    jrtyp1 = models.SmallIntegerField(db_column='JRTYP1', null=True)
    jtpmt2 = models.SmallIntegerField(db_column='JTPMT2', null=True)
    othref = models.SmallIntegerField(db_column='OTHREF', null=True)
    jxpmt3 = models.SmallIntegerField(db_column='JXPMT3', null=True)
    jxpmt2 = models.SmallIntegerField(db_column='JXPMT2', null=True)
    inpmt2 = models.SmallIntegerField(db_column='INPMT2', null=True)
    inpmt3 = models.SmallIntegerField(db_column='INPMT3', null=True)
    mlnoth = models.SmallIntegerField(db_column='MLNOTH', null=True)
    mrtyp2 = models.SmallIntegerField(db_column='MRTYP2', null=True)
    mrtyp3 = models.SmallIntegerField(db_column='MRTYP3', null=True)
    mrtyp1 = models.SmallIntegerField(db_column='MRTYP1', null=True)
    pmt = models.IntegerField(db_column='PMT', null=True)
    mxintw2 = models.SmallIntegerField(db_column='MXINTW2', null=True)
    mxintw3 = models.SmallIntegerField(db_column='MXINTW3', null=True)
    fixed2 = models.SmallIntegerField(db_column='FIXED2', null=True)
    fixed3 = models.SmallIntegerField(db_column='FIXED3', null=True)
    mlncls2 = models.SmallIntegerField(db_column='MLNCLS2', null=True)
    mlncls3 = models.SmallIntegerField(db_column='MLNCLS3', null=True)
    mgresa = models.SmallIntegerField(db_column='MGRESA', null=True)
    varm2 = models.SmallIntegerField(db_column='VARM2', null=True)
    extln3 = models.SmallIntegerField(db_column='EXTLN3', null=True)
    extln2 = models.SmallIntegerField(db_column='EXTLN2', null=True)
    gtcas2 = models.SmallIntegerField(db_column='GTCAS2', null=True)
    gtcas3 = models.SmallIntegerField(db_column='GTCAS3', null=True)
    jortin = models.SmallIntegerField(db_column='JORTIN', null=True)
    pmtinc = models.SmallIntegerField(db_column='PMTINC', null=True)
    junpbal2 = models.SmallIntegerField(db_column='JUNPBAL2', null=True)
    junpbal3 = models.SmallIntegerField(db_column='JUNPBAL3', null=True)
    bloon2 = models.SmallIntegerField(db_column='BLOON2', null=True)
    bloon3 = models.SmallIntegerField(db_column='BLOON3', null=True)
    junpbal4 = models.SmallIntegerField(db_column='JUNPBAL4', null=True)
    adjfix2 = models.SmallIntegerField(db_column='ADJFIX2', null=True)
    redpay = models.SmallIntegerField(db_column='REDPAY', null=True)
    orintw2 = models.SmallIntegerField(db_column='ORINTW2', null=True)
    orintw3 = models.SmallIntegerField(db_column='ORINTW3', null=True)
    adjpm = models.SmallIntegerField(db_column='ADJPM', null=True)
    jamrtz = models.SmallIntegerField(db_column='JAMRTZ', null=True)
    redpa2 = models.SmallIntegerField(db_column='REDPA2', null=True)
    redpa3 = models.SmallIntegerField(db_column='REDPA3', null=True)
    mlndwn = models.SmallIntegerField(db_column='MLNDWN', null=True)
    arm3 = models.SmallIntegerField(db_column='ARM3', null=True)
    addtns = models.SmallIntegerField(db_column='ADDTNS', null=True)
    sell = models.SmallIntegerField(db_column='SELL', null=True)
    varm3 = models.SmallIntegerField(db_column='VARM3', null=True)
    canvar = models.SmallIntegerField(db_column='CANVAR', null=True)
    amtm = models.IntegerField(db_column='AMTM', null=True)
    gtcash = models.SmallIntegerField(db_column='GTCASH', null=True)
    add_year = models.PositiveSmallIntegerField(db_column='ADD_YEAR', default=2013, db_index=True)

