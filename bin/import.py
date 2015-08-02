#!/usr/bin/env python

"""
This script will download data files (csv) from AHS site and save it to
data/non-git directory. Also it will unpack all files
"""
import initializers.framework
import downloader.remote as remote
import downloader.local as local
import initializers.data as di

from downloader.models import Downloader

for y in di.YEARS:
    remote_attrs = remote.year_attributes(y)
    local_attrs = local.year_attributes(y)
    full_path = local.FULL_PATH
    Downloader(remote_attrs, local_attrs, full_path).download()
