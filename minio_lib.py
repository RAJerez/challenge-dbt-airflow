import boto3
from botocore.exceptions import ClientError
import logging

class MinIO:
    def __init__(self, bucket_name, endpoint_url, aws_access_key, aws_secret_key):
        self.bucket_name = bucket_name
        self.endpoint_url = endpoint_url
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_key,
            endpoint_url=self.endpoint_url
        )
        self.logger = logging.getLogger(__name__)
    
    def create_bucket(self) -> None:
        try:
            self.s3.create_bucket(Bucket=self.bucket_name)
            self.logger.info(f"Bucket {self.bucket_name} created successfully")
        except ClientError as e:
            self.logger.error(f"Error: {e}")
    
    
    def load_files(self, local_file_path: str, s3_key: str) -> None:
        try:
            self.s3.upload_file(local_file_path, self.bucket_name, s3_key)
            self.logger.info(f"File {local_file_path} uploaded to {self.bucket_name}/{s3_key}")
        except ClientError as e:
            self.logger.error(f"Error uploading file: {e}")