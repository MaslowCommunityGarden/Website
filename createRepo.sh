#!/bin/bash

cd /var/www/html

sudo unzip /var/www/html/uploads/userUpload.zip

#sudo rm /var/www/html/uploads/userUpload.zip

sudo python createRepo.py

cd /var/www/html/uploads

#find . -maxdepth 1 -name \* -type f -printf "deleting %P\n" -delete


