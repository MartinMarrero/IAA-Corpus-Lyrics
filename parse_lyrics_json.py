import json


def extraer_lyrics_a_txt(json_path: str, output_path: str):
    with open(json_path, "r", encoding="utf-8") as f:
        datos = json.load(f)

    letras = [cancion.get("lyrics", "") for cancion in datos.get("songs", [])]
    texto_completo = "\n\n".join(letras)

    with open(output_path, "w", encoding="utf-8") as f_out:
        f_out.write(texto_completo)

    print(f"Letras guardadas en: {output_path}")


# Cambia las rutas si lo necesitas
if __name__ == "__main__":
    extraer_lyrics_a_txt("viejos.json", "letras_viejos.txt")
