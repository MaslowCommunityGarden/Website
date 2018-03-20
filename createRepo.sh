#!/bin/bash

cd /var/www/html

unzip /var/www/html/uploads/userUpload.zip -d /home/ubuntu

sudo rm /var/www/html/uploads/userUpload.zip

python createRepo.py

cd /var/www/html/uploads

find . -maxdepth 1 -name \* -type f -printf "deleting %P\n" -delete


