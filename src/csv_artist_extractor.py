import csv

def extract_artists(input_csv, output_txt):
    artists = set()  # Use a set to store unique artist names

    # Read the CSV file
    with open(input_csv, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Split multiple artists by commas and strip whitespace
            artist_names = row['Artist Name(s)'].split(',')
            for artist in artist_names:
                artists.add(artist.strip())

    # Write the unique artist names to a plain text file
    with open(output_txt, 'w', encoding='utf-8') as txtfile:
        for artist in sorted(artists):  # Sort alphabetically
            txtfile.write(artist + '\n')

# Example usage
input_csv = './gofio_pltano_y_salitre___.csv'
output_txt = './nuevos.txt'
extract_artists(input_csv, output_txt)