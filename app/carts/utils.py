
from .models import Cart


def get_user_carts(request):
    if request.user.is_authenticated:
        # Для авторизованных пользователей
        return Cart.objects.filter(user=request.user)
    else:
        # Для анонимных пользователей
        if not request.session.session_key:
            request.session.create()  # создаем сессию, если ее нет
        return Cart.objects.filter(session_key=request.session.session_key)