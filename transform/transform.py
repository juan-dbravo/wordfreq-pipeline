
from pathlib import Path
import logging
from transform.transform_utils import (
    read_text_file,
    clean_text_file,
    tokenize_text,
    lemmatize_tokens,
    count_frequency,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s -%(message)s",
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def run_pipeline(file_path: Path, preview: bool = True):

    """
    Runs the full text transformation pipeline and returns a DataFrame.

    Args:
        file_path (Path): Path to the .txt input file.
        preview (bool): Whether to show preview at each step.

    Returns:
        pd.DataFrame: Two-column DataFrame of lemmatized tokens with frequency
    """
    logger.info(f"Starting pipeline for file: {file_path}")

    text = read_text_file(file_path, preview)
    logger.debug(f"Original text read. Length: {len(text)}")

    cleaned = clean_text_file(text, preview)
    logger.debug("Text cleaned.")

    tokens = tokenize_text(cleaned, preview)
    logger.debug(f"Tokenized text. Token count: {len(tokens)}")

    lemmatized = lemmatize_tokens(tokens, preview)
    logger.debug(f"Lemmatized tokens. Count: {len(lemmatized)}")

    df = count_frequency(lemmatized, preview)
    logger.info(f"Pipeline complete. Unique lemmas: {len(df)}")

    return df

if __name__ == "__main__":
    input_path = Path(__file__).parent.parent / "data/raw_data/robin_hood.txt"
    df = run_pipeline(input_path, preview=True)

    try:
        df = run_pipeline(input_path, preview=True)
    except Exception as e:
        logger.exception("Pipeline failed due to an unexpected error.")
        raise

    # Save result
    output_path = Path(__file__).parent.parent / "data/clean_data/robin_lemmas.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    
    logger.info(f"Saved output to: {output_path}")