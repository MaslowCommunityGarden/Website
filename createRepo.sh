#!/bin/bash

cd uploads

find . -maxdepth 1 -name \* -type f -printf "deleting %P\n" -delete


