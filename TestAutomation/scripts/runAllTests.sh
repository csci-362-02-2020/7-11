#!/bin/sh


rm -rf temp
mkdir temp
rm -rf reports


python3 ./scripts/testmap.py -v
