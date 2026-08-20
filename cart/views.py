from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from menu.models import FoodItem
from .models import Cart

@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    subtotal = sum(item.total_price for item in cart_items)
    delivery_fee = 50.00 if cart_items.exists() else 0.00
    grand_total = float(subtotal) + delivery_fee

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'delivery_fee': delivery_fee,
        'grand_total': grand_total,
    }
    return render(request, 'cart/cart.html', context)

@login_required
def add_to_cart(request, item_id):
    food_item = get_object_or_404(FoodItem, id=item_id, availability=True)
    quantity = int(request.POST.get('quantity', 1))

    if quantity < 1:
        quantity = 1

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        food_item=food_item,
        defaults={'quantity': quantity}
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()
        messages.success(request, f"Updated {food_item.name} quantity in your cart.")
    else:
        messages.success(request, f"Added {food_item.name} to your cart.")

    return redirect(request.META.get('HTTP_REFERER', 'cart_detail'))

@login_required
def update_cart_quantity(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    action = request.POST.get('action')

    if action == 'increase':
        cart_item.quantity += 1
        cart_item.save()
    elif action == 'decrease':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
            messages.info(request, f"Removed {cart_item.food_item.name} from your cart.")
            return redirect('cart_detail')
    elif action == 'set':
        qty = int(request.POST.get('quantity', 1))
        if qty > 0:
            cart_item.quantity = qty
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart_detail')

@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    food_name = cart_item.food_item.name
    cart_item.delete()
    messages.success(request, f"Removed {food_name} from your cart.")
    return redirect('cart_detail')
