import os
from os import path
import boto3

s3 = boto3.client("s3", aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.environ.get('AWS_SECRET_KEY_ID'))

data_dir = path.dirname(path.abspath(__file__))+"/data/"
bucket_name = "company-pipeline-bucket"

companies = [d for d in os.listdir(data_dir) if os.path.isdir(path.join(data_dir,d))]

for company in companies:

    files = [f for f in os.listdir(path.join(data_dir,company)) if f[-4:]==".csv"]
    
    for file in files:
        s3.upload_file(path.join(data_dir, company, file), bucket_name, f"{company}/{file}")

print("S3 Upload Completed")
