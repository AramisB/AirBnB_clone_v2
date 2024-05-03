#!/usr/bin/env python3
"""A module that generates a .tgz archive from the contents of the web_static folder."""

from fabric.api import local, env, put, run
from datetime import datetime
from os.path import exists

env.hosts = ['54.172.126.130', '52.90.15.79']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        date = datetime.now()
        timestamp = date.strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_" + timestamp + ".tgz"
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        print("Error:", e)
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Uncompress the archive to /data/web_static/releases/<archive filename without extension>
        archive_filename = archive_path.split('/')[-1]
        release_folder = '/data/web_static/releases/{}'.format(
            archive_filename[:-4]
        )
        run('sudo mkdir -p {}'.format(release_folder))
        run('sudo tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        # Delete the archive from the web server
        run('sudo rm /tmp/{}'.format(archive_filename))

        # Delete the symbolic link /data/web_static/current
        run('sudo rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run('sudo ln -s {} /data/web_static/current'.format(release_folder))

        return True
    except Exception as e:
        print(e)
        return False

def deploy():
    """Creates and distributes an archive to your web servers."""
    # Call do_pack function and store the path of the created archive
    archive_path = do_pack()

    # Return False if no archive has been created
    if not archive_path:
        return False

    # Call do_deploy function, using the new path of the new archive
    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()

