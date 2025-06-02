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
import logging

nlp = spacy.load("en_core_web_sm")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s -%(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

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
    logger.info("✅ Text successfully recognized")

    if preview:
        print("\nPreview of raw file content:")
        print(text[:20]) 
    return text

def clean_text_file(text: str, preview: bool = False) -> str:
    """
    Cleans a text string by:
    - Lowercasing all tokens
    - Removing numbers, punctuation, symbols, and alphanumeric garbage
    - Removing stopwords
    - Keeping only alphabetic words

    Args:
        text (str): Input text to clean.
        preview (bool): If True, prints the first 500 characters of the cleaned text.

    Returns:
        str: Cleaned version of the input text with valid word tokens.
    """
    doc = nlp(text)

    # Keep only lowercase alphabetic tokens (filter out numbers, punctuation, symbols)
    words = [
        token.text.lower()
        for token in doc
        if token.is_alpha and not token.is_stop
    ]

    cleaned_text = " ".join(words)

    logger.info("✅ Text successfully cleaned using spaCy")

    if preview:
        logger.debug("Preview of cleaned text: %s", cleaned_text[:20])

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
    logger.info(f"✅ Tokenized {len(tokens)} words")

    if preview:
        logger.debug("Preview of tokens: %s", tokens[:10])

    return tokens

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
    logger.info(f"✅ Total lemmatized: {len(lemmatized)}")
    logger.info(f"🔥 Extracted {len(set(lemmatized))} unique lemmas ")

    if preview:
        print("\nspaCy Lemmatization Preview:")
        for original, lemma in zip(tokens[:10], lemmatized[:10]):
            logger.info(f"  {original:12} → {lemma}")

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
    df = df.sort_values(by=["lemma","frequency"], ascending=[True, True])
    df = df.reset_index(drop=True)
    df.index += 1

    logger.info(f"✅ Final DataFrame shape: {df.shape}\n")
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
        lemmatized_tokens = lemmatize_tokens(tokens)
        data_frame = count_frequency(lemmatized_tokens)

    except Exception as e:
        logger.exception("Pipeline error")