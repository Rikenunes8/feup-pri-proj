# Information Needs

### Which are the songs from Nirvana of 1991 having between 2 and 3 minutes?

- http://localhost:8983/solr/tracks/select?defType=dismax&indent=true&q.op=OR&q=Nirvana%201991&qf=artist%20album_release_date&rows=100
- http://localhost:8983/solr/tracks/select?defType=dismax&indent=true&q.op=OR&q=%2BNirvana%20%2B1991&qf=artist%20album_release_date&rows=100
- http://localhost:8983/solr/tracks/select?defType=dismax&fq=%7B!frange%20l%3D120%20u%3D180%7Dtrack_duration&indent=true&q.op=OR&q=%2BNirvana%20%2B1991&qf=artist%20album_release_date

defType: dismax
q: Nirvana 1991
qf: artist album_release_date
fq: {!frange l=120 u=180}track_duration

### Which are the songs belonging to the best album?

- http://localhost:8983/solr/tracks/select?defType=dismax&indent=true&q.op=OR&q=rank%201&qf=album_ranking

defType: dismax
q: 1 rank
qf: album_ranking

### Which songs have a regretting tone?

- http://localhost:8983/solr/tracks/select?defType=dismax&indent=true&q.op=OR&q=sorrow%20pain&qf=track%5E2%20lyrics

q: sorrow pain
defType: dismax
qf: track^2 lyrics

**Field Boost** on track name

### Information of which song has in its title "she came in through" (TODO)
