from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv
from pathlib import Path
import os

# Get the current script's directory (relative to where the script is run)
current_directory = Path(__file__).parent
dotenv_path = current_directory / 'config' / '.env'

# Load environment variables from the .env file
load_dotenv(dotenv_path=dotenv_path)

# Azure Blob Storage Configuration
AZURE_CONNECTION_STRING = os.getenv('AZURE_CONNECTION_STRING')
CONTAINER_NAME = 'user-profile-pictures'

# Create an instance of BlobServiceClient
blob_service_client = BlobServiceClient. \
    from_connection_string(AZURE_CONNECTION_STRING)


# Function to upload image to Azure Blob Storage
def upload_file_to_blob(file_path: str, file_name: str):
    blob_client = blob_service_client. \
        get_blob_client(container=CONTAINER_NAME, blob=file_name)

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    return f"https://{blob_service_client.account_name}. \
        blob.core.windows.net/{CONTAINER_NAME}/{file_name}"
