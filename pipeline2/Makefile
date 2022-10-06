# rs means rolling stones

DIR := data/
RS_HTML := rolling_stones.html
RS_CSV := rolling_stones.csv
RST_CSV := rolling_stones_tracks.csv


all: collect process analyze

clean:
	rm -rf $(DIR)

collect:
	mkdir -p data
	
	chmod +x src/collect_rs_html.sh
	chmod +x src/collect_tracks.sh
	chmod +x src/collect_lyrics.sh

	bash src/collect_rs_html.sh $(DIR)$(RS_HTML)
	python3 src/rs_html_to_csv.py $(DIR)$(RS_HTML) $(DIR)$(RS_CSV)
	bash src/collect_tracks.sh $(DIR)$(RS_CSV) $(DIR)$(RST_CSV)
	bash src/collect_lyrics.sh $(DIR) $(DIR)$(RST_CSV)

process:
analyze:


