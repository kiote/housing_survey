from newhouse.models import Newhouse
from datatype.newhouse.models import NewhouseDatatype

NewhouseDatatype().write_types()
NewhouseDatatype().generate_columns()
# copy columns
# makemigrations
# migrate
Newhouse().read_data_file()