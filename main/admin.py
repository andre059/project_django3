from django.contrib import admin

from main.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'image', 'is_active',)
    search_fields = ('name', 'category', 'image', 'is_active',)
    list_filter = ('is_active',)

