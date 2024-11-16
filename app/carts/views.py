from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .cart_manager import CartManager
from goods.models import Products
from .models import Cart
from django.http import JsonResponse
from django.template.loader import render_to_string

from django.contrib import auth,messages

# Create your views here.

class CartAddView(CartManager,View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Products, id=product_id)

        cart = self.get_cart(request, product=product)
        if cart:
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(
                user=request.user if request.user.is_authenticated else None,
                session_key=request.session.session_key if not request.user.is_authenticated else None,
                product=product,
                quantity=1
            )
        user_cart = self.get_user_carts(request)
        total_items = self.get_total_items(request)

        response_data = {
            "message": "Товар додано в кошик",
            "cart_items_html": self.render_cart(request),
            "cart_offcanvas_html": render_to_string('main/cart_offcanvass.html', {'carts': user_cart}, request=request),
            "total_items": total_items,
        }
        return JsonResponse(response_data)
        

class CartChangeView(CartManager, View):
    """Предст для изменения колич товара в корзине."""

    def post(self, request, product_id):
        product = get_object_or_404(Products, id=product_id)
        quantity = int(request.POST.get('quantity', 1))

        # Получаем или создаём объект корзины
        cart = self.get_cart(request, product=product)
        
        if cart:
            cart.quantity = quantity
            cart.save()
            return JsonResponse({"message": "Quantity updated", "quantity": cart.quantity})
        
        return JsonResponse({"error": "Unable to update cart"}, status=400)


class CartRemoveView(View):
    """Представление для удаления товара из корзины."""
    def post(self, request, cart_id):
        try:
            # Получаем объект корзины по cart_id
            cart = Cart.objects.get(id=cart_id)
            cart.delete()
            # Добавляем сообщение об успешном удалении
            messages.success(request, "Товар успішно видалено.")
        except Cart.DoesNotExist:
            # Если товар не найден, выводим ошибку
            messages.error(request, "Щось пішло не так.")
        # Перенаправляем обратно на предыдущую страницу
        return redirect(request.META.get('HTTP_REFERER'))
        

















































# def cart_change(request, product_id):
#     product = get_object_or_404(Products, id=product_id)
#     quantity = int(request.POST.get('quantity', 1))
#     if request.user.is_authenticated:
#         # Для авторизованных пользователей
#         cart, created = Cart.objects.get_or_create(user=request.user, product=product)
#         cart.quantity = quantity
#         cart.save()  
#         return JsonResponse({"message": "Quantity updated", "quantity": cart.quantity})
#     else:
#         # Для неавторизованных пользователей - работа с корзиной по session_key
#         session_key = request.session.session_key
#         if not session_key:
#             request.session.create()  # Создаем сессию, если её нет
#         cart, created = Cart.objects.get_or_create(session_key=session_key, product=product)
#         cart.quantity = quantity
#         cart.save()
#         return JsonResponse({"message": "Quantity updated", "quantity": cart.quantity})
#     return JsonResponse({"error": "Unable to update cart"}, status=400)





# def cart_add(request):
#     product_id = request.POST.get('product_id')
#     product = get_object_or_404(Products, id=product_id)

#     if request.user.is_authenticated:
#         carts = Cart.objects.filter(user=request.user, product=product)
#         if carts.exists():
#             cart = carts.first()
#             cart.quantity += 1
#             cart.save()
#         else:
#             Cart.objects.create(user=request.user, product=product, quantity=1)
#     else:
#         carts=Cart.objects.filter(session_key=request.session.session_key, product=product)
#         if carts.exists():
#             cart = carts.first()
#             if cart:
#                 cart.quantity += 1
#                 cart.save()
#         else:
#             Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)

#     user_cart = get_user_carts(request)
#     total_items = sum(cart_item.quantity for cart_item in user_cart)
    
#     cart_item_html = render_to_string('main/cart_button.html', {'carts': user_cart}, request=request)
#     cart_offcanvas_html = render_to_string('main/cart_offcanvass.html', {'carts': user_cart}, request=request)

#     response_data = {
#     "message": "Товар додано в кошик",
#     "cart_items_html": cart_item_html,
#     "cart_offcanvas_html": cart_offcanvas_html,
#     "total_items": total_items,
# }
#     return JsonResponse(response_data)
        



# def cart_remove(request, cart_id):
#     try:
#         cart = Cart.objects.get(id=cart_id)
#         cart.delete()
#         # Добавляем сообщение об успешном удалении товара
#         messages.success(request, "Товар успішно видалено.")
#     except Cart.DoesNotExist:
#         messages.error(request, "Щось пішло не так.")
    
#     # Перенаправляем обратно на предыдущую страницу
#     return redirect(request.META.get('HTTP_REFERER'))

