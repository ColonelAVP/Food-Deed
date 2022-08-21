from django.urls import path
from .views import CustomUserController
from knox import views as knox_views

urlpatterns = [
    path("register/", CustomUserController.register, name="user-register"),
    path("login/", CustomUserController.login, name="user-login"),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path(
        "google-login/",
        CustomUserController.get_consent_screen,
        name="google-consent-screen",
    ),
    path(
        "google-user-data",
        CustomUserController.get_consent_callback,
        name="google-consent-callback",
    ),
]
