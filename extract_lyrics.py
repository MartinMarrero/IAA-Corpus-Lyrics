import json
import os
import argparse

def extract_lyrics_from_json(json_file, output_file):
    """
    Extracts lyrics from a JSON file and saves them to a plain text file.

    Args:
        json_file (str): Path to the JSON file containing lyrics.
        output_file (str): Path to the output text file.
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Extract lyrics from the JSON structure
        lyrics_list = []
        for song in data.get("songs", []):
            lyrics = song.get("lyrics", "").strip()
            if lyrics:  # Only include non-empty lyrics
                lyrics_list.append(lyrics)

        # Save the extracted lyrics to a text file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("\n\n".join(lyrics_list))  # Separate songs with double newlines

        print(f"Lyrics successfully extracted to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {json_file} was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {json_file}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Extract lyrics from a JSON file and save them to a text file.")
    parser.add_argument("json_file", help="Path to the input JSON file containing lyrics.")
    parser.add_argument("output_file", help="Path to the output text file where lyrics will be saved.")

    # Parse command-line arguments
    args = parser.parse_args()

    # Extract lyrics and save them to a text file
    extract_lyrics_from_json(args.json_file, args.output_file)