#!/bin/bash

{
    IFS=";"
    read
    while read -r -a fields; do
        python3 src/get_track_from_album_artist.py $2 ${fields[0]} ${fields[1]}
    done 
} < $1
