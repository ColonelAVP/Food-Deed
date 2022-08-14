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
from django.utils.translation import gettext

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user Model --> stores user information in respective fields
    """

    email = EmailField(max_length=50, unique=True)
    mobile_number = CharField(max_length=12)
    password = CharField(max_length=200)
    first_name = CharField(max_length=100, null=True, blank=True)
    middle_name = CharField(max_length=100, null=True, blank=True)
    last_name = CharField(max_length=100, null=True, blank=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    created_date = CreationDateTimeField(null=True)
    updated_date = ModificationDateTimeField(null=True)
    remark = TextField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)
