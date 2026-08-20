from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart
from accounts.models import UserProfile
from .models import Order, OrderItem

@login_required
def checkout_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.warning(request, "Your cart is empty! Add some delicious items before checkout.")
        return redirect('menu')

    subtotal = sum(item.total_price for item in cart_items)
    delivery_fee = 50.00
    grand_total = float(subtotal) + delivery_fee

    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        delivery_address = request.POST.get('delivery_address')
        phone_number = request.POST.get('phone_number')

        if not delivery_address or not phone_number:
            messages.error(request, "Delivery address and phone number are required.")
            return render(request, 'orders/checkout.html', {
                'cart_items': cart_items,
                'subtotal': subtotal,
                'delivery_fee': delivery_fee,
                'grand_total': grand_total,
                'profile': profile,
            })

        # Update profile if blank
        if not profile.phone_number:
            profile.phone_number = phone_number
        if not profile.address:
            profile.address = delivery_address
        profile.save()

        # Create Order
        order = Order.objects.create(
            user=request.user,
            total_amount=grand_total,
            delivery_address=delivery_address,
            phone_number=phone_number,
            status='Pending'
        )

        # Create OrderItems
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                food_item=item.food_item,
                quantity=item.quantity,
                price=item.food_item.price
            )

        # Clear Cart
        cart_items.delete()

        messages.success(request, f"Order #{order.id} placed successfully! We're preparing your delicious meal.")
        return redirect('order_detail', order_id=order.id)

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'delivery_fee': delivery_fee,
        'grand_total': grand_total,
        'profile': profile,
    }
    return render(request, 'orders/checkout.html', context)

@login_required
def order_history_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})

@login_required
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # Status progression calculation for progress bar
    status_steps = ['Pending', 'Preparing', 'Out for Delivery', 'Delivered']
    try:
        current_step_index = status_steps.index(order.status)
    except ValueError:
        current_step_index = 0

    progress_percent = int(((current_step_index + 1) / len(status_steps)) * 100)

    context = {
        'order': order,
        'status_steps': status_steps,
        'current_step_index': current_step_index,
        'progress_percent': progress_percent,
    }
    return render(request, 'orders/order_detail.html', context)
