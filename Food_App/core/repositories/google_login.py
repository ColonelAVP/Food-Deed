# Dependencies for Calendar API utility
from typing import final
from django.contrib.auth.models import User
import requests
from core.models import CustomUser
from core.helpers.base import get_or_create
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from core.helpers.constants import GoogleKeys
# from base64 import urlsafe_b64decode
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow


def get_consent_url():
    """
    Function prompts google consent window
    Returns:
        string: consent url
    """
    flow = Flow.from_client_secrets_file(
        "core/helpers/google_creds.json",
        scopes=[
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile",
        ],
        redirect_uri=GoogleKeys.CALLBACK_URL,
    )

    # Tell the user to go to the authorization URL.
    auth_url, _ = flow.authorization_url(prompt="consent")
    if not auth_url:
        return False, "URL not Found"
    return True, auth_url


def get_consent_callback(access_code):
    """
    Function to get Access token, refresh token, EmailID from redirect URL
    Parameters:
        access code(string):
    Returns:
        Bool, Response(string)
    """

    print(f"access code ---->>>>{access_code}")

    api_url = GoogleKeys.USER_INFO_URL
    params = {
        "grant_type": "authorization_code",
        "code": access_code,
        "redirect_uri": GoogleKeys.CALLBACK_URL,
        "client_id": GoogleKeys.GOOGLE_CLIENT_ID,
        "client_secret": GoogleKeys.GOOGLE_CLIENT_SECRET,
    }
    token_response = requests.post(GoogleKeys.GOOGLE_TOKEN_URL, data=params)
    print(f"token response ----> {token_response.json()}")
    access_token = token_response.json().get("access_token")
    # print(access_token)
    user_info_response = requests.get(
        api_url,
        params={"access_token": access_token},
    )
    print(f"user_info_response---->{user_info_response.json()}")
    if user_info_response.status_code != 200:
        return False, "Google User Info not found"
    user_info_data = user_info_response.json()
    user_email = user_info_data.get("email")
    response = {
        "email": user_email,
    }
    return True, response
