import boto3
import json

s3 = boto3.client('s3')
for each_bucket in s3.list_buckets()['Buckets']:
    print(f"S3 bucket {each_bucket['Name']} created on {each_bucket['CreationDate']}")
