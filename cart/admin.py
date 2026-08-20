from django.contrib import admin
from .models import Cart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'food_item', 'quantity', 'created_at')
    list_filter = ('user',)
