import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from flask import current_app
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io

SCOPES = ['https://www.googleapis.com/auth/drive']

def get_drive_service():
    creds = None
    token_file = 'token.json'

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)
    return service

def upload_file_to_drive(filepath, filename, mimetype="application/octet-stream"):
    service = get_drive_service()
    file_metadata = {'name': filename}
    media = MediaFileUpload(filepath, mimetype=mimetype)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file.get('id')

def list_drive_files():
    service = get_drive_service()
    results = service.files().list(pageSize=10, fields="files(id, name)").execute()
    return results.get('files', [])

def delete_drive_file(file_id):
    service = get_drive_service()
    service.files().delete(fileId=file_id).execute()

def download_drive_file(file_id, destination_path):
    service = get_drive_service()
    request = service.files().get_media(fileId=file_id)
    with open(destination_path, 'wb') as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
