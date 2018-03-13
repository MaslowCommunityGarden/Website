#!/bin/bash 
cd /home/ubuntu/Website
sudo git pull
sudo python buildSite.py
sudo python testScript.py
