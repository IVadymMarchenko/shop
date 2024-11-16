from django.urls import path

from . import views



app_name = 'carts'


urlpatterns = [
     path("cart_add/", views.CartAddView.as_view(), name="cart_add"),
     path("cart_change/<int:product_id>/", views.CartChangeView.as_view(), name="cart_change"),
     path("cart_remove/<int:cart_id>/", views.CartRemoveView.as_view(), name="cart_remove")]