from django.contrib import admin

from retail.models import Chain, Product, Contact


@admin.register(Chain)
class ChainAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts', 'parent', 'debt_to_supplier',)
    # list_filter = ('price',)
    # search_fields = ('title', 'price', 'user',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release_date')
    # list_filter = ('user', 'services', 'result')
    # search_fields = ('user', 'services', 'result')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('chain', 'email', 'country', 'city', 'street', 'house_number',)
