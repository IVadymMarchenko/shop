from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.views import View
from carts.models import Cart
from .forms import OrderForm
from .models import Order, OrderItem
from django.http import JsonResponse
import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView


API_KEY_NOVA = "625a9f60043360a977eefc5929d79c79"



class CreateOrderView(LoginRequiredMixin, FormView):
    template_name = "orders/k_order.html"
    form_class = OrderForm
    success_url = 'main:main'

    def get_initial(self):
        """Заполняем начальные данные формы для текущего пользователя."""
        initial = super().get_initial()
        initial['name'] = self.request.user.first_name
        initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        """Обрабатываем корректную форму и создаем заказ."""
        try:
            with transaction.atomic():
                user = self.request.user
                cart_products = Cart.objects.filter(user=user)
                if cart_products:
                    # Создаем заказ
                    order = Order.objects.create(
                        user=user,
                        phone_number=form.cleaned_data['phone_number'],
                        requires_delivery=form.cleaned_data['requires_delivery'],
                        delivery_address=f"{form.cleaned_data['city']}, {form.cleaned_data['delivery_address']}", 
                        payment=form.cleaned_data['payment'],
                    )
                    
                    # Обрабатываем каждый товар в корзине
                    for cart in cart_products:
                        product = cart.product
                        name = product.name
                        price = product.sell_price()
                        quantity = cart.quantity
                        
                        if product.count < quantity:
                            raise ValueError(f'Товар {name} на складе осталось меньше {quantity} штук.')

                        # Создаем OrderItem для каждого товара
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

                    # Очищаем корзину
                    cart_products.delete()
                    
                    # Отправляем сообщение об успешном оформлении
                    messages.success(self.request, 'Заказ успешно оформлен')
                    return redirect(self.success_url)
        except ValueError as e:
            # Если есть ошибка (например, недостаточно товара на складе), показываем сообщение
            messages.error(self.request, str(e))
            return redirect(self.success_url)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Помилка у формі. Перевірте правильність введених даних.')
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs):
        """Передаем дополнительные данные в контекст."""
        context = super().get_context_data(**kwargs)
        
        # Получаем корзину и рассчитываем общую цену
        cart_products = Cart.objects.filter(user=self.request.user)
        total_price = sum(cart.product.sell_price() * cart.quantity for cart in cart_products)
        
        # Добавляем информацию о корзине и общей сумме
        context['title'] = 'Оформлення замовлення'
        context['total_price'] = total_price
        return context


       
class GetDepartmentsView(View):
    API_KEY = API_KEY_NOVA  # Замените на свой API-ключ

    def get(self, request, *args, **kwargs):
        city_ref = request.GET.get('city')
        if not city_ref:
            return JsonResponse({'error': 'City reference is required'}, status=400)

        url = "https://api.novaposhta.ua/v2.0/json/"
        payload = {
            "apiKey": self.API_KEY,
            "modelName": "Address",
            "calledMethod": "getWarehouses",
            "methodProperties": {
                "CityRef": city_ref
            }
        }

        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            departments = data.get('data', [])
            return JsonResponse(departments, safe=False)
        else:
            return JsonResponse({'error': 'Failed to fetch departments'}, status=500)



class GetCitiesView(View):
    API_KEY = API_KEY_NOVA  # Замените на свой API-ключ

    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('search', '')
        url = "https://api.novaposhta.ua/v2.0/json/"
        payload = {
            "apiKey": self.API_KEY,
            "modelName": "Address",
            "calledMethod": "getCities",
            "methodProperties": {
                "FindByString": search_query
            }
        }

        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            cities = [
                {"name": city["Description"], "ref": city["Ref"]}
                for city in data.get("data", [])
            ]
            return JsonResponse(cities, safe=False)
        else:
            return JsonResponse({'error': 'Failed to fetch cities'}, status=500)





















# def get_departments(request):
#     city = request.GET.get('city')
#     if not city:
#         return JsonResponse({'error': 'City is required'}, status=400) 
#     # API ключ Новой Почты
#     API_KEY = API_KEY_NOVA
#     url = "https://api.novaposhta.ua/v2.0/json/"
    
#     payload = {
#         "apiKey": API_KEY,
#         "modelName": "Address",
#         "calledMethod": "getWarehouses",
#         "methodProperties": {
#             "CityName": city
#         }
#     }
    
#     response = requests.post(url, json=payload)
#     if response.status_code == 200:
#         data = response.json()
#         departments = data.get('data', [])
#         return JsonResponse(departments, safe=False)
#     else:
#         return JsonResponse({'error': 'Failed to fetch departments'}, status=500)












































































# @login_required
# def create_order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
     
#         if form.is_valid():
#             try:
#                 with transaction.atomic():
#                     user = request.user
#                     cart_products = Cart.objects.filter(user=user)
#                     total_price = sum(cart.product.sell_price() * cart.quantity for cart in cart_products)  
#                     if cart_products:
#                         order = Order.objects.create(
#                             user=user,
#                             phone_number=form.cleaned_data['phone_number'],
#                             requires_delivery=form.cleaned_data['requires_delivery'],
#                             delivery_address=f"{form.cleaned_data['city']}, Отделение №{form.cleaned_data['delivery_address']}", 
#                             payment=form.cleaned_data['payment'],
#                         )
#                         for cart in cart_products:
#                             product = cart.product
#                             name = cart.product.name
#                             price = cart.product.sell_price()
#                             quantity = cart.quantity
#                             if product.count < quantity:
#                                 raise ValueError(f'Товар {name} на складе осталось меньше {quantity} штук.')
                            
#                             # Создаем OrderItem для каждого товара в корзине
#                             OrderItem.objects.create(
#                                 order=order,
#                                 product=product,
#                                 name=name,
#                                 price=price,
#                                 quantity=quantity,
#                             )
#                             # Обновляем количество товара на складе
#                             product.count -= quantity
#                             product.save()
#                         cart_products.delete()
#                         messages.success(request, 'Заказ успешно оформлен')
#                         return redirect('main:main')
#             except ValueError as e:
#                 messages.error(request, str(e))
#     else:
#         initial = {
#             'name': request.user.username,
#             'email': request.user.email,
#             'phone_number': getattr(request.user, 'phone', ''),
#         }
#         form = OrderForm(initial=initial)
    
#     # Получаем корзину и рассчитываем общую цену
#     cart_products = Cart.objects.filter(user=request.user)
#     total_price = sum(cart.product.sell_price() * cart.quantity for cart in cart_products)
    
#     context = {
#         'title': 'Оформление заказа',
#         'form': form,
#         'total_price': total_price,
#     }
  
#     return render(request, 'orders/k_order.html', context=context)




# def get_departments(request):
#     city = request.GET.get('city')
#     if not city:
#         return JsonResponse({'error': 'City is required'}, status=400) 
#     # API ключ Новой Почты
#     API_KEY = API_KEY_NOVA
#     url = "https://api.novaposhta.ua/v2.0/json/"
    
#     payload = {
#         "apiKey": API_KEY,
#         "modelName": "Address",
#         "calledMethod": "getWarehouses",
#         "methodProperties": {
#             "CityName": city
#         }
#     }
    
#     response = requests.post(url, json=payload)
#     if response.status_code == 200:
#         data = response.json()
#         departments = data.get('data', [])
#         return JsonResponse(departments, safe=False)
#     else:
#         return JsonResponse({'error': 'Failed to fetch departments'}, status=500)