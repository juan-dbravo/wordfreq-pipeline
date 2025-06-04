import sys
from pathlib import Path

# Add the root directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))


from s3_utils.s3_handler import upload_to_s3

upload_to_s3("data/raw_data/crime.txt", "wordfreq-bucket-gutenberg", "raw/crime.txt")
