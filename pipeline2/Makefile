# rs means rolling stones

RS_HTML=rolling_stones.html
RS_CSV=rolling_stones.csv

all: get_rs_html rs_html_to_csv build_artist_album_track

get_rs_html:
	if [ -f $(RS_HTML) ]; then \
		echo "$(RS_HTML) already exists."; \
	else \
		curl -s 'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Albums/500' > "$(RS_HTML)"; \
	fi

rs_html_to_csv:
	python3 rolling_stones.py $(RS_HTML)

build_artist_album_track:
	chmod +x build_artist_album_track.sh
	bash build_artist_album_track.sh $(RS_CSV)

clean:
	rm -f $(RS_HTML)
	rm -f $(RS_CSV)
	rm -f rolling_stones_tracks.csv
