from django.shortcuts import get_object_or_404, redirect, render
from goods.models import Products
from .models import Cart
from django.http import JsonResponse
# Create your views here.



def cart_add(request,product_slug):
    product= Products.objects.get(slug=product_slug)
    
    if request.user.is_authenticated:
        
        carts=Cart.objects.filter(user=request.user,product=product)
        if carts.exists():
            cart=carts.first()
            if cart:
                cart.quantity+=1
                cart.save()
        else:
            Cart.objects.create(user=request.user,product=product,quantity=1)
    else:
        return redirect('user:registration')
    return redirect(request.META.get('HTTP_REFERER')) # для перенаправ на ту страниц с котор пришел
        




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

