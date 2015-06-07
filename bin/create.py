"""
 Manual steps are commented, but they are required

 To run this you should first run in command line:

    export PYTHONPATH="/webapps/housing_survey/:$PYTHONPATH"

  And then just run it with python bin/create.py
"""
import django_init

from datatype.determiner.models import AbstractDatatype

files = ['homimp', 'mortg', 'newhouse', 'omov', 'owner', 'person', 'ratiov', 'repwgt', 'rmov', 'topical']
years = [2013, 2011]

for year in years:
    for base_name in files:
        print "%d: %s" % (year, base_name)
        AbstractDatatype(year, base_name).generate_columns()
# copy columns to the model file
# run makemigrations
# run migrate
# run load_data.py
