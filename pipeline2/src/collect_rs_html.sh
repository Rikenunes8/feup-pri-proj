#!bin/bash

FILE=$1

if [ -f $FILE ]; then
    echo "$FILE already exists."
else
    curl -s 'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Albums/500' > $FILE
fi