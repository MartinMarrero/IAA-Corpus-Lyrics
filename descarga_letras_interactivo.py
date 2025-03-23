from lyricsgenius import Genius

# Ask the user for the API key and artist name
api_key = input("Enter your Genius API key: ")
artist_name = input("Enter the artist name: ")

genius = Genius(api_key)

genius.verbose = True  # Turn off status messages
genius.remove_section_headers = True  # Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.skip_non_songs = True  # Include hits thought to be non-songs (e.g. track lists)
genius.excluded_terms = ["(Remix)", "(Live)", "(Mixed)", "(FreeStyle)", "(Original Version)"]  # Exclude songs with these words in their title
genius.sleep_time = 1
genius.retries = 3

# Search for the artist and print their songs
artist = genius.search_artist(artist_name, sort="title")
print(artist.songs)

# Save the lyrics to a file
artist.save_lyrics()