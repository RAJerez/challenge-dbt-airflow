import boto3
from botocore.exceptions import ClientError
import logging

log = logging.getLogger()

# Set up MinIO client
s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minio_admin",
    aws_secret_access_key="minio_password",
)


def create_buckets() -> None:
    buckets = ["raw", "dbt"]
    for name in buckets:
        try:
            # Create a 'raw' bucket
            s3.create_bucket(Bucket=name)
            log.info(f"Bucket {name} created succesfully")

        except ClientError as e:
            log.info(f"Error: {e}")
    
def load_files() -> None:   
    s3.upload_file('/home/agustin/Documentos/minio-dbt-airflow/csv-data/bibliotecas.csv', 'raw', 'bibliotecas.csv')        



if __name__ == "__main__":
    create_buckets()
    load_files()


## Upload a file to the bucket
# s3.upload_file('myfile.txt', 'mybucket', 'myfile.txt')

## List objects in the bucket
# response = s3.list_objects(Bucket='mybucket')
# for obj in response.get('Contents', []):
#    print(obj['Key'])
