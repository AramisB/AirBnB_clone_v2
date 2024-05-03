#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx HTTP'

#Create folders if doesn't already exist (use -p flag)
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

#create a HTML file
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
        <head>
        </head>
        <body>
        Holberton School
        </body>
        <html>" | sudo tee /data/web_static/releases/test/index.html
        
#Create a symbolic link
sudo -sf /data/web_static/releases/test/ /data/web_static/current

#Give ownership of /data/ folder to ubuntu user and group(recursively)
sudo chown -R ubuntu:ubuntu /data/

#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

#Restart Nginx
sudo service nginx restart