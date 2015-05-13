from django.db import connection

import importlib

# make sure we have all files we need
# print '---> Downloading and unpacking AHS files...'
# Downloader().download()


print '---> Removing previously collected data...'
files = ['homimp', 'mortg', 'newhouse', 'omov', 'owner', 'person', 'ratiov', 'repwgt', 'rmov', 'topical']
truncate = "; ".join(["TRUNCATE `ahs_%s`;" % f for f in files])
with connection.cursor() as c:
    c.execute(truncate)

files = ['homimp']

for _file in files:
    module = importlib.import_module("datatype.%s.models" % _file)
    klass = getattr(module, "%sDatatype" % _file.capitalize())
    print "---> Save %s data (national)" % _file

    klass().save_csv()
    # db.close_connection()