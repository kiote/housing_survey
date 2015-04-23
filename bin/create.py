from newhouse.models import Newhouse
from newhouse_datatype.models import NewhouseDatatype

NewhouseDatatype().write_types()
Newhouse().generate_columns()