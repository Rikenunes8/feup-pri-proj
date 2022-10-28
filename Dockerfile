FROM solr:8.10

COPY solr/data/tracks.json /data/tracks.json
COPY solr/simple_schema.json /data/simple_schema.json
COPY solr/startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
