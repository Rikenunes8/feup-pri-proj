# Information Needs

### 1. I want 1991 Nirvana songs having between 2 and 3 minutes

- http://localhost:8983/solr/tracks/select?defType=dismax&fq=%7B!frange%20l%3D120%20u%3D180%7Dtrack_duration&indent=true&q.op=OR&q=%2BNirvana%20%2B1991&qf=artist%20album_release_date

- defType: dismax
- q: Nirvana 1991
- qf: artist album_release_date
- fq: {!frange l=120 u=180}track_duration



### 2. I want songs with a regretting tone

**Fields boosts**	The thing with ^ but for fields

- http://localhost:8983/solr/tracks/select?defType=dismax&indent=true&q.op=OR&q=sorrow%20pain&qf=track%5E2%20lyrics

- defType: dismax
- q: sorrow pain
- qf: track^2 lyrics



### 3. I want an underrated relaxing song

**Independent boosts**	The thing with ^ but general, independent of the field
boosts the album_ranking ?

- http://localhost:8983/solr/tracks/select?bf=field(album_ranking)&debugQuery=false&defType=dismax&indent=true&q.op=OR&q=calm%20enjoy%20peace%20quiet&qf=track%20album%20artist%20album_release_data%20lyrics&rows=100

- defType: dismax
- q: calm enjoy peace quiet
- qf: track album artist album_realease_date lyrics
- bf: field(album_ranking)



### 4. I want a song that speaks of love in a depressing way

**Term boosts**	    The thing with ^ but for words

- http://localhost:8983/solr/tracks/select?debugQuery=false&defType=dismax&indent=true&q.op=OR&q=love%5E5%20-good%20bad%20-happy%20sad&qf=lyrics&rows=100

- defType: dismax
- q: love^5 -good bad -happy sad 
- qf: lyrics



### 5. I want a song that talks of life and love

**Proximity searches** the thing with "word1 word2"~< distance >

- http://localhost:8983/solr/tracks/select?indent=true&q.op=AND&q=lyrics%3A%20%22life%20love%22~3

- defType: lucene
- q: lyrics: "life love"~3
- q.op: AND



### 6. I want songs about surprise and happiness

**Wildcards / Fuziness**	words with at the end, like surpr* or surprise~
Search for surpr* and happ* in the title

- http://localhost:8983/solr/tracks/select?debugQuery=false&indent=true&q.op=OR&q=track%3A%20surpr*%20%0Atrack%3A%20happ*&rows=100

- defType: lucene
- q: track: surpr* track: happ*



### 7. I want a song with a sentence like "I like her"

**Phrase match w/ slop**     dismax query

- http://localhost:8983/solr/tracks/select?debugQuery=false&defType=dismax&indent=true&q.op=OR&q=%22I%20like%20her%22&qf=tracks%20lyrics&qs=5&rows=100

- defType: dismax
- q: "I like her"
- qf: tracks lyrics
- qs: 5



### 8. I want the very best songs

- http://localhost:8983/solr/tracks/select?defType=dismax&indent=true&q.op=OR&q=rank%201&qf=album_ranking

- defType: dismax
- q: 1 rank
- qf: album_ranking






### I want the song that I remember has a line something like "the wish for crying"

### I want a happy song

### I want chrismtas  songs

### I want sad songs

### I want a good instrumental song