import json


def extraer_lyrics_a_txt(json_path: str, output_path: str):
    with open(json_path, "r", encoding="utf-8") as f:
        datos = json.load(f)

    # Initialize an empty list to store all the lyrics
    letras = []

    # Iterate through each artist and their songs
    for artist, songs in datos.items():
        for cancion in songs:
            # Get the lyrics of the song, defaulting to an empty string if not present
            letra = cancion.get("lyrics", "")
            if letra:  # Only add non-empty lyrics
                letras.append(letra)

    # Join all the lyrics with two newlines between them
    texto_completo = "\n\n".join(letras)

    # Write the combined lyrics to the output file
    with open(output_path, "w", encoding="utf-8") as f_out:
        f_out.write(texto_completo)

    print(f"Letras guardadas en: {output_path}")


# Cambia las rutas si lo necesitas
if __name__ == "__main__":
    extraer_lyrics_a_txt("viejos.json", "letras_viejos.txt")