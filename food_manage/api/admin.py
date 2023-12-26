from django.contrib import admin

from .models import Category, SubCategory, Products, UserModel


@admin.register(Category, SubCategory, Products, UserModel)
class BlogAdmin(admin.ModelAdmin):
    pass