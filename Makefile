# rs means rolling stones

DATA := data/
PROCESSED := processed/
ANALYSIS := analysis/
RS_HTML := rolling_stones.html
RS_CSV := rolling_stones.csv
RST_CSV := rolling_stones_tracks.csv
RS_COMPLETE := all.csv



all: collect process analyze

clean: clean-data clean-processed clean-analysis
	
clean-data:
	rm -rf $(DATA)
clean-processed:
	rm -rf $(PROCESSED)
clean-analysis:
	rm -rf $(ANALYSIS)

collect:
	mkdir -p data
	
	chmod +x src/collect_rs_html.sh
	chmod +x src/collect_tracks.sh
	chmod +x src/collect_lyrics.sh

	bash src/collect_rs_html.sh $(DATA)$(RS_HTML)
	python3 src/rs_html_to_csv.py $(DATA)$(RS_HTML) $(DATA)$(RS_CSV)
	bash src/collect_tracks.sh $(DATA)$(RS_CSV) $(DATA)$(RST_CSV)
	bash src/collect_lyrics.sh $(DATA) $(DATA)$(RST_CSV) $(DATA)$(RS_COMPLETE)

process:
	mkdir -p processed
	python3 src/normalize_release_date.py $(DATA)$(RS_COMPLETE) $(PROCESSED)$(RS_COMPLETE)

analyze:
	mkdir -p analysis
	python3 src/analyze_release_date.py $(PROCESSED)$(RS_COMPLETE)
	python3 src/analyze_lyrics_existence.py $(PROCESSED)$(RS_COMPLETE)


