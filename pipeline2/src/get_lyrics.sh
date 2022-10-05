#!/bin/bash

{
    OUT=$2all.csv
    touch ${OUT}
    IFS=";"
    read
    while read -r -a fields; do
        output=$((python3 "src/get_tracks_lyrics.py" $2 ${fields[0]} ${fields[2]}) 2>&1)
        echo "output: ${output}"
        echo "${fields[*]}${IFS}${output}" >> ${OUT}
    done 
} < $1
