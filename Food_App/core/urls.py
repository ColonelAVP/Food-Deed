from django.urls import path
from .views import CustomUserController, RestaurantController
from knox import views as knox_views

urlpatterns = [
    ### START LOGIN URLS
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
    ### END LOGIN URLS
    ### START RESTAURANTS URLS
    # path(
    #     "get-all-restaurants/",
    #     RestaurantController.get_all_restaurants,
    #     name="get-all-restaurants",
    # ),
    path(
        "get-restaurant/",
        RestaurantController.get_restaurant,
        name="get-restaurant",
    ),
    path(
        "get-restaurant-menu/",
        RestaurantController.get_restaurant_menu,
        name="get-restaurant-menu",
    ),
    path(
        "get-reviews/",
        RestaurantController.get_all_reviews,
        name="get-all-reviews",
    ),
]
