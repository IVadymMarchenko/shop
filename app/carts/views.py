from django.shortcuts import get_object_or_404, redirect, render
from goods.models import Products
from .models import Cart
from django.http import JsonResponse
from django.template.loader import render_to_string
from .utils import get_user_carts

# Create your views here.

 

def cart_add(request):
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Products, id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    user_cart = get_user_carts(request)
    total_items = sum(cart_item.quantity for cart_item in user_cart)
    
    cart_item_html = render_to_string('main/cart_button.html', {'carts': user_cart}, request=request)
    cart_offcanvas_html = render_to_string('main/cart_offcanvass.html', {'carts': user_cart}, request=request)

    response_data = {
    "message": "Товар добавлен в корзину",
    "cart_items_html": cart_item_html,
    "cart_offcanvas_html": cart_offcanvas_html,
    "total_items": total_items,
}
    return JsonResponse(response_data)
        




def cart_change(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    
    if request.user.is_authenticated:
        quantity = int(request.POST.get('quantity', 1))
        
        cart, created = Cart.objects.get_or_create(user=request.user, product=product)
        cart.quantity = quantity
        cart.save()
        
        # Возвращаем JSON-ответ с новым количеством и подтверждением
        return JsonResponse({"message": "Quantity updated", "quantity": cart.quantity})
    
    return JsonResponse({"error": "User not authenticated"}, status=403)





def cart_remove(request,cart_id):
    cart= Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META.get('HTTP_REFERER')) # для перенаправ на ту страниц с котор пришел

