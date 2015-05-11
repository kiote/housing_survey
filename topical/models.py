from django.db import models


class Topical(models.Model):
    class Meta:
        db_table = 'ahs_topical'

    control = models.BigIntegerField(db_column='CONTROL', unique=True, primary_key=True)

    eage = models.SmallIntegerField(db_column='EAGE', null=True)
    dpdrfood = models.SmallIntegerField(db_column='DPDRFOOD', null=True)
    ptcostcarp = models.IntegerField(db_column='PTCOSTCARP', null=True)
    ptcostcarm = models.IntegerField(db_column='PTCOSTCARM', null=True)
    wbsidewalk = models.SmallIntegerField(db_column='WBSIDEWALK', null=True)
    dpemwater = models.SmallIntegerField(db_column='DPEMWATER', null=True)
    eaban = models.SmallIntegerField(db_column='EABAN', null=True)
    cefspknbors = models.SmallIntegerField(db_column='CEFSPKNBORS', null=True)
    ptcostinsu = models.IntegerField(db_column='PTCOSTINSU', null=True)
    ptoftsub = models.SmallIntegerField(db_column='PTOFTSUB', null=True)
    eprkg = models.SmallIntegerField(db_column='EPRKG', null=True)
    eheight = models.SmallIntegerField(db_column='EHEIGHT', null=True)
    ptgetbus = models.SmallIntegerField(db_column='PTGETBUS', null=True)
    ptgetsub = models.SmallIntegerField(db_column='PTGETSUB', null=True)
    ptusrail = models.SmallIntegerField(db_column='PTUSRAIL', null=True)
    wbnobkcrim = models.SmallIntegerField(db_column='WBNOBKCRIM', null=True)
    pthealth = models.SmallIntegerField(db_column='PTHEALTH', null=True)
    etrans = models.SmallIntegerField(db_column='ETRANS', null=True)
    wfprop = models.SmallIntegerField(db_column='WFPROP', null=True)
    wbnobklite = models.SmallIntegerField(db_column='WBNOBKLITE', null=True)
    cefgpblock = models.SmallIntegerField(db_column='CEFGPBLOCK', null=True)
    ptdispub = models.SmallIntegerField(db_column='PTDISPUB', null=True)
    dpevvehic = models.SmallIntegerField(db_column='DPEVVEHIC', null=True)
    ptoftbus = models.SmallIntegerField(db_column='PTOFTBUS', null=True)
    egreen = models.SmallIntegerField(db_column='EGREEN', null=True)
    ceftrusted = models.SmallIntegerField(db_column='CEFTRUSTED', null=True)
    ceffiresta = models.SmallIntegerField(db_column='CEFFIRESTA', null=True)
    ptdisrail = models.SmallIntegerField(db_column='PTDISRAIL', null=True)
    ejunk = models.SmallIntegerField(db_column='EJUNK', null=True)
    cefclosknit = models.SmallIntegerField(db_column='CEFCLOSKNIT', null=True)
    talknbor = models.SmallIntegerField(db_column='TALKNBOR', null=True)
    ptdisbus = models.SmallIntegerField(db_column='PTDISBUS', null=True)
    cefspkrelg = models.SmallIntegerField(db_column='CEFSPKRELG', null=True)
    dpgenert = models.SmallIntegerField(db_column='DPGENERT', null=True)
    ptusshut = models.SmallIntegerField(db_column='PTUSSHUT', null=True)
    smsa = models.PositiveIntegerField(db_column='SMSA', null=True, db_index=True)
    ptcostptr = models.IntegerField(db_column='PTCOSTPTR', null=True)
    cefdisrspct = models.SmallIntegerField(db_column='CEFDISRSPCT', null=True)
    cefspkprblm = models.SmallIntegerField(db_column='CEFSPKPRBLM', null=True)
    ptcostpark = models.IntegerField(db_column='PTCOSTPARK', null=True)
    dpevinfo = models.SmallIntegerField(db_column='DPEVINFO', null=True)
    wbnobkothr = models.SmallIntegerField(db_column='WBNOBKOTHR', null=True)
    cefhelpnbor = models.SmallIntegerField(db_column='CEFHELPNBOR', null=True)
    ptpubtrn = models.SmallIntegerField(db_column='PTPUBTRN', null=True)
    ptgetrail = models.SmallIntegerField(db_column='PTGETRAIL', null=True)
    ebarcl = models.SmallIntegerField(db_column='EBARCL', null=True)
    ptusotr = models.SmallIntegerField(db_column='PTUSOTR', null=True)
    cefgpchurch = models.SmallIntegerField(db_column='CEFGPCHURCH', null=True)
    wbentmnt = models.SmallIntegerField(db_column='WBENTMNT', null=True)
    ptdisshut = models.SmallIntegerField(db_column='PTDISSHUT', null=True)
    ecom1 = models.SmallIntegerField(db_column='ECOM1', null=True)
    ecom2 = models.SmallIntegerField(db_column='ECOM2', null=True)
    cefgetalong = models.SmallIntegerField(db_column='CEFGETALONG', null=True)
    wbservic = models.SmallIntegerField(db_column='WBSERVIC', null=True)
    drugstore = models.SmallIntegerField(db_column='DRUGSTORE', null=True)
    nhdbldsua = models.SmallIntegerField(db_column='NHDBLDSUA', null=True)
    satpol = models.SmallIntegerField(db_column='SATPOL', null=True)
    ptservic = models.SmallIntegerField(db_column='PTSERVIC', null=True)
    wbgrocer = models.SmallIntegerField(db_column='WBGROCER', null=True)
    cefsprypnt = models.SmallIntegerField(db_column='CEFSPRYPNT', null=True)
    ptretail = models.SmallIntegerField(db_column='PTRETAIL', null=True)
    nhdbldsud = models.SmallIntegerField(db_column='NHDBLDSUD', null=True)
    dpevloc = models.SmallIntegerField(db_column='DPEVLOC', null=True)
    dpevkit = models.SmallIntegerField(db_column='DPEVKIT', null=True)
    ptuscrpl = models.SmallIntegerField(db_column='PTUSCRPL', null=True)
    ptbank = models.SmallIntegerField(db_column='PTBANK', null=True)
    ptgetshut = models.SmallIntegerField(db_column='PTGETSHUT', null=True)
    wbnobktime = models.SmallIntegerField(db_column='WBNOBKTIME', null=True)
    ptusbus = models.SmallIntegerField(db_column='PTUSBUS', null=True)
    wbnobkbike = models.SmallIntegerField(db_column='WBNOBKBIKE', null=True)
    wbnobkfast = models.SmallIntegerField(db_column='WBNOBKFAST', null=True)
    dpevfin = models.SmallIntegerField(db_column='DPEVFIN', null=True)
    wbnobktraf = models.SmallIntegerField(db_column='WBNOBKTRAF', null=True)
    ewater = models.SmallIntegerField(db_column='EWATER', null=True)
    cefspkoffcl = models.SmallIntegerField(db_column='CEFSPKOFFCL', null=True)
    cefspkmeetg = models.SmallIntegerField(db_column='CEFSPKMEETG', null=True)
    wbnobkhlth = models.SmallIntegerField(db_column='WBNOBKHLTH', null=True)
    ptwkschl = models.SmallIntegerField(db_column='PTWKSCHL', null=True)
    wbwkschl = models.SmallIntegerField(db_column='WBWKSCHL', null=True)
    ptoftrail = models.SmallIntegerField(db_column='PTOFTRAIL', null=True)
    grocery = models.SmallIntegerField(db_column='GROCERY', null=True)
    dpevsep = models.SmallIntegerField(db_column='DPEVSEP', null=True)
    cefgpcivic = models.SmallIntegerField(db_column='CEFGPCIVIC', null=True)
    wbnobknosw = models.SmallIntegerField(db_column='WBNOBKNOSW', null=True)
    ptdissub = models.SmallIntegerField(db_column='PTDISSUB', null=True)
    dpbnread = models.SmallIntegerField(db_column='DPBNREAD', null=True)
    ceffighting = models.SmallIntegerField(db_column='CEFFIGHTING', null=True)
    ptustaxi = models.SmallIntegerField(db_column='PTUSTAXI', null=True)
    wbnobike = models.SmallIntegerField(db_column='WBNOBIKE', null=True)
    eroad = models.SmallIntegerField(db_column='EROAD', null=True)
    wbnobklane = models.SmallIntegerField(db_column='WBNOBKLANE', null=True)
    wbbikelane = models.SmallIntegerField(db_column='WBBIKELANE', null=True)
    spltwgt2 = models.DecimalField(db_column='SPLTWGT2', max_digits=20, decimal_places=10, null=True)
    spltwgt1 = models.DecimalField(db_column='SPLTWGT1', max_digits=20, decimal_places=10, null=True)
    cefsharvals = models.SmallIntegerField(db_column='CEFSHARVALS', null=True)
    wbretail = models.SmallIntegerField(db_column='WBRETAIL', null=True)
    volnteer = models.SmallIntegerField(db_column='VOLNTEER', null=True)
    wbnobkdest = models.SmallIntegerField(db_column='WBNOBKDEST', null=True)
    ptentmnt = models.SmallIntegerField(db_column='PTENTMNT', null=True)
    wbbank = models.SmallIntegerField(db_column='WBBANK', null=True)
    wbhealth = models.SmallIntegerField(db_column='WBHEALTH', null=True)
    ptcostgas = models.IntegerField(db_column='PTCOSTGAS', null=True)
    wbbikewalk = models.SmallIntegerField(db_column='WBBIKEWALK', null=True)
    ptoftshut = models.SmallIntegerField(db_column='PTOFTSHUT', null=True)
    nhdbldmh = models.SmallIntegerField(db_column='NHDBLDMH', null=True)
    wbnobkbdsw = models.SmallIntegerField(db_column='WBNOBKBDSW', null=True)
    ptussub = models.SmallIntegerField(db_column='PTUSSUB', null=True)
    dpaltcom = models.SmallIntegerField(db_column='DPALTCOM', null=True)
    cefskipschl = models.SmallIntegerField(db_column='CEFSKIPSCHL', null=True)
    dpevacpets = models.SmallIntegerField(db_column='DPEVACPETS', null=True)
    ptuscrsh = models.SmallIntegerField(db_column='PTUSCRSH', null=True)
    ptgrocer = models.SmallIntegerField(db_column='PTGROCER', null=True)
    friends = models.SmallIntegerField(db_column='FRIENDS', null=True)
    nhdbldmu = models.SmallIntegerField(db_column='NHDBLDMU', null=True)
