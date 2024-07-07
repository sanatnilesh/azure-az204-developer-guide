from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, ContentSettings

def get_blob_service_client_token_credential():
    # TODO: Replace <storage-account-name> with your actual storage account name
    account_url = "https://blobstoragesanat.blob.core.windows.net/"
    credential = DefaultAzureCredential()

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=credential)
    
    return blob_service_client

def list_containers(blob_service_client: BlobServiceClient):
    containers = blob_service_client.list_containers(include_metadata=True)
    for container in containers:
        print(container['name'], container['metadata'])

def list_blobs_flat(blob_service_client: BlobServiceClient, container_name):
    container_client = blob_service_client.get_container_client(container=container_name)

    blob_list = container_client.list_blobs()

    for blob in blob_list:
        return blob.name

def set_properties(blob_service_client: BlobServiceClient, container_name, blob_impage_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_impage_name)

    # Get the existing blob properties
    properties = blob_client.get_blob_properties()

    # Set the content_type and content_language headers, and populate the remaining headers from the existing properties
    blob_headers = ContentSettings(content_type=properties.content_settings.content_type,
                                   content_encoding=properties.content_settings.content_encoding,
                                   content_language="en-CA",
                                   content_disposition=properties.content_settings.content_disposition,
                                   cache_control=properties.content_settings.cache_control,
                                   content_md5=properties.content_settings.content_md5)
    
    blob_client.set_http_headers(blob_headers)

def get_properties(blob_service_client: BlobServiceClient, container_name, blob_impage_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_impage_name)

    properties = blob_client.get_blob_properties()

    print(f"Blob type: {properties.blob_type}")
    print(f"Blob size: {properties.size}")
    print(f"Content type: {properties.content_settings.content_type}")
    print(f"Content language: {properties.content_settings.content_language}")

def set_metadata(blob_service_client: BlobServiceClient, container_name, blob_impage_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_impage_name)

    # Retrieve existing metadata, if desired
    blob_metadata = blob_client.get_blob_properties().metadata

    more_blob_metadata = {'name': 'sanat', 'lastname': 'dhobi'}
    blob_metadata.update(more_blob_metadata)

    # Set metadata on the blob
    blob_client.set_blob_metadata(metadata=blob_metadata)

def get_metadata(blob_service_client: BlobServiceClient, container_name, blob_impage_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_impage_name)

    # Retrieve existing metadata, if desired
    blob_metadata = blob_client.get_blob_properties().metadata

    for k, v in blob_metadata.items():
        print(k, v)

blobServiceClient = get_blob_service_client_token_credential()
list_containers(blobServiceClient)
#container name hard coded, which is createed on Azure Portal.
blob_impage_name = list_blobs_flat(blobServiceClient, 'sanat')
set_properties(blobServiceClient, 'sanat', blob_impage_name)
get_properties(blobServiceClient, 'sanat', blob_impage_name)
set_metadata(blobServiceClient, 'sanat', blob_impage_name)
get_metadata(blobServiceClient, 'sanat', blob_impage_name)