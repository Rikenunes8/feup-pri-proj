# rs means rolling stones

DIR=data/
RS_HTML=rolling_stones.html
RS_CSV=rolling_stones.csv
RST_CSV=rolling_stones_tracks.csv


all: makedir get_rs_html rs_html_to_csv build_artist_album_track get_lyrics

makedir:
	mkdir -p data

get_rs_html:
	if [ -f "$(DIR)$(RS_HTML)" ]; then \
		echo "$(DIR)$(RS_HTML) already exists."; \
	else \
		curl -s 'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Albums/500' > "$(DIR)$(RS_HTML)"; \
	fi

rs_html_to_csv:
	if [ -f "$(DIR)$(RS_CSV)" ]; then \
		echo "$(DIR)$(RS_CSV) already exists."; \
	else \
		python3 src/rolling_stones.py "$(DIR)$(RS_HTML)" "$(DIR)$(RS_CSV)"; \
	fi

build_artist_album_track:
	if [ -f "$(DIR)$(RST_CSV)" ]; then \
		echo "$(DIR)$(RST_CSV) already exists."; \
	else \
		chmod +x src/build_artist_album_track.sh; \
		bash src/build_artist_album_track.sh $(DIR)$(RS_CSV) $(DIR)$(RST_CSV); \
	fi

get_lyrics: 
	chmod +x src/get_lyrics.sh
	bash src/get_lyrics.sh $(DIR)$(RST_CSV) $(DIR)

clean:
	rm -rf $(DIR)
