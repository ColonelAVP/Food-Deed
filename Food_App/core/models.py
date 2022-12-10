from pickle import TRUE
import random
from sys import maxsize
from typing import Text
from django.utils.translation import gettext
from django.db.models import Model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import (
    Model,
    TextField,
    BooleanField,
    EmailField,
    CharField,
    JSONField,
    ForeignKey,
    ImageField,
    FloatField,
    CASCADE,
    ManyToManyField,
    IntegerField,
)
from core.helpers.constants import FoodCategoryTypes, FoodSubCategoryTypes
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from .managers import CustomUserManager


def generate_user_id():
    """Generates a 10 digit alphanumeric unique key"""
    user_id = "".join(
        [random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVXYZ") for i in range(10)]
    )
    return user_id


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user Model --> stores user information in respective fields
    """

    user_id = CharField(max_length=10, default=generate_user_id, unique=True, null=True)
    email = EmailField(max_length=50)
    mobile_number = CharField(max_length=12, unique=True)
    password = CharField(max_length=200)
    first_name = CharField(max_length=100, null=True, blank=True)
    last_name = CharField(max_length=100, null=True, blank=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    created_date = CreationDateTimeField(null=True)
    updated_date = ModificationDateTimeField(null=True)
    remark = TextField(blank=True, null=True)

    USERNAME_FIELD = "mobile_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.mobile_number)


class Food(Model):
    """
    Food model --> Contains details of a food item
    """

    food_category_choices = (
        (FoodCategoryTypes.ASIAN, FoodCategoryTypes.ASIAN),
        (FoodCategoryTypes.CHINESE, FoodCategoryTypes.CHINESE),
        (FoodCategoryTypes.ITALIAN, FoodCategoryTypes.ITALIAN),
        (FoodCategoryTypes.MEXICAN, FoodCategoryTypes.MEXICAN),
        (FoodCategoryTypes.HAMBURGER, FoodCategoryTypes.HAMBURGER),
    )

    food_subcategory_choices = (
        (FoodSubCategoryTypes.VEG, FoodSubCategoryTypes.VEG),
        (FoodSubCategoryTypes.NON_VEG, FoodSubCategoryTypes.NON_VEG),
    )

    name = CharField(max_length=30)
    image = ImageField(upload_to="food_images/", null=True, blank=True)
    category = CharField(
        max_length=10, choices=food_category_choices, default=FoodCategoryTypes.ASIAN
    )
    sub_category = CharField(
        max_length=10,
        choices=food_subcategory_choices,
        default=FoodSubCategoryTypes.VEG,
    )
    price = FloatField(max_length=10)
    # TODO CART (Many-to-many)
    description = CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(f"{self.name} :: {self.sub_category}")


class Review(Model):
    """Review model for Restaurants where user can add multiple reviews."""

    rating_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    review = TextField(max_length=500, blank=True, null=True)
    rating = IntegerField(max_length=1, choices=rating_choices, blank=True, null=True)


class Restaurant(Model):
    """
    Restaurant model --> saves Restaurant instances in Database
    """

    name = CharField(max_length=150)
    address = CharField(max_length=350)
    key = CharField(max_length=5, unique=True)
    phone_number = CharField(max_length=12, unique=True)
    availability = BooleanField(default=True)
    foods = ManyToManyField(Food, blank=True)
    reviews = ManyToManyField(Review, blank=True)
    description = CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.name)


# class Cart(Model):
#     """
#     Cart model --> Cart handles all the cart functionality
#     """

#     user = ForeignKey(CustomUser, on_delete=True)
#     food_item = ForeignKey(Food, on_delete=True)
