from google.cloud import storage, exceptions
import datetime
import google.auth
from google.oauth2 import service_account
import config

config_dict = config.merge()
credentials = service_account.Credentials.from_service_account_file(config_dict["service_account_filepath"])
if __name__ == "__main__":
    #using default credentials and project 
    client = storage.Client(project = "uiuc-ncsa-mayogenomics", credentials=credentials)
    new_bucket = None
    try:
        new_bucket = client.create_bucket(config_dict["bucket_name"])
    except exceptions.Conflict:
        new_bucket = client.get_bucket(config_dict["bucket_name"])
    my_blob = new_bucket.blob(config_dict["blob_name"])
    my_blob.upload_from_filename(config_dict['upload_filepath'])
    new_bucket.delete(force=True, client=client)
   