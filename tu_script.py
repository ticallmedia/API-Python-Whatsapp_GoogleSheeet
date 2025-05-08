from google.oauth2.service_account import Credentials
import gspread
from dotenv import load_dotenv
import os

load_dotenv()

def get_google_credentials_from_env():
    creds_dict = {
        "type": os.environ["GOOGLE_TYPE"],
        "project_id": os.environ["GOOGLE_PROJECT_ID"],
        "private_key_id": os.environ["GOOGLE_PRIVATE_KEY_ID"],
        "private_key": os.environ["GOOGLE_PRIVATE_KEY"].replace("\\n", "\n"),
        "client_email": os.environ["GOOGLE_CLIENT_EMAIL"],
        "client_id": os.environ["GOOGLE_CLIENT_ID"],
        "auth_uri": os.environ["GOOGLE_AUTH_URI"],
        "token_uri": os.environ["GOOGLE_TOKEN_URI"],
        "auth_provider_x509_cert_url": os.environ["GOOGLE_AUTH_PROVIDER_CERT_URL"],
        "client_x509_cert_url": os.environ["GOOGLE_CLIENT_CERT_URL"]
    }
    return Credentials.from_service_account_info(creds_dict)

# Ejemplo de acceso a Google Sheets
creds = get_google_credentials_from_env()
gc = gspread.authorize(creds)
sheet = gc.open("LogDeEventos").sheet1
print(sheet.get_all_records())
