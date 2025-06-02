"""
This is a test script to build all the functions needed to transform .txt books 
downloaded from Project Guthemberg library.

For the moment I'll manage to clean an excerpt of Alice's adventures in wonderland,
named Alice.txt and saved in the raw_data folder.
"""

from pathlib import Path
import re
from typing import List
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

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

def remove_stopwords (tokens: List[str], preview: bool = False ) -> List[str]:
    """
    Removes common English stopwords from a list of tokens.

    Args:
        tokens (List[str]): A list of word tokens.
        preview (bool): If True, prints a preview of the result.

    Returns:
        List[str]: A new list with stopwords removed.
    """
    # Ensure corpus is available inside the function
    try:
        stop_words = set(stopwords.words('english'))
    except LookupError:
        print("⚠️  NLTK 'stopwords' corpus not found. Downloading it now...")
        nltk.download('stopwords')
        stop_words = set(stopwords.words('english'))

    removed_tokens= [word for word in tokens if word in stop_words]
    filtered_tokens = [word for word in tokens if word not in stop_words]

    print(" ✅ Stopwords succesfully removed")
    if preview:
        print(f"Preview of removed stopwords: {removed_tokens[:20]}")
        print(f"Preview after stopword removal: {filtered_tokens[:20]}")

    return filtered_tokens



def lemmatize_tokens(tokens: List[str], preview: bool = False) -> List[str]:
    """
    Reduces tokens to their base form using lemmatization.

    Args:
        tokens (List[str]): A list of word tokens (typically already cleaned).
        preview (bool): If True, prints a preview of lemmatization.

    Returns:
        List[str]: A list of lemmatized word tokens.
    """
    # Ensure corpus is available inside the function
    try:
        nltk.data.find('corpora/wordnet')
    except LookupError:
        print("⚠️  NLTK 'wordnet' corpus not found. Downloading...")
        nltk.download('wordnet')

    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(token) for token in tokens]

    if preview:
        print(" Preview of lemmatization:")
        for original, lemma in zip(tokens[:20], lemmatized[:20]):
            print(f"  {original} → {lemma}")

    return lemmatized

if __name__ == "__main__":
    # Example usage
    file_path = Path(__file__).parent.parent / "data/raw_data/Alice.txt"  # Replace with your actual file path
    try:
        text = read_text_file(file_path, True)
        cleaned_text = clean_text_file(text, True)
        tokens = tokenize_text(cleaned_text, True)
        filtered_tokens = remove_stopwords(tokens, True)
        lemnatized_tokens = lemmatize_tokens(filtered_tokens, True)

    except Exception as e:
        print(f"Error: {e}")