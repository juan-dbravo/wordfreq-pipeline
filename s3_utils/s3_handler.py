import boto3

def upload_to_s3(local_path, wordfreq-bucket-gutenberg, s3_path):
    s3 = boto3.client('s3')
    s3.upload_file(local_path, wordfreq-bucket-gutenberg, s3_path)
    print(f"Uploaded {local_path} to s3://{wordfreq-bucket-gutenberg}/{s3_path}")

"""
from s3_utils.s3_handler import upload_to_s3

upload_to_s3('data/raw/hamlet.txt', 'wordfreq-bucket-gutenberg', 'raw/gutenberg/hamlet.txt')

"""