from django import template
from carts.models import Cart

register = template.Library()
def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)
    else:
        # Если пользователь не авторизован, возвращаем корзину по сессионному ключу
        session_key = request.session.session_key
        if not session_key:
            request.session.create()  # создаем сессию, если ее нет
            session_key = request.session.session_key
        return Cart.objects.filter(session_key=session_key)

@register.simple_tag()
def user_carts(request):
    
    return get_user_carts(request)
    