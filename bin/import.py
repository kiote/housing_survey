#!/usr/bin/env python

"""
This script will download data files (csv) from AHS site and save it to
data/non-git directory. Also it will unpack all files
"""
import initializers.framework

from downloader.models import Downloader

Downloader().download()
