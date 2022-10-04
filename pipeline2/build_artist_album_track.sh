#!/bin/bash

IFS=";"
while read -r -a fields; do
    python3 get_track_from_album_artist.py ${fields[0]} ${fields[1]}
done < $1
