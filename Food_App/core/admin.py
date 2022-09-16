from django.contrib import admin
from .models import CustomUser, Food, Restaurant, Review

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Food)
admin.site.register(Restaurant)
admin.site.register(Review)


class ReviewInline(admin.StackedInline):
    model = Review


class RestaurantAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
