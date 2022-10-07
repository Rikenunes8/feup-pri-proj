#!/bin/bash

FILE_RS=$1
FILE_RS_TRACKS=$2

if [ -f $FILE_RS_TRACKS ]; then
    echo "$FILE_RS_TRACKS already exists."
else
    {
        IFS=";"
        read
        while read -r -a fields; do
            python3 src/get_track_infos.py $FILE_RS_TRACKS ${fields[0]} ${fields[1]} ${fields[2]}
        done 
    } < $FILE_RS
fi


