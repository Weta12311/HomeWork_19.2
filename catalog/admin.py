from django.contrib import admin
from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Version)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("product", "version_number", "name", "version_sign")
    list_filter = ("product",)
    search_fields = ("product",)
