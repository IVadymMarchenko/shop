from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from carts.models import Cart
from .forms import OrderForm
from .models import Order, OrderItem
from django.http import JsonResponse
import requests


API_KEY_NOVA = "625a9f60043360a977eefc5929d79c79"
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print(request.POST.get('city'))
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_products = Cart.objects.filter(user=user)
                    # Вычисляем общую цену для отображения в шаблоне
                    total_price = sum(cart.product.sell_price() * cart.quantity for cart in cart_products)  
                    if cart_products:
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=f"{form.cleaned_data['city']}, Отделение №{form.cleaned_data['delivery_address']}", 
                            payment=form.cleaned_data['payment'],
                        )
                        for cart in cart_products:
                            product = cart.product
                            name = cart.product.name
                            price = cart.product.sell_price()
                            quantity = cart.quantity
                            if product.count < quantity:
                                raise ValueError(f'Товар {name} на складе осталось меньше {quantity} штук.')
                            
                            # Создаем OrderItem для каждого товара в корзине
                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            # Обновляем количество товара на складе
                            product.count -= quantity
                            product.save()
                        cart_products.delete()
                        messages.success(request, 'Заказ успешно оформлен')
                        return redirect('main:main')
            except ValueError as e:
                messages.error(request, str(e))
    else:
        initial = {
            'name': request.user.username,
            'email': request.user.email,
            'phone_number': getattr(request.user, 'phone', ''),
        }
        form = OrderForm(initial=initial)
    
    # Получаем корзину и рассчитываем общую цену
    cart_products = Cart.objects.filter(user=request.user)
    total_price = sum(cart.product.sell_price() * cart.quantity for cart in cart_products)
    
    context = {
        'title': 'Оформление заказа',
        'form': form,
        'total_price': total_price,
    }
    
    return render(request, 'orders/k_order.html', context=context)


def get_departments(request):
    city = request.GET.get('city')
    if not city:
        return JsonResponse({'error': 'City is required'}, status=400)
    
    # API ключ Новой Почты
    API_KEY = API_KEY_NOVA
    url = "https://api.novaposhta.ua/v2.0/json/"
    
    payload = {
        "apiKey": API_KEY,
        "modelName": "Address",
        "calledMethod": "getWarehouses",
        "methodProperties": {
            "CityName": city
        }
    }
    
    response = requests.post(url, json=payload)
    print(response.json())
    if response.status_code == 200:
        data = response.json()
        departments = data.get('data', [])
        return JsonResponse(departments, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch departments'}, status=500)