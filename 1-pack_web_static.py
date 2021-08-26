#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
from datetime import datetime
from fabric.api import local
from os import path


def do_pack():
    """Generates a tgz archive."""
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir versions")
    archive = "versions/web_static_{}.tgz".format(date_time)
    local("tar -cvzf {} web_static".format(archive))
    if path.exists(archive):
        return archive
    else:
        return None
