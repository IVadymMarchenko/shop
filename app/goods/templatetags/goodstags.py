

from django import template
from django.views.generic.list import ListView
from goods.models import Products
from django.utils.http import urlencode
from goods.dbfilters import GetProduct


register=template.Library()


@register.simple_tag()
def tag_categories():
     return Products.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
     # Копируем GET-параметры из текущего запроса чтоб раб пагинац
    query_dict = context['request'].GET.copy()
    print(query_dict)
    for key, value in kwargs.items():
        if value is None:
            query_dict.pop(key, None)
        else:
            query_dict[key] = value
    return query_dict.urlencode()


@register.simple_tag()
def get_producer():
     get_product_instance = GetProduct()
     all_producer = get_product_instance.get_producer()
    # Преобразуем QuerySet в список и убираем дубликаты
     all_producer = list(dict.fromkeys(all_producer))
     return all_producer


@register.simple_tag()
def get_processor_model():
    # Используем distinct() для получения уникальных значений напрямую из базы данных
    processor_models = Products.objects.filter(
        processor_model__isnull=False
    ).order_by('processor_model').values_list('processor_model', flat=True).distinct()
    return processor_models

@register.simple_tag()
def get_videocard_model():
    videocard_model=Products.objects.filter(videocard_model__isnull=False).order_by('videocard_model').values_list('videocard_model',flat=True).distinct()
    return videocard_model


@register.simple_tag()
def get_ram():
    ram=Products.objects.filter(ram__isnull=False).order_by('ram').values_list('ram', flat=True).distinct()
    return ram
    
    
@register.simple_tag()
def get_hdd():
    hdd=Products.objects.filter(storage_type__isnull=False).order_by('storage_type').values_list('storage_type', flat=True).distinct()
    return hdd