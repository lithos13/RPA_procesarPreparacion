# Description: Conexión a la API de Google Sheets y Gmail
from google.oauth2.service_account import Credentials as ServiceAccountCredentials
from decouple import config
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

# Define the scopes for the application
SCOPES = {
    "sheets": [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ],
    "gmail": [
        'https://www.googleapis.com/auth/gmail.readonly',
        'https://www.googleapis.com/auth/gmail.modify'
    ]
}

# General function to handle OAuth 2.0 authorization
def authorize_google_api(scope_key, token_file_name):
    """
    Authorizes access to a Google API using OAuth 2.0.

    :param scope_key: The key to select the appropriate scope (e.g., 'sheets', 'gmail').
    :param token_file_name: The name of the token file to store/reuse credentials.
    :return: The authorized Google API client.
    """
    creds = None
    # Check if token file exists (to reuse the token)
    if os.path.exists(token_file_name):
        creds = Credentials.from_authorized_user_file(token_file_name, SCOPES[scope_key])

    # If no valid credentials are available, request authorization
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                config('AUTH_GOOGLE_CREDENTIALS_PATH'), SCOPES[scope_key]
            )
            creds = flow.run_local_server(port=8080, access_type='offline', prompt='consent')

        # Save the credentials for the next run
        with open(token_file_name, 'w') as token_file:
            token_file.write(creds.to_json())

    return creds

# Authorize Google Sheets API
def authorize_google_sheets():
    """
    Authorizes access to the Google Sheets API.
    :return: The Google Sheets API client.
    """
    creds = authorize_google_api("sheets", "token_sheets.json")
    return build('sheets', 'v4', credentials=creds)

# Authorize Gmail API
def gmail_authorize():
    """
    Authorizes access to the Gmail API.
    :return: The Gmail API client.
    """
    print(f"Authorizing Gmail API using credentials from {config('AUTH_GOOGLE_CREDENTIALS_PATH')}")
    creds = authorize_google_api("gmail", "token_gmail.json")
    return build('gmail', 'v1', credentials=creds)