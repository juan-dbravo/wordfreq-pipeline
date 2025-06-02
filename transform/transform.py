
from pathlib import Path
from transform.transform_utils import (
    read_text_file,
    clean_text_file,
    tokenize_text,
    lemmatize_tokens,
    count_frequency,
)

def run_pipeline(file_path: Path, preview: bool = True):

    """
    Runs the full text transformation pipeline and returns a DataFrame.

    Args:
        file_path (Path): Path to the .txt input file.
        preview (bool): Whether to show preview at each step.

    Returns:
        pd.DataFrame: Two-column DataFrame of lemmatized tokens with frequency
    """

    text = read_text_file(file_path, preview)
    cleaned = clean_text_file(text, preview)
    tokens = tokenize_text(cleaned, preview)
    lemmatized = lemmatize_tokens(tokens, preview)
    df = count_frequency(lemmatized, preview)
    return df

if __name__ == "__main__":
    input_path = Path(__file__).parent.parent / "data/raw_data/robin_hood.txt"
    df = run_pipeline(input_path, preview=True)

    # Save result
    output_path = Path(__file__).parent.parent / "data/clean_data/robin_lemmas.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nSaved to: {output_path}\n")
