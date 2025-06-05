"""
This script uploads a local raw text file (Crime and Punishment) to an S3 bucket
under the specified key. It uses the reusable `upload_to_s3` function from the
s3_utils.s3_handler module.

"""

import sys
from pathlib import Path

# Add the project root (wordfreq-pipeline/) to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import the batch upload function
from s3_utils.s3_handler import upload_all_txt_files

# Local folder containing .txt files
folder = "data/raw_data"

# S3 bucket details
bucket = "wordfreq-bucket-gutenberg"
s3_prefix = "raw"  # S3 subfolder path

# Upload all .txt files in the folder to S3
upload_all_txt_files(folder, bucket, s3_prefix)
