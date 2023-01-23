# rs means rolling stones

DATA := data/
PROCESSED := processed/
ANALYSIS := analysis/
RS_HTML := rolling_stones.html
RS_CSV := rolling_stones.csv
RST_CSV := rolling_stones_tracks.csv
RS_COMPLETE := all.csv
LYRICS_DIR := $(DATA)/lyrics



all: collect process analyze

clean: clean-data clean-processed clean-analysis
	
clean-data:
	rm -rf $(DATA)
clean-processed:
	rm -rf $(PROCESSED)
clean-analysis:
	rm -rf $(ANALYSIS)

collect: collect-tracks collect-lyrics

collect-tracks:
	mkdir -p $(DATA)

	chmod +x src/collect_rs_html.sh
	chmod +x src/collect_tracks.sh

	bash src/collect_rs_html.sh $(DATA)$(RS_HTML)
	python3 src/rs_html_to_csv.py $(DATA)$(RS_HTML) $(DATA)$(RS_CSV)
	bash src/collect_tracks.sh $(DATA)$(RS_CSV) $(DATA)$(RST_CSV)

collect-lyrics:
	mkdir -p $(DATA)
	chmod +x src/collect_lyrics.sh
	bash src/collect_lyrics.sh $(DATA) $(DATA)$(RST_CSV) $(DATA)$(RS_COMPLETE)

process:
	mkdir -p $(PROCESSED)
	python3 src/normalize_release_date.py $(DATA)$(RS_COMPLETE) $(PROCESSED)$(RS_COMPLETE)

analyze:
	mkdir -p $(ANALYSIS)
	python3 src/data_characterization/album_distribution_by_duration.py $(PROCESSED)$(RS_COMPLETE)
	python3 src/data_characterization/album_distribution_by_mean_song_duration.py $(PROCESSED)$(RS_COMPLETE)
	python3 src/data_characterization/album_distribution_by_year.py $(PROCESSED)$(RS_COMPLETE)
	python3 src/data_characterization/album_duration_by_ranking.py $(PROCESSED)$(RS_COMPLETE)
	python3 src/data_characterization/album_mean_song_duration_by_ranking.py $(PROCESSED)$(RS_COMPLETE)
	python3 src/data_characterization/album_number_of_songs_by_ranking.py $(PROCESSED)$(RS_COMPLETE)
	python3 src/data_characterization/album_release_date_by_ranking.py $(PROCESSED)$(RS_COMPLETE)
	python3 src/data_characterization/song_distribution_by_duration.py $(PROCESSED)$(RS_COMPLETE)
	python3 src/data_characterization/song_distribution_by_year.py $(PROCESSED)$(RS_COMPLETE)
	python3 src/data_characterization/lyrics_existence.py $(PROCESSED)$(RS_COMPLETE)
	python3 src/data_characterization/ranking_by_release_and_mean_duration.py $(PROCESSED)$(RS_COMPLETE)
	python3 src/data_characterization/make_wordcloud.py $(LYRICS_DIR)
	python3 src/data_characterization/track_by_number_of_words.py $(LYRICS_DIR)



