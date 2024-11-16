
from django.urls import reverse

from .models import Cart
from django.template.loader import render_to_string

class CartManager:
    
    def get_cart(self, request, product):
        if request.user.is_authenticated:
            return Cart.objects.filter(user=request.user, product=product).first()
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
            return Cart.objects.filter(session_key=session_key, product=product).first()
        
    
    def get_user_carts(self, request):
        """
        Получение всех объектов корзины для текущего пользователя
        или сессии.
        """
        if request.user.is_authenticated:
            # Возвращаем корзину для авторизованного пользователя
            return Cart.objects.filter(user=request.user).select_related('product')
        else:
            # Создаем сессию, если ее нет, и возвращаем корзину для сессии
            if not request.session.session_key:
                request.session.create()
            return Cart.objects.filter(session_key=request.session.session_key).select_related('product')
        
    def get_total_items(self, request):
        """
        Подсчёт общего количества товаров в корзине.
        """
        user_cart = self.get_user_carts(request)
        return sum(cart_item.quantity for cart_item in user_cart)
    
    

    def render_cart(self, request):
        user_cart = self.get_user_carts(request)
        return render_to_string('main/cart_button.html', {'carts': user_cart}, request=request)