from datatype.newhouse.models import NewhouseDatatype

NewhouseDatatype().generate_columns()
# copy columns
# makemigrations
# migrate
NewhouseDatatype().save_csv()