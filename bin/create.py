from datatype.newhouse.models import NewhouseDatatype

NewhouseDatatype().generate_columns()
# copy columns
# add to settings
# makemigrations
# migrate
NewhouseDatatype().save_csv()