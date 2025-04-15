# Description: Conexión a la API de Google Sheets y Gmail
import gspread
import json
from google.oauth2.service_account import Credentials as ServiceAccountCredentials
from decouple import config

# Import the necessary libraries to access the Gmail API
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

# defining the scope of the application
scope_app =[
             'https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'
            ]  

scope_gmail =[            
             'https://www.googleapis.com/auth/gmail.readonly',
             'https://www.googleapis.com/auth/gmail.modify'
    ]
#Client mail getting from json credential
jsonFile        = open(config('SERVICE_ACCOUNT_GOOGLE_CREDENTIALS_PATH'))
datajson        = json.load(jsonFile)            
client_email    = datajson['client_email']

#credentials to the account
credServiceAccount = ServiceAccountCredentials.from_service_account_file(config('SERVICE_ACCOUNT_GOOGLE_CREDENTIALS_PATH'),scopes=scope_app) 

# authorize the clientsheet 
#client = gspread.authorize(credServiceAccount) 

# Authorize Google Sheets and Drive using OAuth 2.0
def authorize_google_sheets():
    creds = None
    # Check if token.json exists (to reuse the token)
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scope_app)

    # If no valid credentials are available, request authorization
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                config('AUTH_GOOGLE_CREDENTIALS_PATH'), scope_app
            )
            # Explicitly request offline access to get a refresh_token
            creds = flow.run_local_server(port=8080, access_type='offline', prompt='consent')

        # Save the credentials for the next run
        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())

    # Build the Google Sheets API client
    service = build('sheets', 'v4', credentials=creds)
    return service

# authorize the client gmail
def gmail_authorize():
    print(f'autorizando...{config("CREDENTIALS")}')
    """
    Autoriza el acceso a la API de Gmail y reutiliza el token si es posible.
    """
    credAuth = None
    # Reutiliza el token si existe
    if os.path.exists('token.json'):
        credAuth = Credentials.from_authorized_user_file('token.json', scope_gmail)
    
    # Si no hay credenciales válidas, solicita autorización
    if not credAuth or not credAuth.valid:
        if credAuth and credAuth.expired and credAuth.refresh_token:
            credAuth.refresh(Request())  # Renueva el token automáticamente
        else:
            flow = InstalledAppFlow.from_client_secrets_file(config("CREDENTIALS"), scope_gmail)
            credAuth = flow.run_local_server(port=0)
            # Guarda las credenciales para la próxima vez
            with open('token.json', 'w') as token_file:
                token_file.write(credAuth.to_json())

    # Construye el cliente de Gmail
    service = build('gmail', 'v1', credentials=credAuth)
    return service