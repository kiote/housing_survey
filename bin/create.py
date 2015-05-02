"""
This is the example of a model generation.
 Previously, app with the same name should be created
 with manage.py startapp

 Manual steps are commented, but they are required
"""
from datatype.newhouse.models import NewhouseDatatype

NewhouseDatatype('newhouse').generate_columns()
# copy columns to the model file
# add new app to the settings file
# run makemigrations
# run migrate
NewhouseDatatype('newhouse').save_csv()