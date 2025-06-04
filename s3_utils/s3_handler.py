
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

def upload_to_s3(local_path, bucket_name, s3_path):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_path, bucket_name, s3_path)
        print(f"✅ Uploaded {local_path} to s3://{bucket_name}/{s3_path}")
    except Exception as e:
        print(f"❌ Failed to upload: {e}")
