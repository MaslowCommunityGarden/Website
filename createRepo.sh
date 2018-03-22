#!/bin/bash
#exec 1>var/www/html/uploads/scriptlog.txt 2>&1

echo "got to the beginning of the script"

cd /var/www/html

unzip /var/www/html/uploads/userUpload.zip -d /var/www/html/uploads

rm /var/www/html/uploads/userUpload.zip 

python createRepo.py

cd /var/www/html/uploads/tmp 

cd /var/www/html/uploads

rm -r -f /var/www/html/uploads/tmp

find . -maxdepth 1 -name \* -type f -printf "deleting %P\n" -delete


