from django.db import models


class Person(models.Model):
    class Meta:
        db_table = 'ahs_person'

    control = models.BigIntegerField(db_column='CONTROL', unique=True, primary_key=True)

    pqint = models.SmallIntegerField(db_column='PQINT', null=True)
    par = models.SmallIntegerField(db_column='PAR', null=True)
    movm = models.PositiveSmallIntegerField(db_column='MOVM', null=True)
    pqssi = models.SmallIntegerField(db_column='PQSSI', null=True)
    pqss = models.SmallIntegerField(db_column='PQSS', null=True)
    age = models.PositiveSmallIntegerField(db_column='AGE', null=True)
    move = models.PositiveIntegerField(db_column='MOVE', null=True)
    pqsalnr = models.SmallIntegerField(db_column='PQSALNR', null=True)
    jpqrent = models.SmallIntegerField(db_column='JPQRENT', null=True)
    pcare = models.SmallIntegerField(db_column='PCARE', null=True)
    jpqslfnr = models.SmallIntegerField(db_column='JPQSLFNR', null=True)
    pqother = models.SmallIntegerField(db_column='PQOTHER', null=True)
    jpqother = models.SmallIntegerField(db_column='JPQOTHER', null=True)
    jmovm = models.SmallIntegerField(db_column='JMOVM', null=True)
    jpqself = models.SmallIntegerField(db_column='JPQSELF', null=True)
    pmemry = models.SmallIntegerField(db_column='PMEMRY', null=True)
    pqself = models.SmallIntegerField(db_column='PQSELF', null=True)
    lodrnt = models.IntegerField(db_column='LODRNT', null=True)
    jten = models.SmallIntegerField(db_column='JTEN', null=True)
    jmove = models.SmallIntegerField(db_column='JMOVE', null=True)
    phear = models.SmallIntegerField(db_column='PHEAR', null=True)
    rel = models.PositiveSmallIntegerField(db_column='REL', null=True)
    jsal = models.SmallIntegerField(db_column='JSAL', null=True)
    ten = models.PositiveSmallIntegerField(db_column='TEN', null=True)
    jspan = models.SmallIntegerField(db_column='JSPAN', null=True)
    jspos = models.SmallIntegerField(db_column='JSPOS', null=True)
    sal = models.IntegerField(db_column='SAL', null=True)
    jrel = models.SmallIntegerField(db_column='JREL', null=True)
    jmar = models.SmallIntegerField(db_column='JMAR', null=True)
    sex = models.PositiveSmallIntegerField(db_column='SEX', null=True)
    psee = models.SmallIntegerField(db_column='PSEE', null=True)
    race = models.PositiveSmallIntegerField(db_column='RACE', null=True)
    pqrent = models.SmallIntegerField(db_column='PQRENT', null=True)
    pqretir = models.SmallIntegerField(db_column='PQRETIR', null=True)
    pqsal = models.SmallIntegerField(db_column='PQSAL', null=True)
    grad = models.SmallIntegerField(db_column='GRAD', null=True)
    pqwkcmp = models.SmallIntegerField(db_column='PQWKCMP', null=True)
    jpqsal = models.SmallIntegerField(db_column='JPQSAL', null=True)
    jpqint = models.SmallIntegerField(db_column='JPQINT', null=True)
    jpqothnr = models.SmallIntegerField(db_column='JPQOTHNR', null=True)
    pline = models.PositiveSmallIntegerField(db_column='PLINE', null=True, db_index=True)
    jrace = models.SmallIntegerField(db_column='JRACE', null=True)
    jatvty = models.SmallIntegerField(db_column='JATVTY', null=True)
    jpqwkcmp = models.SmallIntegerField(db_column='JPQWKCMP', null=True)
    food = models.SmallIntegerField(db_column='FOOD', null=True)
    perrnd = models.SmallIntegerField(db_column='PERRND', null=True)
    jpvother = models.SmallIntegerField(db_column='JPVOTHER', null=True)
    spos = models.SmallIntegerField(db_column='SPOS', null=True)
    rntdue = models.SmallIntegerField(db_column='RNTDUE', null=True)
    inusyr = models.IntegerField(db_column='INUSYR', null=True)
    jage = models.SmallIntegerField(db_column='JAGE', null=True)
    jpqssi = models.SmallIntegerField(db_column='JPQSSI', null=True)
    pqalim = models.SmallIntegerField(db_column='PQALIM', null=True)
    natvty = models.PositiveIntegerField(db_column='NATVTY', null=True)
    pqselfnr = models.SmallIntegerField(db_column='PQSELFNR', null=True)
    jpqretir = models.SmallIntegerField(db_column='JPQRETIR', null=True)
    pqwelf = models.SmallIntegerField(db_column='PQWELF', null=True)
    mvg = models.SmallIntegerField(db_column='MVG', null=True)
    famrel = models.PositiveSmallIntegerField(db_column='FAMREL', null=True)
    citshp = models.PositiveSmallIntegerField(db_column='CITSHP', null=True)
    jpqalim = models.SmallIntegerField(db_column='JPQALIM', null=True)
    jpar = models.SmallIntegerField(db_column='JPAR', null=True)
    jgrad = models.SmallIntegerField(db_column='JGRAD', null=True)
    pvother = models.IntegerField(db_column='PVOTHER', null=True)
    famnum = models.PositiveSmallIntegerField(db_column='FAMNUM', null=True)
    mar = models.SmallIntegerField(db_column='MAR', null=True)
    span = models.PositiveSmallIntegerField(db_column='SPAN', null=True)
    pqdiv = models.SmallIntegerField(db_column='PQDIV', null=True)
    pwalk = models.SmallIntegerField(db_column='PWALK', null=True)
    pqothnr = models.SmallIntegerField(db_column='PQOTHNR', null=True)
    jpqdiv = models.SmallIntegerField(db_column='JPQDIV', null=True)
    jitshp = models.SmallIntegerField(db_column='JITSHP', null=True)
    jpqss = models.SmallIntegerField(db_column='JPQSS', null=True)
    smsa = models.PositiveIntegerField(db_column='SMSA', null=True)
    jnusyr = models.SmallIntegerField(db_column='JNUSYR', null=True)
    person = models.PositiveSmallIntegerField(db_column='PERSON', null=True)
    jpqsalnr = models.SmallIntegerField(db_column='JPQSALNR', null=True)
    jmvg = models.SmallIntegerField(db_column='JMVG', null=True)
    jsex = models.SmallIntegerField(db_column='JSEX', null=True)
    jpqwelf = models.SmallIntegerField(db_column='JPQWELF', null=True)
    lodsta = models.SmallIntegerField(db_column='LODSTA', null=True)
    famtyp = models.PositiveSmallIntegerField(db_column='FAMTYP', null=True)