#!/bin/bash
echo -e "<h3> Current directory: /"$(basename "$PWD")"</h3>" > index.html

for folder in $(ls -d */) 
do 
printf '<p style="color:0099FF;">%b\n' "/$folder""</p>" >> index.html
done

for file in $(ls -p | grep -v /)
do 
printf '<p style="color:9900CC;">%b\n' "$file""</p>" >> index.html
done
xdg-open index.html
