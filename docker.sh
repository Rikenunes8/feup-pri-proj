#!/bin/bash

docker stop pri_container
docker rm pri_container
docker build -t pri_tracks .
docker run -p 8983:8983 --name pri_container --rm -d pri_tracks