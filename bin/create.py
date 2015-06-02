"""
This is the example of a model generation.
 Previously, app with the same name should be created
 with manage.py startapp

 Manual steps are commented, but they are required
"""
from datatype.determiner.models import AbstractDatatype
from datatype.saver.models import Datasaver

AbstractDatatype('newhouse').generate_columns()
# copy columns to the model file
# add new app to the settings file
# run makemigrations
# run migrate
Datasaver(2013, 'newhouse').fill_model_by_csv_data()
