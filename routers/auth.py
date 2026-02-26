from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow
import os

router = APIRouter()

CLIENT_SECRET_FILE = "client_secret.json"

SCOPES = ["https://www.googleapis.com/auth/drive"]

@router.get("/login")
def login():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE,
        scopes=SCOPES,
        redirect_uri="http://localhost:8000/auth/callback"
    )

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )

    return RedirectResponse(authorization_url)

@router.get("/callback")
def callback(code: str):
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE,
        scopes=SCOPES,
        redirect_uri="http://localhost:8000/auth/callback"
    )

    flow.fetch_token(code=code)
    credentials = flow.credentials

    return {
        "access_token": credentials.token,
        "refresh_token": credentials.refresh_token
    }