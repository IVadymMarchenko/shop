from django.urls import path

from . import views



app_name = 'orders'


urlpatterns = [
     path("get_departments/", views.get_departments, name="get_departments"),
     path("create_order/", views.CreateOrderView.as_view(), name="create_order"),   
]