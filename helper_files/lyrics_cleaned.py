import json
import re


lyrics_list = ['Adele_songs_scraped.json', 'Elvis_songs_scraped.json'] #, 'Johnny_Cash_songs_scraped.json']




for f in lyrics_list:
	# Open and read the JSON file
	with open(f, 'r') as file:
	    data = json.load(file)
	    # print(data)
	    for song in data:
	    	title = song['title'] + " Lyrics"
	    	# Find where the title appears in the lyrics
	    	match = re.search(rf"{re.escape(title)}", song['lyrics'], re.IGNORECASE)
	    	# print("MATCH")
	    	# print(match)
	    	if match:
	    		# Keep the lyrics from the title onward
	    		song['lyrics'] = song['lyrics'][match.end():].strip()

	    	song['lyrics'] = re.sub(r"Embed$", "", song['lyrics']).strip()
	    	# print(song['lyrics'])

	new_filename = f.replace(".json", "_cleaned.json")
	# Save the modified data back to a new file
	with open(new_filename, 'w') as file:
		json.dump(data, file, indent = 4)  # indent=4 for pretty-printing