#! /usr/bin/bash

sudo apt-get install python3 r-base rpl libcurl4-openssl-dev libssl-dev iwatch cron openssh-server -y
chmod +x paquetes.R watch.R
sudo ./paquetes.R
