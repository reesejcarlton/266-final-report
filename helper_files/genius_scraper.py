#helper scraper code:
#https://github.com/johnwmillr/LyricsGenius



GENIUS_API_TOKEN = #insert token here

import json
from lyricsgenius import Genius

import requests
from requests.exceptions import Timeout



genius = Genius(GENIUS_API_TOKEN)
genius.timeout = 100


artist_name = "Johnny Cash" #Elvis Presley, Johnny Cash, Adele

print('22')
#search_artist() only returns songs where the given artist is the primary artist
#include_features param: to get all of the songs that the artist appears on
artist = genius.search_artist(artist_name, sort = "title", include_features = True) #, max_songs = 5)
print('26')
print(artist)
print('28')
#big json file
# artist.save_lyrics() 

#compact lyrics files for all songs
songs_list = []
for song in artist.songs:
	# try:
		# response = requests.get(song, timeout = timeout_seconds)
		# response.raise_for_status()

	song_dict = song.to_dict()
	# print(song.to_dict())
	print('====================')

	song_id = song_dict.get('description_annotation').get('id')
	song_album = song_dict.get('album')
	print(song_album)

	# (‘all’, ‘rap’, ‘pop’, ‘rb’, ‘rock’ or ‘country’)


	artists = song_dict.get('artist_names')
	if '(Ft.' in artists:
	    # Split by '(Ft.' to separate primary artist and featured artists
	    primary_artist, featured_artist = artists.split('(Ft.')
	    
	    # Clean up whitespace and remove the closing parenthesis
	    primary_artist = primary_artist.strip()  # Adele
	    featured_artist = featured_artist.strip(')').strip()  # Greg Kurstin
	else:
	    # No featured artist
	    primary_artist = artists.strip()
	    featured_artist = None

	song_data = {'song_id': song_id,
				 'title': song.title,
				 'primary_artist': primary_artist,
				 'featured_artists': featured_artist,
				 'release_date': song_dict.get('release_date'),
        		 # 'genre': song.genre,  # Genre (may not be available in all cases)
    			 'lyrics': song.lyrics}

    			 #TODO
    			 #probably have to add a "search song to find album"
    			 #then can get genre, release date
    			 #i think
	songs_list.append(song_data)
	# except Timeout:
	# 	print(f"Request for {song} timed out. Skipping to the next song.")
	# except requests.RequestException as e:
	# 	print(f"An error occurred: {e}")


# print(songs_list)
# 

#save songs list
file_name = f'{artist_name}_songs_scraped.json'

with open(file_name, 'w') as f:
    json.dump(songs_list, f, ensure_ascii = False, indent = 4)

print(f'--- Saved {len(songs_list)} songs to {file_name}')
