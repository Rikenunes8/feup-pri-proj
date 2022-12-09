#!/bin/bash

precreate-core tracks

# Start Solr in background mode so we can use the API to upload the schema
solr start

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema.json \
    http://localhost:8983/solr/tracks/schema

curl -X POST \
    --data-binary @/data/synonyms_en.txt \
    http://localhost:8983/solr/tracks/conf

# Populate collection
bin/post -c tracks /data/tracks.json

# Restart in foreground mode so we can access the interface
solr restart -f
