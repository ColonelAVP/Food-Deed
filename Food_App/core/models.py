import random
from django.utils.translation import gettext
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import (
    Model,
    TextField,
    BooleanField,
    EmailField,
    CharField,
    JSONField,
    ForeignKey,
)

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
