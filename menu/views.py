from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Category, FoodItem

def home_view(request):
    categories = Category.objects.all()
    featured_items = FoodItem.objects.filter(is_featured=True, availability=True)[:6]
    if not featured_items.exists():
        featured_items = FoodItem.objects.filter(availability=True)[:6]
        
    context = {
        'categories': categories,
        'featured_items': featured_items,
    }
    return render(request, 'menu/home.html', context)

def menu_view(request):
    categories = Category.objects.all()
    selected_category_id = request.GET.get('category')
    search_query = request.GET.get('q')
    sort_by = request.GET.get('sort', 'default')

    items = FoodItem.objects.filter(availability=True)

    if selected_category_id:
        items = items.filter(category_id=selected_category_id)
        
    if search_query:
        items = items.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(ingredients__icontains=search_query)
        )

    if sort_by == 'price_low':
        items = items.order_by('price')
    elif sort_by == 'price_high':
        items = items.order_by('-price')
    elif sort_by == 'rating':
        items = items.order_by('-rating')
        
    context = {
        'categories': categories,
        'items': items,
        'selected_category_id': int(selected_category_id) if selected_category_id and selected_category_id.isdigit() else None,
        'search_query': search_query or '',
        'sort_by': sort_by,
    }
    return render(request, 'menu/menu.html', context)

def food_detail_view(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    ingredients_list = [ing.strip() for ing in item.ingredients.split(',')] if item.ingredients else []
    related_items = FoodItem.objects.filter(category=item.category, availability=True).exclude(id=item.id)[:4]

    context = {
        'item': item,
        'ingredients_list': ingredients_list,
        'related_items': related_items,
    }
    return render(request, 'menu/food_detail.html', context)
