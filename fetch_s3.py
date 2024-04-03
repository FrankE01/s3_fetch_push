import os
from os import path
import boto3

s3 = boto3.client("s3", aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.environ.get('AWS_SECRET_KEY_ID'))

data_dir = path.dirname(path.abspath(__file__))+"/data/"
bucket_name = "company-pipeline-bucket"

response = s3.list_objects(Bucket=bucket_name)

files = [obj["Key"] for obj in response["Contents"]]

for file in files:
    parts = file.split("/")
    if len(parts) == 2:
        os.makedirs(path.join(data_dir, parts[0]))
        with open(path.join(data_dir, file), 'wb') as f:
            s3.download_fileobj(bucket_name, file, f)


print("S3 Download Completed")
