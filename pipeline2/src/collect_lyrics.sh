#!/bin/bash

DIR=$1
FILE_RS_TRACKS=$2

{
    OUT=${DIR}all.csv
    touch ${OUT}
    IFS=";"
    read
    while read -r -a fields; do
        output=$((python3 "src/get_track_lyrics.py" $DIR ${fields[3]} ${fields[0]}) 2>&1)
        echo "output: ${output}"
        echo "${fields[*]}${IFS}${output}" >> ${OUT}
    done 
} < $FILE_RS_TRACKS
