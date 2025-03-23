import nltk
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
from nltk.util import ngrams
import os
import matplotlib
import argparse

# Configuración de matplotlib para evitar problemas con la interfaz gráfica
matplotlib.use("Agg")
# Descargar los recursos necesarios de NLTK
nltk.download('punkt')

def cargar_texto(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        texto = f.read()
    return texto

def analizar_texto(texto):
    # Tokenización
    oraciones = nltk.sent_tokenize(texto)
    palabras = nltk.word_tokenize(texto.lower())
    palabras = [palabra for palabra in palabras if palabra.isalpha()]

    # Unigramas, Bigrams y Trigrams
    unigramas = palabras
    bigramas = list(ngrams(palabras, 2))
    trigramas = list(ngrams(palabras, 3))

    # Frecuencias
    freq_unigramas = Counter(unigramas).most_common(10)
    freq_bigramas = Counter(bigramas).most_common(10)
    freq_trigramas = Counter(trigramas).most_common(10)

    #  Gráficos de barras para n=1,2,3
    plt.figure(figsize=(16, 8))

    # Unigramas
    plt.subplot(1, 3, 1)
    palabras_labels, conteos = zip(*freq_unigramas)
    plt.barh(palabras_labels, conteos, color='skyblue')
    plt.title('Top 10 Unigramas')
    plt.gca().invert_yaxis()

    # Bigrams
    plt.subplot(1, 3, 2)
    bigram_labels, bigram_counts = zip(*freq_bigramas)
    bigram_texts = [' '.join(b) for b in bigram_labels]
    plt.barh(bigram_texts, bigram_counts, color='mediumseagreen')
    plt.title('Top 10 Bigrams')
    plt.gca().invert_yaxis()

    # Trigrams
    plt.subplot(1, 3, 3)
    trigram_labels, trigram_counts = zip(*freq_trigramas)
    trigram_texts = [' '.join(t) for t in trigram_labels]
    plt.barh(trigram_texts, trigram_counts, color='salmon')
    plt.title('Top 10 Trigrams')
    plt.gca().invert_yaxis()

    plt.tight_layout()
    plt.savefig("frecuencias_ngrams.png")

    # 🌥️ Nube de palabras
    plt.figure(figsize=(6, 4))
    nube = WordCloud(width=400, height=300, background_color='white', colormap='plasma').generate(' '.join(palabras))
    plt.imshow(nube, interpolation='bilinear')
    plt.axis('off')
    plt.title('Nube de Palabras')
    plt.tight_layout()
    plt.savefig("nube_palabras.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analizar texto y generar visualizaciones.")
    parser.add_argument("working_directory", type=str, help="Directorio de trabajo")
    parser.add_argument("file_path", type=str, help="Ruta del archivo a analizar")

    args = parser.parse_args()

    # Configuración del directorio de trabajo
    os.chdir(args.working_directory)

    # Cargar y analizar el texto
    texto = cargar_texto(args.file_path)
    analizar_texto(texto)