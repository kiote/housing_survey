from django.db import connection

files = ['homimp', 'mortg', 'newhouse', 'omov', 'owner', 'person', 'ratiov', 'repwgt', 'rmov', 'topical']
truncate = "; ".join(["TRUNCATE `ahs_%s`" % f for f in files])

with connection.cursor() as c:
    c.execute(truncate + ';')

from datatype.homimp.models import HomimpDatatype
from datatype.mortg.models import MortgDatatype
from datatype.newhouse.models import NewhouseDatatype
from datatype.omov.models import OmovDatatype
from datatype.owner.models import OwnerDatatype
from datatype.person.models import PersonDatatype
from datatype.ratiov.models import RatiovDatatype
from datatype.repwgt.models import RepwgtDatatype
from datatype.rmov.models import RmovDatatype
from datatype.topical.models import TopicalDatatype

HomimpDatatype().save_csv()
MortgDatatype().save_csv()
NewhouseDatatype().save_csv()
OmovDatatype().save_csv()
OwnerDatatype().save_csv()
PersonDatatype().save_csv()
RatiovDatatype().save_csv()
RepwgtDatatype().save_csv()
RmovDatatype().save_csv()
TopicalDatatype().save_csv()

