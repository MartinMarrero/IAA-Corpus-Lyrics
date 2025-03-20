from lyricsgenius import Genius

genius = Genius("API_KEY")

genius.verbose = True # Turn off status messages
genius.remove_section_headers = True # Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.skip_non_songs = True # Include hits thought to be non-songs (e.g. track lists)
genius.excluded_terms = ["(Remix)", "(Live)", "(Mixed)", "(FreeStyle)"] # Exclude songs with these words in their title
genius.sleep_time=1
genius.retries=3

artist = genius.search_artist("Mestisay", sort="title")
print(artist.songs)


artist.save_lyrics()