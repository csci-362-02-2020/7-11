#!/bin/sh

cd ..
rm -rf temp
mkdir temp
rm -rf reports
cd scripts

python3 testmap.py -v

