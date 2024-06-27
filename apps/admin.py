from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('category',)


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
