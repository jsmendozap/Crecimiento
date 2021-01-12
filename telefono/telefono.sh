#!/usr/bin/bash

pkg update -y && pkg upgrade -y
pkg install termux-api cronie openssh python -y
pip install --upgrade pip
pip install pytelegrambotapi
pip install python-crontab
chmod +x bot.py monitoreo.py
