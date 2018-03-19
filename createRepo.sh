#!/bin/bash

cd /var/www/html

python createRepo.py

cd var/www/html/uploads

find . -maxdepth 1 -name \* -type f -printf "deleting %P\n" -delete


