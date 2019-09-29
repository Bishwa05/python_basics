from django.contrib import admin
from .models import Product, Offer

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


# Manage product in admin area

admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
