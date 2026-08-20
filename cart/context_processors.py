from .models import Cart

def cart_count(request):
    total_count = 0
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        total_count = sum(item.quantity for item in cart_items)
    return {'cart_count': total_count}
