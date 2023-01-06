from django.contrib import admin
from .models import Customer, Product, Sale, Purchase
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Purchase)


class SaleAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'customer', 'cow_milk_quantity', 'buffalo_milk_quantity')
    list_filter = ['created_at']
    search_fields = ['customer']

admin.site.register(Sale, SaleAdmin)
