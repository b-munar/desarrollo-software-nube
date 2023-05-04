from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/usr/src/app/linen-mason-384315-d051f5f132d3.json'

def upload_file(bucket_name, source_file, destination_file_name): 
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_file_name)
    blob.upload_from_file(file_obj=source_file, content_type=source_file.content_type)

def delete_file(bucket_name, file_dir): 
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blobs = bucket.list_blobs(prefix=file_dir)

    for blob in blobs:
        blob.delete()

def download_file(bucket_name, file_name, name): 
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.get_blob(file_name)
    content_type = blob.content_type
    file = blob.download_as_string()
    return file, content_type