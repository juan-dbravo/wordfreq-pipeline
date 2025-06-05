
"""
s3_handler.py is a utility module — 
a centralized Python file where I define all the functions that interact with AWS S3, such as:

- Uploading files
- Downloading files
- Listing S3 contents
- Deleting S3 objects
- Managing folder paths inside buckets

"""
import boto3
from pathlib import Path

def upload_to_s3(local_path, bucket_name, s3_path):
    """
    Upload a single file to an S3 bucket.

    Args:
        local_path (Path or str): Local file path.
        bucket_name (str): Name of the S3 bucket.
        s3_path (str): Destination key (path) in the S3 bucket.
    """
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_path, bucket_name, s3_path)
        print(f"✅ Uploaded {local_path} to s3://{bucket_name}/{s3_path}")
    except Exception as e:
        print(f"❌ Failed to upload: {e}")

def upload_all_txt_files(folder_path, bucket_name, s3_prefix=""):
    """
    Upload all .txt files from a local folder to an S3 bucket.

    Args:
        folder_path (str or Path): Local folder containing .txt files.
        bucket_name (str): Name of the S3 bucket.
        s3_prefix (str): Optional prefix (like a folder) for the S3 keys.
    """
    folder = Path(folder_path)

    if not folder.exists():
        print(f"❌ Folder {folder_path} does not exist.")
        return

    for file_path in folder.iterdir():
        # Process only regular .txt files
        if file_path.suffix == ".txt" and file_path.is_file():
            # Construct S3 key: prefix/filename or just filename
            s3_key = f"{s3_prefix}/{file_path.name}" if s3_prefix else file_path.name
            upload_to_s3(file_path, bucket_name, s3_key)
