docker exec pri_container bin/solr delete -c tracks
docker exec pri_container bin/solr create_core -c tracks

curl -X POST -H 'Content-type:application/json' \
    --data-binary @solr/simple_schema.json \
    http://localhost:8983/solr/tracks/schema

curl -X POST -H 'Content-type:application/json' \
--data-binary @solr/data/tracks.json \
http://localhost:8983/solr/tracks/update?commit=true
