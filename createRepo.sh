#!/bin/bash
exec &> /home/ubuntu/logfile.txt

cd /var/www/html

sudo apt-get install unzip

sudo unzip /var/www/html/uploads/userUpload.zip -d /var/www/html/uploads

sudo rm /var/www/html/uploads/userUpload.zip

python createRepo.py

cd /var/www/html/uploads

find . -maxdepth 1 -name \* -type f -printf "deleting %P\n" -delete


