#!/usr/bin/python3
"""
Fabric script to create archive
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    making an archive best on the web_static folder
    """
    static_archive = 'web_static_' + datetime.now().strftime(
        "%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local(f'tar -cvzf versions/{static_archive} web_static')
    if create is not None:
        return static_archive
    else:
        return None
