from google.cloud.storage import blob, bucket
from helpers import get_file_name, get_file_location, create_location

def upload_blob(file_path: str, blob_url: str, bucket: bucket.Bucket) -> blob.Blob:
    '''
    Upload a blob to the bucket
    '''
    server_destination_path = get_file_location(blob_url)
    file_name = get_file_name(file_path)

    destination_blob_name = create_location(server_destination_path, file_name)

    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(file_path)
    return blob

def download_blob(blob: blob.Blob, local_destination_path: str) -> str:
    '''
    Download a blob from the bucket
    '''
    file_name = get_file_name(blob.name)
    temp_path = local_destination_path + file_name
    blob.download_to_filename(temp_path)
    return temp_path
