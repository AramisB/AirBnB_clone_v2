#!/usr/bin/env bash
# A script to set up web server for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p '/data/web_static/shared/'
sudo mkdir -p '/data/web_static/releases/test/'

index='/data/web_static/releases/test/index.html'
s_link="/data/web_static/current"
simple_web_content="
<html>\n
  <head>\n
  </head>\n
  <body>\n
    Holberton School\n
  </body>\n
</html>\n
"

if [ ! -e "$index" ]
then 
    sudo touch "$index"
fi

sudo chown "$USER":"$USER" "$index"
echo -e "$simple_web_content" > "$index"

if [ -e "$s_link" ]
then    
    rm "$s_link"
fi

sudo ln -s -f '/data/web_static/releases/test/' "$s_link"
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

# Updating the nginx.conf file to include the /hbnb_static location.
CONFIG="server {\n

        listen 80 default_server;\n

        listen [::]:80 default_server;\n

        root /var/www/html;\n\n



        index index.html index.htm index.nginx-debian.html;\n

        server_name _;\n

        location / {\n

                add_header X-Served-By 531574-web-02;\n
                try_files \$uri /\$uri/ /404.html;\n

        }
        location /hbnb_static {\n

            alias /data/web_static/current/;\n
            index index.html;
        }
        location /redirect_me {\n

            return 301 https://www.alxafrica.com;\n

        }\n

        error_page 404 /404.html;\n

        location = /404.html {\n

            root /var/www/html;\n

            internal;\n

        }\n

}\n"

if [ ! -w '/etc/nginx/sites-available/default' ]
then
    sudo chown ubuntu:ubuntu '/etc/nginx/sites-available/default'
fi
echo -e "$CONFIG" > '/etc/nginx/sites-available/default'
sudo chown root:root '/etc/nginx/sites-available/default'
sudo service nginx reload
