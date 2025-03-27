from lyricsgenius import Genius
import json

# Ask the user for the API key, input file, and output file
api_key = input("Enter your Genius API key: ")
input_file = input("Enter the path to the file with artist names: ")
output_file = input("Enter the path to the output JSON file: ")

# Initialize Genius API
genius = Genius(api_key)
genius.verbose = True  # Turn on status messages
genius.remove_section_headers = True  # Remove section headers (e.g. [Chorus]) from lyrics
genius.skip_non_songs = True  # Skip non-song entries
genius.excluded_terms = ["(Remix)", "(Live)", "(Mixed)", "(FreeStyle)", "(Original Version)"]  # Exclude songs with these terms
genius.sleep_time = 1
genius.retries = 3

# Read artist names from the input file
with open(input_file, 'r', encoding='utf-8') as file:
    artist_names = [line.strip() for line in file if line.strip()]

# Dictionary to store results
results = {}

# Search for each artist and save their songs
for artist_name in artist_names:
    print(f"Searching for songs by {artist_name}...")
    try:
        artist = genius.search_artist(artist_name, sort="title", max_songs=50)  # Limit to 50 songs per artist
        if artist:
            results[artist_name] = [song.to_dict() for song in artist.songs]  # Save song data as dictionaries
        else:
            print(f"No songs found for {artist_name}.")
    except Exception as e:
        print(f"Error while searching for {artist_name}: {e}")

# Save results to the output JSON file
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(results, json_file, ensure_ascii=False, indent=4)

print(f"Results saved to {output_file}.")