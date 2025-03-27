from gensim.models import Word2Vec

import sys
import numpy as np
import os

import auxfunctions as auxF 

# Define a custom callback to log the loss

def train_word2vec_model(sentences, vector_size=100, window=5, min_count=2, workers=4, epochs=100, batch_words=100,callbacks=auxF.loss_logger):
    """
    Entrena un modelo Word2Vec en las oraciones dadas.
    Args:
        sentences (list of list of str): Lista de oraciones preprocesadas.
        vector_size (int): Dimensión de los embeddings.
        window (int): Tamaño de la ventana para contextos.
        min_count (int): Frecuencia mínima para incluir una palabra.
        workers (int): Número de hilos para entrenamiento.
    Returns:
        Word2Vec: Modelo Word2Vec entrenado.
    """
    model = Word2Vec(
        sentences=sentences,
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        workers=workers,
        sg=1,  # Skip-gram
        compute_loss=True,
        epochs=epochs,
        batch_words=batch_words,
        alpha=0.01,  # Initial learning rate
        min_alpha=0.0001,  # Minimum learning rate
        callbacks=[auxF.loss_logger] 
    )


    return model

def save_model(model, file_path):
    """
    Guarda el modelo entrenado en un archivo.
    Args:
        model (Word2Vec): Modelo Word2Vec entrenado.
        file_path (str): Ruta del archivo donde se guardará el modelo.
    """
    model.wv.save_word2vec_format(file_path,binary= False)
    auxF.write_tsv(file_path)  #extensión para visualización
    


def load_model(file_path):
    """
    Carga un modelo Word2Vec desde un archivo.
    Args:
        file_path (str): Ruta del archivo que contiene el modelo.
    Returns:
        Word2Vec: Modelo Word2Vec cargado.
    """
    return Word2Vec.load(file_path)



if __name__ == "__main__":
    # Configuración inicial
    os.chdir(r"G:\Mi unidad\24-25\docencia\iaa\practica")
    model_file = "word2vec.model"
    output_file = "most_similar_words_gensim.txt"

    # Paso 1: Cargar y preprocesar el corpus
    print("Cargando y preprocesando el corpus...")
    file=r"simpletext.txt"
    sentences=auxF.read_and_tokenize_wordvec(file,preprocess=auxF.preprocess)
    print(f"Cargadas {len(sentences)} oraciones del corpus.")

    # Paso 2: Entrenar el modelo Word2Vec
    print("Entrenando el modelo Word2Vec...")
    model = train_word2vec_model(sentences, vector_size=128, window=7, min_count=50, epochs=100, workers=4)

    # Paso 3: Guardar el modelo
    print(f"Guardando el modelo en {model_file}...")
    save_model(model, model_file)
    



    # Paso 4: Escribir las palabras más similares en un archivo
    print(f"Escribiendo palabras más similares en {output_file}...")
    auxF.write_most_similar_words_gensim(model, output_file)

    # Paso 5: Extraer embeddings para visualización
    print("Extrayendo embeddings para visualización...")
    words = [word for word in model.wv.index_to_key if word.isalpha()][:100]  # Top 100 palabras alfabéticas
    word_embeddings = np.array([model.wv[word] for word in words])

    # Paso 6: Visualizar con PCA
    print("Visualizando embeddings con PCA...")
    auxF.visualize_embeddings_gensim(model, min_frequency=50, method="pca")

    # Paso 7: Visualizar con t-SNE
    print("Visualizando embeddings con t-SNE...")
    auxF.visualize_embeddings_gensim(model, min_frequency=50, method="tsne")





    
   

  