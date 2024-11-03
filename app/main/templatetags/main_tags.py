from django import template
from goods.models import Products,Categories
from carts.models import Cart




register=template.Library()


@register.simple_tag()
def tag_categories():
     return Categories.objects.all()


@register.simple_tag()
def user_carts(request):
    return Cart.objects.filter(user=request.user)
    
