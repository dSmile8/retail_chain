from django.contrib import admin

from retail.models import Chain, Product, Contact


@admin.register(Chain)
class ChainAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts', 'parent', 'debt_to_supplier',)
    list_filter = ('contacts__city',)
    list_display_links = ('name', 'parent')

    actions = ['clear_debts']

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_debts(self, request, queryset):
        for company in queryset:
            company.debt_to_supplier = 0
            company.save()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release_date')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number', 'chain_line',)
