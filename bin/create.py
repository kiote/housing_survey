from newhouse.models import Newhouse
from newhouse_datatype.models import NewhouseDatatype

NewhouseDatatype().write_types()
Newhouse().generate_columns()
# copy columns
Newhouse().read_data_file()