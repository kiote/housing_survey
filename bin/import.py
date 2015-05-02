"""
This script will download data files (csv) from ahs site and save it to
data/non-git directory. Also it will unpack all files
"""
from downloader.models import Downloader

Downloader().download()
