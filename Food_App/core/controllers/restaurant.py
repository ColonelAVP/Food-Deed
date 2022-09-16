from core.helpers.base import (
    BadRequestJSONResponse,
    SuccessJSONResponse,
    NotFoundJSONResponse,
    UnauthorizedJSONResponse,
)
from core.repositories.restaurant import (
    get_all_restaurants,
    get_restaurant,
    get_menu,
    get_reviews,
)
from rest_framework.decorators import api_view


class RestaurantController:
    @staticmethod
    @api_view(["GET"])
    def get_all_restaurants(request):
        """
        get_all_restaurants() API retrieves all the restaurants present in Database
        """
        success, response = get_all_restaurants()
        if not success:
            return BadRequestJSONResponse(message=response)
        return SuccessJSONResponse(response)

    @staticmethod
    @api_view(["GET"])
    def get_restaurant(request):
        """
        get_restaurant() API displays information of selected restaurant
        """
        # TODO convert to Get request
        restaurant_key = request.GET.get("restaurant_key")
        print(restaurant_key)
        success, response = get_restaurant(key=restaurant_key)
        if not success:
            return BadRequestJSONResponse(message=response)
        return SuccessJSONResponse(response)

    @staticmethod
    @api_view(["GET"])
    def get_restaurant_menu(request):
        """
        get_menu() retrieves all the present food items from selected restaurant
        Additional filter of displaying only veg foods
        """
        key = request.GET.get("key")
        veg = request.GET.get("veg")
        success, response = get_menu(key=key, veg=veg)
        if not veg:
            success, response = get_menu(key=key, veg=False)
        if not success:
            return BadRequestJSONResponse(message=response)
        return SuccessJSONResponse(response)

    @staticmethod
    @api_view(["GET"])
    def get_all_reviews(request):
        """
        get_all_reviews() displays all the existing reviews of restaurant by key
        """
        key = request.GET.get("key")
        success, response = get_reviews(key=key)
        if not success:
            return BadRequestJSONResponse(message=response)
        return SuccessJSONResponse(response)
