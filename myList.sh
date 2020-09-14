#!/bin/bash
echo "Current directory: " $(basename "$PWD") > index.html

for folder in $(ls -d */) 
do 
printf '%b\n' "$folder" >> index.html
done

for file in $(ls -p | grep -v /)
do 
printf '%b\n' "$file" >> index.html
done
xdg-open index.html
