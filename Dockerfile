FROM solr:8.10

COPY solr/data/tracks.json /data/tracks.json
COPY solr/schema.json /data/schema.json
COPY solr/synonyms_en.txt /data/synonyms_en.txt
COPY solr/startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
