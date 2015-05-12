from downloader.models import Downloader
from django.db import connection

# make sure we have all files we need
print '---> Downloading and unpacking AHS files...'
Downloader().download()


# files = ['homimp', 'mortg', 'newhouse', 'omov', 'owner', 'person', 'ratiov', 'repwgt', 'rmow', 'topical']
print '---> Removing previously collected data...'
cursor = connection.cursor()
cursor.execute('''TRUNCATE `ahs_omov`;
               TRUNCATE `ahs_topical`;
               TRUNCATE `ahs_mortg`;
               TRUNCATE `ahs_ratiov`;
               TRUNCATE `ahs_owner`;
               TRUNCATE `ahs_homimp`;
               TRUNCATE `ahs_person`;
               TRUNCATE `auth_user`;
               TRUNCATE `ahs_rmov`;
               TRUNCATE `ahs_newhouse`;
               TRUNCATE `ahs_repwgt`;''')

from datatype.homimp.models import HomimpDatatype
HomimpDatatype().save_csv()