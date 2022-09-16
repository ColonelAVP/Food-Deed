from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import Restaurant, Review


class ReviewSerializer:
    """
    Review serializer serializes the instances of Review Model
    """

    class Meta:
        model = Review
        fields = "__all__"
