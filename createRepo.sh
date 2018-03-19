#!/bin/bash

cd uploads

/var/www/html/createRepo.py

find . -maxdepth 1 -name \* -type f -printf "deleting %P\n" -delete


