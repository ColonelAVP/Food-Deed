from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import Restaurant, Food


class RestaurantSerializer(ModelSerializer):
    """
    RestaurantSerializer serializes data for Restaurant model
    """

    class Meta:
        model = Restaurant
        fields = [
            "name",
            "address",
            "phone_number",
            "availability",
            "key",
            "description",
        ]


class FoodSerializer(ModelSerializer):
    """
    RestaurantFoodSerializer makes the foods field in restaurants model usable
    """

    class Meta:
        model = Food
        fields = "__all__"
