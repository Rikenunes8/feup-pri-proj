#!/bin/bash

DIR=$1
FILE_RS_TRACKS=$2
FILE_RS_COMPLETE=$3


if [ -f $FILE_RS_COMPLETE ]; then
    echo "$FILE_RS_COMPLETE already exists."
else
    {
        mkdir -p data/lyrics
        OUT=${FILE_RS_COMPLETE}
        touch ${OUT}
        IFS=";"
        header=$(head -n 1 $FILE_RS_TRACKS)
        echo "${header}${IFS}lyrics" >> ${OUT}
        read
        while read -r -a fields; do
            output=$((python3 "src/get_track_lyrics.py" $DIR ${fields[4]} ${fields[0]}) 2>&1)
            echo "output: ${output}"
            echo "${fields[*]}${IFS}${output}" >> ${OUT}
        done 
    } < $FILE_RS_TRACKS
fi