"""
This is a test script to build all the functions needed to transform .txt books 
downloaded from Project Guthemberg library.

For the moment I'll manage to clean an excerpt of Alice's adventures in wonderland,
named Alice.txt and saved in the raw_data folder.
"""

from pathlib import Path
import re
from typing import List
from collections import Counter

import pandas as pd
import spacy
import nltk
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")


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
    print("\n✅ Text succesfully recognized")
    if preview:
        print("\nPreview of raw file content:")
        print(text[:20])  # Show the first 500 characters
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
    print("\n✅ Text succesfully cleaned from punctuation and extra spaces")

    if preview:
        print("\nPreview of raw file content:")
        print(cleaned_text[:20])  # Show the first 500 characters

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
    print(f"\n✅ Tokenized {len(tokens)} words")

    if preview:
        print("\nPreview of tokens:")
        print(tokens[:10])

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

    print(f"\n✅ Removed {len(removed_tokens)} stopwords out of {len(tokens)} words")
    if preview:
        print(f"\nPreview of removed stopwords: {removed_tokens[:10]}")
        print(f"\nPreview after stopword removal: {filtered_tokens[:10]}")

    return filtered_tokens

def lemmatize_tokens(tokens: List[str], preview: bool = False) -> List[str]:
    """
    Lemmatizes tokens using spaCy's language model.

    Args:
        tokens (List[str]): A list of tokens (after cleaning and stopword removal).
        preview (bool): If True, shows original → lemmatized.

    Returns:
        List[str]: List of lemmatized tokens.
    """
    
    doc = nlp(" ".join(tokens))
    lemmatized = [token.lemma_ for token in doc]

    if preview:
        print("\nspaCy Lemmatization Preview:")
        for original, lemma in zip(tokens[:10], lemmatized[:10]):
            print(f"  {original:12} → {lemma}")

    return lemmatized

def count_frequency (lemmatized : List[str], preview: bool = False) -> pd.DataFrame:

    """
    Counts the frequency of lemmatized tokens and returns a DataFrame.

    Args:
        lemmatized (List[str]): List of lemmatized word tokens.
        preview (bool): Whether to print the top rows.

    Returns:
        pd.DataFrame: DataFrame with columns ['lemma', 'frequency']
    """

    word_counts = Counter(lemmatized)  # This turns the list into a dict.
    df = pd.DataFrame(word_counts.items(), columns=["lemma", "frequency"])
    
    print(f"\n✅ Final DataFrame shape: {df.shape}\n")
    if preview:
        print(df.head(10))
    return df


if __name__ == "__main__":
    # Example usage
    file_path = Path(__file__).parent.parent / "data/raw_data/Alice.txt" 
    try:
        text = read_text_file(file_path)
        cleaned_text = clean_text_file(text)
        tokens = tokenize_text(cleaned_text)
        filtered_tokens = remove_stopwords(tokens)
        lemmatized_tokens = lemmatize_tokens(filtered_tokens)
        data_frame = count_frequency(lemmatized_tokens)

    except Exception as e:
        print(f"Error: {e}")