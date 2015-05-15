import importlib

files = ['homimp', 'mortg', 'newhouse', 'omov', 'owner', 'person', 'ratiov', 'repwgt', 'rmov', 'topical']

for _file in files:
    module = importlib.import_module("datatype.%s.models" % _file)
    klass = getattr(module, "%sDatatype" % _file.capitalize())
    print "---> Save %s data (national)" % _file

    klass().save_csv()
