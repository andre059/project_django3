from django.contrib import admin

from main.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    search_fields = ('name', 'category',)
    list_filter = ('is_active',)

