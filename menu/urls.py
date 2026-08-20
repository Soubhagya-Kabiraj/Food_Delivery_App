from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('food/<int:item_id>/', views.food_detail_view, name='food_detail'),
]
