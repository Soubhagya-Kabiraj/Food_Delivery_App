from django.contrib import admin
from .models import Category, FoodItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'rating', 'availability', 'is_featured')
    list_filter = ('category', 'availability', 'is_featured')
    search_fields = ('name', 'description')
    list_editable = ('price', 'availability', 'is_featured', 'rating')
