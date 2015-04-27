from datatype.newhouse.models import NewhouseDatatype

NewhouseDatatype('newhouse').generate_columns()
# copy columns
# add to settings
# makemigrations
# migrate
NewhouseDatatype('newhouse').save_csv()