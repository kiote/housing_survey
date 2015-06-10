"""
This script will download data files (csv) from AHS site and save it to
data/non-git directory. Also it will unpack all files
"""
import django_init

from downloader.models import Downloader

Downloader().download()
