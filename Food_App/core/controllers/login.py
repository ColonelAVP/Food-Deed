import logging
from os import stat
from rest_framework.decorators import api_view
from core.models import CustomUser
from core.helpers.base import (
    BadRequestJSONResponse,
    SuccessJSONResponse,
    NotFoundJSONResponse,
    UnauthorizedJSONResponse,
    get_access_token,
    datetime_from_epoch,
)
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from django.utils import timezone
from django.core.cache import cache
from core.serializers.token_serializer import get_token_pair
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from core.repositories.google_login import (
    get_consent_url,
    get_consent_callback,
)


class CustomUserController:
    @staticmethod
    @api_view(["GET", "POST", "PUT", "DELETE"])
    def invalid_login(request):
        return UnauthorizedJSONResponse(message="Invalid Token")

    @staticmethod
    @api_view(["POST"])
    def register(request):
        """Creates a new user in database"""
        post_data = request.data
        mobile_number = post_data.get("mobile_number")
        password = post_data.get("password")
        email = post_data.get("email")
        first_name = post_data.get("first_name")
        last_name = post_data.get("last_name")
        if not mobile_number:
            return BadRequestJSONResponse(message="Mobile Number not found")
        user = CustomUser.objects.filter(mobile_number=mobile_number)
        if user.first():
            # TODO: return refresh and access token
            return SuccessJSONResponse(message="User already exists!")
        user = CustomUser.objects.create(
            mobile_number=mobile_number,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()
        _, token = AuthToken.objects.create(user)
        response = {"access_token": token, "message": "User created successfully!"}
        return SuccessJSONResponse(response)

    @staticmethod
    @api_view(["POST"])
    def login(request):
        """Logins an existing user in database"""
        serializer = AuthTokenSerializer(data=request.data)
        authenticated_user = serializer.is_valid()
        if not authenticated_user:
            return UnauthorizedJSONResponse(message="Invalid Credentials")
        user = serializer.validated_data["user"]
        _, token = AuthToken.objects.create(user)
        response = {"access_token": token}
        return SuccessJSONResponse(response)

    @staticmethod
    @api_view(["GET"])
    def get_consent_screen(request):
        """
        The get_consent_screen() API prompts google login consent window
        """
        success, response = get_consent_url()
        if not success:
            return NotFoundJSONResponse(message=response)
        return SuccessJSONResponse(response, message="Url generated succesfully")

    @staticmethod
    @api_view(["GET"])
    def get_consent_callback(request):
        """
        get_consent_callback() API gets a callback url on mentioned redirect url
        """
        access_code = request.GET.get("code")
        success, response = get_consent_callback(access_code=access_code)
        if not success:
            return NotFoundJSONResponse(message=response)
        user = CustomUser.objects.filter(email=response.get("email"))
        user = user.first()
        _, token = AuthToken.objects.create(user=user)
        response = {"access_token": token}
        return SuccessJSONResponse(response)
