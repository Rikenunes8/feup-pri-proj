FROM solr:8.10

# Copy the tracks file to the data directory
COPY solr/data/tracks.json /data/tracks.json

# Copy the schema file to the data directory
COPY solr/simple_schema.json /data/schema.json

# Copy the synonyms file to the data directory
COPY solr/synonyms/synonyms_en.txt /data/synonyms_en.txt
COPY solr/synonyms/synonyms_es.txt /data/synonyms_es.txt

COPY solr/startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
