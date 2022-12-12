FROM solr:8.10

COPY solr/data/m2_tracks.json /data/m2_tracks.json
COPY solr/m2_schema.json /data/schema.json
# COPY solr/synonyms/synonyms_en.txt /data/synonyms_en.txt
COPY solr/startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
