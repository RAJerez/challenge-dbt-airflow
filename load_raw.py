from minio_lib import MinIO
from logger import Logger
from cfg import (
    BUCKET,
    ENDPOINT_URL,
    MINIO_ACCESS_KEY,
    MINIO_SECRET_KEY,
    SOURCE_PATH,
    paths_dict,
)

log = Logger()

bucket_name = BUCKET
endpoint_url = ENDPOINT_URL
aws_access_key = MINIO_ACCESS_KEY
aws_secret_key = MINIO_SECRET_KEY


def create_bucket_load_raw():

    minio_client = MinIO(BUCKET, endpoint_url, aws_access_key, aws_secret_key)

    minio_client.create_bucket()

    for name, file in paths_dict.items():
        local_file_path = SOURCE_PATH + file
        key = f"bronze/{file}"
        minio_client.load_files(local_file_path, key)
        log.info(f"Loading file {name}...")


if __name__ == "__main__":
    create_bucket_load_raw()


## Upload a file to the bucket
# s3.upload_file(file, bucket-name, key)

## List objects in the bucket
# response = s3.list_objects(Bucket='mybucket')
# for obj in response.get('Contents', []):
#    print(obj['Key'])
