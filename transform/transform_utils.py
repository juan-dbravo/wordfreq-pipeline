"""
This is a test script to build all the functions needed to transform .txt books 
downloaded from Project Guthemberg library.

For the moment I'll manage to clean an excerpt of Alice's adventures in wonderland,
named Alice.txt and saved in the raw_data folder.
"""


from pathlib import Path
import re
from typing import List

def read_text_file(file_path: Path, preview: bool = False) -> str:
    """
    Reads the content of a .txt file and returns it as a string.

    Args:
        file_path (Path): Path to the text file.
        preview (bool): If True, prints the first 500 characters of the file.

    Returns:
        str: Contents of the file.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    text = file_path.read_text(encoding='utf-8')
    print(" ✅ Text succesfully recognized")
    if preview:
        print("Preview of raw file content:")
        print(text[:500])  # Show the first 500 characters
    return text

def clean_text_file(text: str, preview: bool = False ) :
    """
    Cleans a text string by:
    - Lowercasing all characters
    - Removing punctuation marks
    - Normalizing whitespace

    Args:
        text (str): Input text to clean.
        preview (bool): If True, prints the first 500 characters of the cleaned text.

    Returns:
        str: Cleaned version of the input text.
    """
    text = text.lower()
    text = re.sub(r"[.,!?;:¿¡()\"“”‘’'-]", "", text)  # Remove punctuation
    cleaned_text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    print(" ✅ Text succesfully cleaned")

    if preview:
        print("Preview of raw file content:")
        print(cleaned_text[:500])  # Show the first 500 characters

    return cleaned_text

def tokenize_text (cleaned_text: str, preview: bool = False) -> List[str]:
    """
    Splits a cleaned text string into a list of word tokens.

    Args:
        text(str): The cleaned input text (no punctuation).
        preview (bool): If True, prints the first 20 tokens.

    Returns:
        List[str]: The list of lowercase word tokens.
    """
    tokens = cleaned_text.split()
    print(" ✅ Text succesfully tokenized")

    if preview:
        print("Preview of tokens:")
        print(tokens[:20])

    return tokens





if __name__ == "__main__":
    # Example usage
    file_path = Path(__file__).parent.parent / "data/raw_data/Alice.txt"  # Replace with your actual file path
    try:
        text = read_text_file(file_path)
        cleaned_text = clean_text_file(text)
        tokens = tokenize_text(cleaned_text, True)
    except Exception as e:
        print(f"Error: {e}")