#!/bin/bash
#exec 1>var/www/html/uploads/scriptlog.txt 2>&1

echo "got to the beginning of the script"

cd /var/www/html

echo "after cd"

unzip /var/www/html/uploads/userUpload.zip -d /var/www/html/uploads

#sudo rm /var/www/html/uploads/userUpload.zip 

python createRepo.py

echo "after python"

cd /var/www/html/uploads

find . -maxdepth 1 -name \* -type f -printf "deleting %P\n" -delete


