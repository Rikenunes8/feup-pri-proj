#!/bin/bash

precreate-core tracks

# Start Solr in background mode so we can use the API to upload the schema
solr start

# cp /data/synonyms_en.txt /var/solr/data/tracks/synonyms_en.txt

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema.json \
    http://localhost:8983/solr/tracks/schema

# Populate collection
bin/post -c tracks /data/m2_tracks.json

# Restart in foreground mode so we can access the interface
solr restart -f
