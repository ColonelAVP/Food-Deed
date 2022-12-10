from core.models import Review
from core.models import Restaurant
from core.serializers.restaurant_serializer import (
    RestaurantSerializer,
    FoodSerializer,
)
import json


def get_all_restaurants(type=None):
    """
    get_all_restaurants function displays all restaurants list and categories veg or non-veg restaurants
    """
    restaurants = Restaurant.objects.all()
    data = RestaurantSerializer(restaurants, many=True).data
    restaurants_dict = json.dumps(data)
    if not restaurants_dict:
        return False, "Restaurants not found"
    return True, restaurants_dict


def get_restaurant(key=None):
    """
    get_restaurant function displays a restaurant that user has selected from restaurants list
    """
    if key:
        restaurants = Restaurant.objects.filter(key=key)
        reviews = restaurants.first().reviews
        print(list(reviews.values()))
        if not restaurants:
            return False, "Restaurant not found"
    else:
        restaurants = Restaurant.objects.all()
        if not restaurants:
            return False, "Restaurants not found"
    return True, restaurants.values()


def get_menu(key, veg: bool):
    """
    get_menu function displays all the foods available in certain restaurant
    or queries veg food only
    Takes 2 positional arguments
        key --> Restaurant Initials
        veg --> Boolean value
    returns menu
    """
    restaurant = Restaurant.objects.filter(key=key)
    foods = restaurant.first().foods
    if not foods:
        return False, "Food Not Found"
    response = []
    if veg:
        response = foods.filter(sub_category="VEG").values()
    else:
        response = foods.values()
    return True, response


def get_reviews(key):
    """
    get_reviews function return all the existing reviews of selected restaurant
    """
    restaurant = Restaurant.objects.filter(key=key)
    reviews = restaurant.first().reviews
    if not reviews.values():
        return False, "No reviews exist for the restaurant"
    return True, reviews.values()
