from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodItem

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'food_item')

    @property
    def total_price(self):
        return self.food_item.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.food_item.name} ({self.user.username})"
