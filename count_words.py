def count_words_in_file(file_path: str) -> int:
    """
    Counts the number of words in a given text file.

    Args:
        file_path (str): Path to the text file.

    Returns:
        int: Total number of words in the file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            # Split the text into words using whitespace as a delimiter
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

if __name__ == "__main__":
    # Change the file path to the location of your text file
    file_path = "letras_viejos.txt"
    word_count = count_words_in_file(file_path)
    print(f"Total number of words in the file: {word_count}")